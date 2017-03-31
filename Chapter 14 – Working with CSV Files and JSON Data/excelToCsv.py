#! usr/bin/env python3

# excelToCsv.py - A script which makes a csv version of any xlsx file in
# the active directory

import os, openpyxl, csv

for excelFile in os.listdir('.'):
    # Skip non-xlsx files, load the workbook object.
    if not excelFile.endswith('.xlsx'):
        continue    # skip non-xlsx files
    wb = openpyxl.load_workbook(excelFile)
    for sheetName in wb.get_sheet_names():
        # Loop through every sheet in the workbook.
        sheet = wb.get_sheet_by_name(sheetName)

        # Create the CSV filename from the Excel filename and sheet title.
        basename = os.path.splitext(excelFile)[0]
        csvFilename = basename + '_' + str(sheet) + '.csv'
        # Create the csv.writer object for this CSV file.
        csvFile = open(os.path.join(csvFilename), 'w', newline='')
        csvWriter = csv.writer(csvFile)

        # Loop through every row in the sheet.
        for rowNum in range(1, sheet.max_row +1):
            rowData = []    # append each cell to this list
            # Loop through each cell in the row.
            for colNum in range(1, sheet.max_column +1):
                # Append each cell's data to rowData.
                cellValue = sheet.cell(row=rowNum, column=colNum).value
                rowData.append(str(cellValue))

            # Write the rowData list to the CSV file.
            csvWriter.writerow(rowData)
                
        csvFile.close()
