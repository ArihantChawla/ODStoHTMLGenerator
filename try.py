from openpyxl import load_workbook
wb = load_workbook(filename='try.xlsx')
sheet_ranges = wb['Sheet1']
sheet_range = str(sheet_ranges.merged_cells.ranges)
sheet_range = sheet_range[1:len(sheet_range)-1]
sheet_range = sheet_range.split(", ")
for i in sheet_range:
	i = i[11:len(i)-1]
	i = i.split(":")
	start_cell = i[0][0]
	end_cell = i[1][0]
	merged = ord(end_cell) - ord(start_cell)
	print(merged)
