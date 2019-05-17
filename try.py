from openpyxl import load_workbook
from openpyxl.utils.cell import coordinate_from_string, column_index_from_string
wb = load_workbook(filename='try.xlsx')
sheet_ranges = wb['Sheet1']
sheet_range = str(sheet_ranges.merged_cells.ranges)
sheet_range = sheet_range[1:len(sheet_range)-1]
sheet_range = sheet_range.split(", ")
start_array = []
len_array = []
for i in sheet_range:
	i = i[11:len(i)-1]
	i = i.split(":")
	start_cell = i[0][0]
	end_cell = i[1][0]
	merged_length = ord(end_cell) - ord(start_cell)
	start_array.append(i[0])
	len_array.append(merged_length)
print(start_array)
print(len_array)
