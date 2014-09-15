import sys
import os

#export K=31
#SOAPdenovo-63mer all -p 12 -s soap.config -o soap${K} -K $K 

k   = 31
cpu = 12
config = "soap.config"
cmd = "../SOAPdenovo-63mer all -p " + str(cpu) + " -s " + config + " -o soap" + str(k) + " -K " + str(k)
print cmd
os.system(cmd)