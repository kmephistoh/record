#!/usr/bin/env python2
# -*- coding:utf-8 -*-
# pythonchallenge 第二关的土鳖解法,改天去看看别人的解法
s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
def aplus2(a):
    new = []
    for x in a:
        if x.isalpha() and (x not in ["y","z"]):
           x=chr(ord(x)+2) 
           new.append(x)
        elif x == "y":
            x = "a"
            new.append(x)
        elif x == "z":
            x = "b"
            new.append(x)
        elif not x.isalpha():
            new.append(x)
    return "".join(new)

new_s =[aplus2(x) for x in s.split()]
print " ".join(new_s)

print "修改map为："+aplus2("map")+" 进入下一关"
