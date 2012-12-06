#!/usr/bin/env python2
#-*- coding:utf-8 -*-
import sys
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print "¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿"
print sys.argv[1]+"¿¿¿¿¿ %d" % factorial(int(sys.argv[1])) 
