#!/usr/bin/env python3
import xlsxwriter

input_txt = "/tmp/security_patch_report.txt"
output_xlsx = "/tmp/security_patch_report.xlsx"

workbook = xlsxwriter.Workbook(output_xlsx)
worksheet = workbook.add_worksheet()

with open(input_txt, "r") as file:
    for row_num, line in enumerate(file):
        parts = [cell.strip() for cell in line.strip().split("|")]
        for col_num, value in enumerate(parts):
            worksheet.write(row_num, col_num, value)

workbook.close()
