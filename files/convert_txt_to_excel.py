#!/usr/bin/env python3
import sys
import xlsxwriter

# Check for arguments
if len(sys.argv) != 3:
    print("Usage: convert_txt_to_excel.py <input_txt_file> <output_xlsx_file>")
    sys.exit(1)

input_txt = sys.argv[1]
output_xlsx = sys.argv[2]

workbook = xlsxwriter.Workbook(output_xlsx)
worksheet = workbook.add_worksheet()

with open(input_txt, "r") as file:
    for row_num, line in enumerate(file):
        parts = [cell.strip() for cell in line.strip().split("|")]
        for col_num, value in enumerate(parts):
            worksheet.write(row_num, col_num, value)

workbook.close()
