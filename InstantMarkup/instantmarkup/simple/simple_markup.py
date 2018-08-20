import re,sys
from util import *

print('<html><head><title>...</title><body>')

title = True
for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)
    if title:
        print "<h1>"
        print block
        print "</h1>"
        title = False
    else:
        print "<p>"
        print block
        print "</p>"
print "</body></html>"

'''
C:\Python27>
python.exe E:\pycharm\python_foundation\InstantMarkup\instantmakup\simple\simple_makup.py E:\pycharm\python_foundation\InstantMarkup\instantmakup\simple\\book.txt E:\pycharm\python_foundation\InstantMarkup\instantmakup\simple\\book.html
'''