#!/usr/bin/env python2
#-*- coding:utf-8 -*-
import sys
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print "真真真真真真真真真真�"
print sys.argv[1]+"真真� %d" % factorial(int(sys.argv[1])) 
