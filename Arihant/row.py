def rowhandling(List):
	typeDict = {"b":"button","c":"checkbox","col":"color","d":"date","e":"email","f":"file","h":"hidden","i":"image","m":"month","n":"number","p":"password","o":"radio","g":"range","r":"reset","srch":"search","s":"submit","tel":"tel","txt":"text","t":"time","u":"url","w":"week"}
#	List = []  # enteries are rows
	HTML = ""
	for i in List:
		k = i.split(":")
		if k[0] == "L":
			HTML += '<div class="col">\n'
			HTML += '<label for="'
			HTML += str(k[1])
			HTML += '">'
			HTML += str(k[1])
			HTML += '</label>\n</div>'
			labeltext = str(k[1])
		elif k[0] == "I":
			HTML += '<div class="col">\n'
			HTML += '<input name="'
			HTML += str(k[2])
			HTML += '" id = "'
			HTML += str(k[2])
			HTML += '" type="'
			HTML += str(typeDict[k[1]])
			HTML += '">\n</div>'

	HTML += "</br>\n"
	return(HTML)
