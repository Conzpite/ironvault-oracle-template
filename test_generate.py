from generate import extract_dice_values, generate_header, retrieve_dataset_value, generate_table_values, read_dataset, create_default_filename
import pytest

class TestExtractDice:
    def test_extract_dice(self):
        assert extract_dice_values('1d6') == (1, 6);

    def test_extract_dice_no_count(self):
        assert extract_dice_values('d6') == (1, 6);

    def test_extract_dice_with_count(self):
        assert extract_dice_values('3d20') == (3, 20);

    def test_extract_dice_error_bad_expression(self):
        with pytest.raises(ValueError):
            extract_dice_values('td6');

    def test_extract_dice_error_zero_count(self):
        with pytest.raises(ValueError):
            extract_dice_values('0d6');

    def test_extract_dice_error_zero_sides(self):
        with pytest.raises(ValueError):
            extract_dice_values('1d0');

class TestGenerateHeader:
    def test_generate_header(self):
        assert generate_header('Header Value') == '''---
type: oracle_rollable
description: Header Value
---
'''

class TestRetrieveDatasetValue:
    def test_retrieve_dataset_value_no_dataset(self):
        assert retrieve_dataset_value(7) == "Value 8";

    def test_retrieve_dataset_value_empty_dataset(self):
        assert retrieve_dataset_value(5, []) == "Value 6";

    def test_retrieve_dataset_value_with_dataset(self):
        assert retrieve_dataset_value(5, ["Dataset 1", "Dataset 2", "Dataset 3", "Dataset 4", "Dataset 5", "Dataset 6", "Dataset 7", "Dataset 8"]) == "Dataset 6";

    def test_retrieve_dataset_value_with_dataset_out_of_bounds(self):
        assert retrieve_dataset_value(10, ["Dataset 1", "Dataset 2", "Dataset 3", "Dataset 4", "Dataset 5", "Dataset 6", "Dataset 7", "Dataset 8"]) == "VALUE OUT OF BOUNDS";

class TestGenerateTableValue:
    def test_generate_table_value_1d6(self):
        assert generate_table_values(1, 6, 0, []) == (["1", "2", "3", "4", "5", "6"], 
                                                      ["Value 1", "Value 2", "Value 3", "Value 4", "Value 5", "Value 6"]);

    def test_generate_table_value_1d6_into_5_rows(self):
        assert generate_table_values(1, 6, 5, []) == (["1-2", "3", "4", "5", "6"], 
                                                      ["Value 1", "Value 2", "Value 3", "Value 4", "Value 5"]);

    def test_generate_table_value_1d6_with_dataset(self):
        assert generate_table_values(1, 6, 0, ["Dataset 1", "Dataset 2", "Dataset 3", "Dataset 4", "Dataset 5", "Dataset 6", "Dataset 7", "Dataset 8"]) ==  \
                                                      (["1", "2", "3", "4", "5", "6"], 
                                                      ["Dataset 1", "Dataset 2", "Dataset 3", "Dataset 4", "Dataset 5", "Dataset 6"]);

    def test_generate_table_value_2d4(self):
        assert generate_table_values(2, 4, 0, []) == (["2", "3", "4", "5", "6", "7", "8"], 
                                                      ["Value 1", "Value 2", "Value 3", "Value 4", "Value 5", "Value 6", "Value 7"]);

    def test_generate_table_value_2d4_into_5_rows(self):
        assert generate_table_values(2, 4, 5, []) == (["2-3", "4-5", "6", "7", "8"], 
                                                      ["Value 1", "Value 2", "Value 3", "Value 4", "Value 5"]);

    def test_generate_table_value_2d4_with_dataset(self):
        assert generate_table_values(2, 4, 0, ["Dataset 1", "Dataset 2", "Dataset 3", "Dataset 4", "Dataset 5", "Dataset 6", "Dataset 7", "Dataset 8"]) ==  \
                                                      (["2", "3", "4", "5", "6", "7", "8"], 
                                                      ["Dataset 1", "Dataset 2", "Dataset 3", "Dataset 4", "Dataset 5", "Dataset 6", "Dataset 7"]);

    def test_generate_table_value_d20_into_5_rows(self):
        assert generate_table_values(1, 20, 5, []) == (["1-4", "5-8", "9-12", "13-16", "17-20"], 
                                                      ["Value 1", "Value 2", "Value 3", "Value 4", "Value 5"]);

    def test_generate_table_value_d20_into_5_rows_with_dataset(self):
        assert generate_table_values(1, 20, 5, ["Dataset 1", "Dataset 2", "Dataset 3", "Dataset 4", "Dataset 5", "Dataset 6", "Dataset 7", "Dataset 8"]) ==  \
                                                      (["1-4", "5-8", "9-12", "13-16", "17-20"], 
                                                      ["Dataset 1", "Dataset 2", "Dataset 3", "Dataset 4", "Dataset 5"]);

class TestReadDataset:
    def test_read_dataset_delimiter_newline(self):
        assert read_dataset("Dataset 1\nDataset 2\nDataset 3", "\n", True) == ["Dataset 1", "Dataset 2", "Dataset 3"];

    def test_read_dataset_delimiter_comma(self):
        assert read_dataset("Dataset 1,Dataset 2,Dataset 3", ",", True) == ["Dataset 1", "Dataset 2", "Dataset 3"];

    def test_read_dataset_trim(self):
        assert read_dataset("Dataset 1  \n  Dataset 2\n     Dataset 3", "\n", True) == ["Dataset 1", "Dataset 2", "Dataset 3"];

    def test_read_dataset_without_trim(self):
        assert read_dataset("Dataset 1  \n  Dataset 2\n     Dataset 3", "\n", False) == ["Dataset 1  ", "  Dataset 2", "     Dataset 3"];

    def test_read_dataset_with_newline_in_text(self):
        assert read_dataset("Dataset 1\nDescription 1,Dataset 2\nDescription 2,Dataset 3\nDescription 3", ",", True) == ["Dataset 1<br>Description 1", "Dataset 2<br>Description 2", "Dataset 3<br>Description 3"];

class TestCreateDefaultFileName:
    def test_create_default_filename(self):
        assert create_default_filename("1d6", 0) == "t_d6"

    def test_create_default_filename_more_than_one_die(self):
        assert create_default_filename("3d10", 0) == "t_3d10"

    def test_create_default_filename_with_expected_rows(self):
        assert create_default_filename("1d6", 3) == "t_d6_3"

    def test_create_default_filename_more_than_one_die_with_expected_rows(self):
        assert create_default_filename("3d10", 3) == "t_3d10_3"

    def test_create_default_filename_more_than_one_die_with_expected_rows(self):
        assert create_default_filename("3d10", 100) == "t_3d10"

    def test_create_default_filename_too_much_expected_rows_from_one_die(self):
        assert create_default_filename("1d6", 100) == "t_d6"

    def test_create_default_filename_too_much_expected_rows_from_multiple_dice(self):
        assert create_default_filename("3d10", 100) == "t_3d10"

