# -*- coding: utf-8 -*-
__author__ = "ChenTong"

import urllib2, re, os

URL = "https://community.topcoder.com/stat?c=problem_solution&cr=23164059&rd=15837&pm=12953"
COOKIE = "km_ai=yv2GYOrwD6owZv4bYiHnafcD9qU%3D; knu=true; km_lv=x; tcsso=40490194|efeaa4cd85ec73f347547b620d0a5e78ca63ef0a9c747e87cfcabb9889c5a7c; _ga=GA1.2.190879198.1489496490; JSESSIONID=mdvXg2gQWcbFZMFkb8qPqw**.tomcat_tc01; AWSELB=D56385311A90FE1A806D3F0FB88957F720A3099EF2CCC09CFBB6117CFEDF1111DDD93A1B9947FC865EAD3C6A53163D494AF053690C3C4E91457A3782C41839505DF24D9B16; __utmt=1; kvcd=1489538920029; km_vs=1; __utma=192638645.190879198.1489496490.1489535377.1489538846.3; __utmb=192638645.7.10.1489538846; __utmc=192638645; __utmz=192638645.1489538846.3.2.utmcsr=sy.hhwdd.com|utmccn=(referral)|utmcmd=referral|utmcct=/new/problem/ViewOLProblem.page"
NAME = "FoxAndWord"

def procInput(s):
	s = s.replace('{', '[').replace('}', ']')
	val = eval("[" + s + "]")

	ret = ""

	# Case: two integer
	# ret += str(val[0]) + " " + str(val[1]) + "\n"

	# Case: two arrays and a string
	# ret += str(len(val[0]) + 1) + ' ' + str(val[2]) + "\n"
	# for i in range(0, len(val[0])):
	# 	ret += str(val[0][i]) + ' ' + str(val[1][i]) + "\n"

	# Case: several arrays
	# ret += str(len(val[0])) + "\n"
	# for i in range(0, len(val[0])):
	# 	for j in range(0, 4):
	# 		ret += str(val[j][i]) + " "
	# 	ret += "\n"

	# Case: several strings need to be concatenated
	# for i in val[0]:
	# 	ret += str(i)
	# ret += "\n"

	# Case: an array
	ret += str(len(val[0])) + "\n";
	for i in val[0]:
		ret += str(i) + "\n"

	return ret

def procOutput(s):
	val = eval(s)
	
	ret = ""
	ret += str(val)

	return ret

def main():
	data = {}
	headers = {"cookie" : COOKIE}

	request = urllib2.Request(URL, data, headers)
	response = urllib2.urlopen(request)
	page = response.read()

	pattern = re.compile(r'<TD ?(?:BACKGROUND="/i/steel_blue_bg.gif")? CLASS="statText" ALIGN="(?:left|right)">([\s\S]*?)</TD>')
	result = re.findall(pattern, page)


	if not os.path.exists(NAME + "/"):
		os.mkdir(NAME + "/");
	for (ind, val) in enumerate(result):
		if ind % 3 == 0:
			infile = open(NAME + "/" + NAME + str(ind / 3 + 1) + ".in", "w")
			infile.write(procInput(val))
		elif ind % 3 == 1:
			outfile = open(NAME + "/" + NAME + str(ind / 3 + 1) + ".out", "w")
			outfile.write(procOutput(val))


if __name__ == '__main__':
	main()
