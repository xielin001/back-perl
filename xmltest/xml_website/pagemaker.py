# coding:utf-8
# ！/usr/local/bin/python
from xml.sax.handler import ContentHandler
from xml.sax import parse


# class TestHandler(ContentHandler):
#     def startElement(self, name, attrs):
#         print(name, attrs.keys())
# parse('website.xml', TestHandler())

class PageMaker(ContentHandler):
    passthrough = False

    def startElement(self, name, attrs):
        if name == 'page':
            self.passthrough = True
            self.out = open(attrs['name'] + '.html', 'w')
            self.out.write('<html><head>\n')
            self.out.write('<title>%s</title>\n' % attrs['title'])
            self.out.write('</head><body>\n')
        elif self.passthrough:
            self.out.write('<' + name)
            for key, value in attrs.items():
                self.out.write(' %s=%s' % (key, value))
            self.out.write('>')

    def endElement(self, name):
        if name == 'page':
            self.passthrough = False
            self.out.write('\n</body></html>\n')
            self.out.close()
        elif self.passthrough:
            self.out.write('</%s>' % name)

    def characters(self, content):
        if self.passthrough: self.out.write(content)


parse('website.xml', PageMaker())
