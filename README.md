# ironvault-oracle-template
Contains a script to generate a markdown template for homebrew oracles to use in Ironvault Obsidian

## How to use

For general use cases, you 


### Note!: About filenames



## Generate custom file

### Command
```python generate.py [dice_expression]```

### Arguments and flags
positional arguments:
  dice_expression       Dice notation of what dice the oracle should roll on. Currently supports only dY and XdY
                        format ('d4', '1d6', '2d10' etc)

options:
```
  -h, --help            Shows this help message and exit
  -r, --rows [ROWS]     Expected number of results. An non-zero input value here, along with a dice experssion of dY,
                        will result in dice values being consolidated in that many rows (a d6 with rows of 3 result in
                        1-2, 3-4, 5-6 columns). In the event that that the values cannot be evenly split, the extra
                        values will be spread among the rows, starting from the first row. Does nothing for XdY where
                        X is not 1
  -o, --output-file_name [OUTPUT_FILE_NAME]
                        Name of the generated file (excluding file extension). Note that this must not begin with a
                        number, as this will cause ironvault to fail reading the file
  -d, --description [DESCRIPTION]
                        Description to place in resulting oracle file
  -w, --overwrite       Automatically overwrites file without prompting
  -i, --input-file [INPUT_FILE]
                        Path to file containing values to fill in results (including file extension)
  -s, --separator [SEPARATOR]
                        Delimiter used to read values from input file. Newline by default
  -n, --no-auto-trim    By default, the system will attempt to trim resulting values from input files, i.e, it
                        prevents row values from containing whitespaces and newlines at the start and end. set this to
                        stop it from doing so
  -p, --print-debug     Set this to allow the system to print messages, mainly for debugging purposes
```

## Testing
Testing is done via pytest, which needs to be installed via pip. 

Calling the pytest command will then run various tests found in test_generate.py. 

It's highly recommanded to run this if you intend to make any changes to the program.

### Installation of pytest

```pip install -r requirements.txt```

### To Run Tests 

```pytest```
