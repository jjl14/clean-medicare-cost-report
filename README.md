# clean-medicare-cost-report
Code for extracting desired variables from the public Medicare Cost Reports datasets.


Medicare documentation files

1996 form version raw data documentation downloaded from: https://www.cms.gov/Research-Statistics-Data-and-Systems/Downloadable-Public-Use-Files/Cost-Reports/Hospital-1996-form.html

2010 form version raw data documentation downloaded from:
https://www.cms.gov/Research-Statistics-Data-and-Systems/Downloadable-Public-Use-Files/Cost-Reports/Hospital-2010-form.html

1996 form original source removed, but equivalent to download and piecing together of individual worksheets from: https://www.costreportdata.com/worksheet_formats.html 

2010 form downloaded from:
https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/Downloads/R3P240f.pdf

1996 instructions (with explanations of each form item) downloaded from: https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/downloads/R8P236.pdf

2010 instructions (with explanations of each form item) downloaded from: https://www.cms.gov/Regulations-and-Guidance/Guidance/Transmittals/downloads/R1P240.pdf


Instructions for use

1) Look at the documentation files to note the (worksheet ID, line number, column number, and variable name) of each desired variable and modify clean_cost_report.py to include those.
  a. Note that any 'A' characters in the column identifier on the worksheet are converted to '1' for potential looping convenience.
  b. When entering a line number or column number, add '00' after the number itself. For example, to get line 1, enter 100. Enter the worksheet and variable name as strings, and enter the line and column numbers as numbers.
  c. Convert the worksheet names (e.g., 'Worksheet S-2, Part I') into worksheet IDs (e.g., 'S200001') with the worksheet codes file in the raw data documentation.
  d. The sample variable lists given are for the 1996 form. 
2) Download and unzip the folders for the desired years from the Medicare Cost Reports archive: https://www.cms.gov/Research-Statistics-Data-and-Systems/Downloadable-Public-Use-Files/Cost-Reports/Cost-Reports-by-Fiscal-Year.html. Make sure to download the 'Hospital' type files.
3) In clean_costreport.py, change the 'userdirectory' variable to the relevant path. It should be the path for the folder that contains the unzipped folders with titles like 'HOSPFY2010' and 'HOSP10FY2010.'
4) Go to the folder with clean_cost_report.py on Terminal.
5) Type 'python clean_cost_report.py [VERSION] [START YEAR] [END YEAR]', where [VERSION] is replaced by 'version1996' or 'version2010' and [START YEAR] and [END YEAR] are replaced by the first and last years of data desired by the user, e.g., '2011 2014'.*


* The form version is taken as an explicit argument to emphasize that the program must be run separately on each form version. This is because the line and column number for the same variable may differ across form versions, so they must be selected for each form version separately. If the user’s chosen time range includes a year during which CMS accepted both form versions (such that the user must use both form versions to get the complete dataset of all hospitals), then a warning is printed.

** Note that this was written for Python 3. Python 2 users may have to make additional changes (e.g., 'print()' to 'print ').

