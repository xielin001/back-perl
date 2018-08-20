# coding=utf-8
import cgi,sys
from os.path import join,abspath
BASE_DIR = abspath('data')
import os
path = os.

form = cgi.FieldStorage()
filename = form.getvalue('filename')
if not filename:
    print("please enter a filename")
    sys.exit()
text = open(join(BASE_DIR,filename)).read()
print("""
<html>
    <head>
        <title>Editing.....</title>
    </head>
    <body>
        <form action="save.cgi" method="post">
            <strong>File:</strong>%s<br />
            <input type="hidden" value="%s" name="filename" />
            <strong>Password:</strong><br />
            <input name="password" type="password" /><br />
            <strong>Text:</strong><br />
            <textarea name="text" cols="40" rows="20">%S</textarea ><br />
            <input type="submit" value="Save" />
        </form>
    </body>
</html>
"""%filename,filename,text)