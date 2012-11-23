#usr/bin/env python
#-*- coding:utf-8 -*-
import time
import os
from time import strftime
Month = strftime('%Y-%m')
Date = strftime('%Y-%m-%d')
Time = strftime('%H:%M:%S')
#top_dir = "D:work_log/"
dst_dir = Month   #if cwd is not top_dir: dst_dir = top_dir + month
logfile = Date + '.txt'
if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)
os.chdir(dst_dir)
if not os.path.isfile(logfile):    
    f = open(logfile,'a')
    f.write('==========  Created by kevin at ' + Time +'  =========='+'\n')
    f.close()
