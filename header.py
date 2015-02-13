import os, sys, string
from os import listdir
from os.path import isfile, join

complexity_path = " ../sequence-complexity/usage/compute_complexity.go "

mypath = sys.argv[1]
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

for f in onlyfiles:	
	str = mypath + f
	#print(f)
	#raw_input()

	#cmd = "head -n 1 " + str
	#print genome name
	#os.system(cmd)

	cmd = "go run" + complexity_path + str
	#print genome name
	os.system(cmd)