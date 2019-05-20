def rowhandling(List, mergedcell, noofcellsmerged):
	typeDict = {"b":"button","c":"checkbox","col":"color","d":"date","e":"email","f":"file","h":"hidden","i":"image","m":"month","n":"number","p":"password","o":"radio","g":"range","r":"reset","srch":"search","s":"submit","tel":"tel","txt":"text","t":"time","u":"url","w":"week"}
	HTML = ""
	if mergedcell == -1 or noofcellsmerged == 0:
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
			else:
				HTML += '<div class="col"></div>'
		HTML += "</br>\n"
		return(HTML)
	else:
		for i in range(len(List)):
			if i == mergedcell:
				k = List[i]
				k = k.split(":")
				if k[0] == "L":
					HTML += '<div class="col-md-'
					HTML +=  str(noofcellsmerged+1)
					HTML += '">\n<label for="'
					HTML += str(k[1])
					HTML += '">'
					HTML += str(k[1])
					HTML += '</label>\n</div>'
					labeltext = str(k[1])
				elif k[0] == "I":
					HTML += '<div class="col-md-'
					HTML +=  str(noofcellsmerged+1)
					HTML += '">\n<input name="'
					HTML += str(k[2])
					HTML += '" id = "'
					HTML += str(k[2])
					HTML += '" type="'
					HTML += str(typeDict[k[1]])
					HTML += '">\n</div>'
				else:
					HTML += '<div class="col"></div>'
			elif (i > mergedcell) and (i <= (mergedcell + noofcellsmerged)):
				print("\n")
			else:
				k = List[i]
				k = k.split(":")
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
				else:
					HTML += '<div class="col"></div>'
		HTML += "</br>\n"
		return(HTML)
