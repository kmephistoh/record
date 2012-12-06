#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print "今天一个简单的阶乘都写错了，罪过"
print sys.argv[1]+"的阶乘是：%d" % factorial(int(sys.argv[1])) 
