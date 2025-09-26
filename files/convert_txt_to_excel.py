#!/usr/bin/env python3
import sys
import xlsxwriter

# Accept input/output paths from command line
if len(sys.argv) != 3:
    print("Usage: convert_txt_to_excel.py <input_txt> <output_xlsx>")
    sys.exit(1)

input_txt = sys.argv[1]
output_xlsx = sys.argv[2]

workbook = xlsxwriter.Workbook(output_xlsx)
worksheet = workbook.add_worksheet()

with open(input_txt, "r") as file:
    for row_num, line in enumerate(file):
        worksheet.write(row_num, 0, line.strip())

workbook.close()
