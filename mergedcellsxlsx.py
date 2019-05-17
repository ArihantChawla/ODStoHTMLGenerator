from openpyxl import load_workbook
wb = load_workbook(filename='try.xlsx')
sheet_ranges = wb['Sheet1']

print(sheet_ranges.merged_cells.ranges)

