import argparse
import os
import re

def extract_dice_values(dice_expression):
    # Validate dice expression
    r = re.search(r"^(\d*)[dD]([\d]+)$", dice_expression);

    if not r:
        raise ValueError("Invalid dice expression");

    dice_count = int(r.group(1) or 1)
    dice_size = int(r.group(2))

    if dice_count <= 0:
        raise ValueError("Invalid dice expression");
    
    if dice_size <= 0:
        raise ValueError("Invalid dice expression");

    return dice_count, dice_size;
    
def retrieve_dataset_value(index, dataset=[]):
    if len(dataset) == 0:
        return "Value {}".format(index + 1);
    
    if index < len(dataset):
        return dataset[index];

    return "VALUE OUT OF BOUNDS";

def generate_table(dice_expression, expected_rows=0, dataset=[]):
    [dice_num, dice_sides] = extract_dice_values(dice_expression);

    dice_expression_header_str = "dice: {}".format(dice_expression);
    result_header_str = "Result";

    dice_values_col = [];
    result_col = [];
    dataset_index = 0;

    if dice_num == 1:
        if expected_rows != 0:
            # Calculate values based on expected rows
            for x in range(expected_rows):
                dataset_index += 1;
                return;
        else:
            # Each value from 1 to dice_side is its own row
            for x in range(dice_sides):
                dice_values_col.append(str(x + 1));
                result_col.append(retrieve_dataset_value(dataset_index));
                dataset_index += 1
    else:
        # Calulate all possible value of the dice as its own row
        # This is not affected in any way by expected_rows
        for x in range(dice_sides):
            dataset_index += 1;
            return;

    # Go another round to pad out values for a nicer look
    dice_values_col_max_length = max(len(dice_expression_header_str), max([len(i) for i in dice_values_col], default=0));
    result_col_max_length = max(len(result_header_str), max([len(i) for i in result_col], default=0));

    dice_expression_header_str = dice_expression_header_str.ljust(dice_values_col_max_length);
    result_header_str = result_header_str.ljust(result_col_max_length);

    dice_values_col = map(lambda x: x.ljust(dice_values_col_max_length), dice_values_col)
    result_col = map(lambda x: x.ljust(result_col_max_length), result_col)

    
    output = "";

    output += '| {} | {} |\n'.format(dice_expression_header_str, result_header_str);
    output += '| {} | {} |\n'.format('-' * dice_values_col_max_length, '-' * result_col_max_length);

    for a, b in zip(dice_values_col, result_col):
        output += '| {} | {} |\n'.format(a, b);

    return output;

def generate_header(description):
    description;

    val =  '''---
type: oracle_rollable
description: {}
---
'''.format(description);

    return val;

def write_to_file(header, body, fileName, filePath='output/'):
    # TODO Check for existing file, and confirm override

    with open(filePath + fileName, "w") as f:
        print("Writing " + fileName + "...");
        f.write(header);
        f.write(body);

def retrieve_dataset_from_file(filepath, delimiter):
    if not filepath:
        return [];

    return [];

def main():
    parser = argparse.ArgumentParser("Generate a .md file to serve as a homebrew oracle for iron vault obsidian")
    parser.add_argument("dice_expression", help="Dice notation of what dice the oracle should roll on. Currently supports only dY and XdY format ('d4', '1d6', '2d10' etc).", type=str)
    parser.add_argument("-r", "--rows", nargs="?", default=0, const=0, help="Expected number of results. An non-zero input value here, along with a dice experssion of dY, will result in dice values being consolidated in that many rows (a d6 with rows of 3 result in 1-2, 3-4, 5-6 columns). In the event that that the values cannot be evenly split, the extra values will be spread among the rows, starting from the first row. Does nothing for XdY where X is not 1.", type=int)
    parser.add_argument("-o", "--output-file_name", nargs="?", default="output", const="output", help="Name of the generated file (excluding file extension)", type=str)
    parser.add_argument("-i", "--input-file", nargs="?", default="", const="", help="Path to file containing values to fill in results (including file extension)", type=str)
    parser.add_argument("-s", "--separator", nargs="?", default="\n", const="\n", help="Delimiter used to read values from input file. Newline by default.",  type=str)
    parser.add_argument("-d", "--description", nargs="?", default="Here is a descripton of my oracle", const="Here is a descripton of my oracle", help="Description to place in resulting oracle file",  type=str)
    args = parser.parse_args()

    print(args);
    # Take in file to extract data from, and delimiter
    dataset = retrieve_dataset_from_file(args.input_file, args.separator);

    header = generate_header(args.description);
    body = generate_table(args.dice_expression, args.rows, dataset);

    print(header);
    print(body);

    # Write MD file
    write_to_file(header, body, args.output_file_name)


if __name__ == "__main__":
    main()