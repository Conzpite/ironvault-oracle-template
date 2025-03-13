from generate import extract_dice_values, generate_header, retrieve_dataset_value
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