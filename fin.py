from pyexcel_xls import get_data
from collections import OrderedDict
data = OrderedDict()
data = OrderedDict(get_data("try.xlsx"))
data = data['Sheet1']
count=0
for i in data:
	i = str(i)
	i = i[1:len(i)-1]
	i = i.split(", ")
	print(i)
	for j in range(0,5): 		# replace 5 with 12 for final
		count = 0 		# count for the number of cols to give
		for k in range(j,5):
			i

