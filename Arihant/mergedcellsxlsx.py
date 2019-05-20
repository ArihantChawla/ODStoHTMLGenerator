def ExtractMergedCellInfo(file):
	from openpyxl import load_workbook
	from openpyxl.utils.cell import coordinate_from_string, column_index_from_string
	wb = load_workbook(filename=str(file))
	sheet_ranges = wb['Sheet1']
	sheet_range = str(sheet_ranges.merged_cells.ranges)
	sheet_range = sheet_range[1:len(sheet_range)-1]
	sheet_range = sheet_range.split(", ")
	merged_array = []  # contains pairs of start of horizontal merge and length respectively
	for i in sheet_range:
		i = i[11:len(i)-1]
		i = i.split(":")
		start_cell = coordinate_from_string(i[0])
		end_cell = coordinate_from_string(i[1])
		if end_cell[1] != start_cell[1]:
			print("MULTI ROW MERGING NOT ALLOWED")
			exit(1)
		merged_length = ord(end_cell[0]) - ord(start_cell[0])
		merged_array.append([i[0],merged_length])
	return(merged_array)
