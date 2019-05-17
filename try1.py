text1 = "L:First Name"
text2 = "I:txt:First Name"
text3 = "L:DOB"
text4 = "I:d:DOB"
typeDict = {"b":"button","c":"checkbox","col":"color","d":"date","e":"email","f":"file","h":"hidden","i":"image","m":"month","n":"number","p":"password","o":"radio","g":"range","r":"reset","srch":"search","s":"submit","tel":"tel","txt":"text","t":"time","u":"url","w":"week"}
List = []
List.append(text1)
List.append(text2)
List.append(text3)
List.append(text4)
HTML = "<form>"
for i in List:
	k = i.split(":")
	if k[0] == "L":
		HTML += '<label for="'
		HTML += str(k[1])
		HTML += '">'
		HTML += str(k[1])
		HTML += '</label></br>'
		labeltext = str(k[1])
	elif k[0] == "I":
		HTML += '<input name="'
		HTML += str(k[2])
		HTML += '" id = "'
		HTML += str(k[2])
		HTML += '" type="'
		HTML += str(typeDict[k[1]])
		HTML += '"></br>'

HTML += "</form>"
print(HTML)
