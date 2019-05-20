from openpyxl import load_workbook

def filter_mergecells((event, element)):
	return element.tag == '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}mergeCell'

def read_mergecells(ws, xml_source):
	source = _get_xml_iter(xml_source)
	ws.mergeCells = []
	it = iterparse(source)
	for event, element in ifilter(filter_mergecells, it):
		ref = element.get('ref')
		ws.mergeCells.append(ws.range(ref))
        # to avoid memory exhaustion, clear the item after use
		element.clear()
	return

def read_worksheet(xml_source, parent, preset_title, string_table,style_table, workbook_name = None, sheet_codename = None):
"""Read an xml worksheet"""
	if workbook_name and sheet_codename:
		ws = IterableWorksheet(parent, preset_title, workbook_name,sheet_codename, xml_source)
	else:
		ws = Worksheet(parent, preset_title)
		fast_parse(ws, xml_source, string_table, style_table)
	read_mergecells(ws, xml_source)
	return ws
