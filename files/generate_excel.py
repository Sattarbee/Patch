#!/usr/bin/env python3

import os
import json
import xlsxwriter

output_dir = '/tmp'
report_file = os.path.join(output_dir, 'yum_security_report.xlsx')

workbook = xlsxwriter.Workbook(report_file)
worksheet = workbook.add_worksheet("Security Updates")

# Header
headers = ['Host', 'FQDN', 'Date', 'Security Updates']
for col, h in enumerate(headers):
    worksheet.write(0, col, h)

row = 1
for filename in os.listdir(output_dir):
    if filename.startswith("yum_output_") and filename.endswith(".json"):
        with open(os.path.join(output_dir, filename)) as f:
            data = json.load(f)
            updates = "\n".join(data["output"]) if data["output"] else "No Updates"
            worksheet.write(row, 0, data["host"])
            worksheet.write(row, 1, data["fqdn"])
            worksheet.write(row, 2, data["date"])
            worksheet.write(row, 3, updates)
            row += 1

workbook.close()
