#!/usr/bin/python
# -*- coding: utf-8 -*-

#Burhan SAFRAN(Safran İnternet Teknolojileri)

import sys
import os

def info():
    print "-on\t\tFana güç verir.\n-off\t\tFanın gücünü keser."
dir = os.getcwd()
os.chdir('settings')

if len(sys.argv) == 1:
    info()
    sys.exit(0)
if sys.argv[1] == "-on":
    os.system("python on.py")
elif sys.argv[1] == "-off":
    os.system("python off.py")
else:
    print "Erör! Lütfen erörle mücadele hattını arayın!"
    info()