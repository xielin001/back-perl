#!/usr/bin/env python
# coding=utf-8
print("Content-type: text/html \n")

from os.path import abspath, join
import cgi,sys
#hashlib代替sha模块
from hashlib import sha1

BASE_DIR = abspath('data')

form = cgi.FieldStorage()

text = form.getvalue('text')
filename = form.getvalue('filename')
password = form.getvalue('password')

if not (text,filename,password):
    print("Invalid parameters.")
    sys.exit()
if sha1(password).hexdigest() != '7c4a8d09ca3762af61e59520943dc26494f8941b':
    #密码123456
    print("Invalid password.")
    sys.exit()

f = open(join(BASE_DIR,filename),'w')
f.write(text)
f.close()