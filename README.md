# Ironvault Oracle Templates

This is created as a way for me to generate oracle templates for homebrewing ironvault without typing the whole thing out by hand. Feel free to use as you wish.

## How to use

If you intend to only use the pre-generated templates, you can simply download just the Templates folder.

Each file follow the same naming convention:
1. Prefix ("t_")
2. Dice expression ("1d6", "2d20")
3. Number of rows ("_3", "_10"), exempted if every row represents one and only one value of the dice
4. Description of what the template is may be used for ("_delve_denizen"), exempted for general oracle templates

To test using the template folder:
1. Add the Templates folder to your homebrew directory. Make sure homebrew content is enabled in the ironvault plugins settings
2. Create a new campaign/Edit an existing campaign
3. Ensure that the Custom playset is selected
4. Click on the Configure button
5. Ensure the Custom Playset is selected here
6. Add '*:templates/\*\*' to the text field
7. Click select, then save
8. Click on any page on the campaign
9. If you don't have a right pane currently, click on the expand button on the top right of your toolbar (Right beside the minimize button)
10. Select the IronVault button at the top right of your right pane (You may have to drag out the right pane to see it), and make sure Oracle is selected
11. Select 'Templates/Basic Templates'
12. Click on any of the templates to activate it. (Note that as of ironvault 1.89.4, the files seem to only be recognizable by the system only after the template files are directly opened at least once in obsidian. If you can only see a few of the templates whenever you add a new file, try to open it directly in obsidian and see if it appears in the list afterwards)

Then, whenever you need a template to work off, copy and paste the template you wish to use, renaming the file and adjusting the description and contents accordingly.

If you intend to generate your own custom templates, continue below...

## Generate custom file

Run the generate.py file to generate a custom file. 

If successful, a new file will be writen in the output folder. 

By default, if no name is provided, then a filename is automatically generated ("t_d6", "t_3d10", "t_d100_3" etc...)

### Command
```python generate.py [dice_expression]```

### Arguments and flags
```
positional arguments:
  dice_expression       Dice notation of what dice the oracle should roll on. Currently supports only dY and XdY
                        format ('d4', '1d6', '2d10' etc)

options:
  -h, --help            Shows this help message and exit
  -r, --rows [ROWS]     Expected number of results. A non-zero input value here, along with a dice experssion of dY,
                        will result in dice values being consolidated in that many rows (a d6 with rows of 3 result in
                        1-2, 3-4, 5-6 columns). In the event that that the values cannot be evenly split, the extra
                        values will be spread among the rows, starting from the first row
  -o, --output-file_name [OUTPUT_FILE_NAME]
                        Name of the generated file (excluding .md file extension). If left blank/not used, will
                        default to a generated name instead.
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

It's highly recommanded to run this if you have made any changes to the program.

### Installation of pytest

```pip install -r requirements.txt```

### To Run Tests 

```pytest```
