import sys
if len(sys.argv)<4:
	print("Fatal: Not enough arguments.")
	if len(sys.argv)==1:
		print("Useage:\npython new.py <FILENAME> <TITLE> <AUTHOR> [-d DATE] [PACKAGES...]")
	sys.exit()
filename=sys.argv[1]
title=sys.argv[2]
author=sys.argv[3]
date=""
packages=[]
if len(sys.argv)>4:
	date=sys.argv[4]
if len(sys.argv)>5:
	for i in range(5,len(sys.argv)):
		packages.append(sys.argv[i])

with open(filename,"w+") as f:
	f.write("\\documentclass{article}\n")
	f.write("\\usepackage[utf8]{inputenc}\n")
	f.write("\\usepackage[english]{babel}\n")
	f.write("\\usepackage{fancyhdr}\n")
	for pack in packages:
		f.write("\\usepackage{"+pack+"}\n")
	f.write("\\lhead{"+title+"}\n")
	f.write("\\rhead{\\thepage}\n")
	f.write("\\cfoot{"+author+"}\n")
	f.write("\\pagestyle{fancy}\n")
	f.write("\\title{"+title+"}\n")
	f.write("\\author{"+author+"}\n")
	f.write("\\date{"+date+"}\n")
	f.write("\\begin{document}\n\\maketitle\n\\end{document}\n")
