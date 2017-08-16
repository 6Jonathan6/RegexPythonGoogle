import re


def get_names(file_name):
	
	f = open(file_name,"r")
	
	code =  f.read()
	
	f.close()
	
	year = re.search("<h.*>(Popularity in )+((199[0-9]|200[0-9]))</h.*>",code).group(2)

	data = re.finditer(r"<tr.*><td>(\d\d*)+?</td><td>(\w+)</td><td>\b(\w+)\b</td>",code,flags=re.I)

	male_dic = {}

	female_dic = {}
	

	for d in data:
		
		male_dic[d.group(2)] = d.group(1)
		
		female_dic[d.group(3)] = d.group(1)
	

	male_list = [k + ": " + str(v) for k,v in male_dic.items()]
	
	male_list.sort()

	female_list  = [k + ": " + str(v) for k,v in female_dic.items()]
	
	female_list.sort()

	list = [ m + " " + female_list[i] for i , m in enumerate(male_list) ]

	list.insert(0,year)

	return list

def main (year):
	
	list = get_names(year)
	for l in list:
		print(l)


main("baby2006.html")




