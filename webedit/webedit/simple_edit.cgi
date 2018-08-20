#!coding=utf-8
import cgi
form = cgi.FieldStorage()

text = form.getvalue('text',open('simple_edit.dat').read())
f = open('simple_edit.dat','w')
f.write(text)
f.close()
print('''Content-type: text/xml

<html>
    <head>
        <title>A Simple Editor</title>   
    </head>
        <body>
            <form action='simple_edit.py' method='POST'>
            <textarea rows='10' cols='20' name='text'>%s</textarea><br />
            <input type='submit' />
            </form>
        </body>
</html>'''%text)