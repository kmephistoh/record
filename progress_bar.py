#/usr/bin/env python2
# -*- coding:utf-8 -*-
import sys,time
for i in range(0,101,10):
    sys.stdout.write("#"*int(round(i/10))+"_"*int(round(10-i/10))+" "+str(i)+"%"+"\r")    
    sys.stdout.flush()
    time.sleep(0.5)
time.sleep(5)
