#!/usr/bin/env python2
# -*- coding:utf-8 -*- 
import gtk.gdk
import pynotify

Title = "blabla"
Msg = u"走你"
Icon = "path to the image"

pynotify.init("test")
n = pynotify.Notification(Title,Msg,Icon)
n.set_hint('x',gtk.gdk.screen_width()/2.)
n.set_hint('y',gtk.gdk.screen_height()/2.)
n.show()
