
import urllib2
import sys
content=urllib2.urlopen('http://www.baidu.com').read()
typeEncode = sys.getfilesystemencoding()
html = content.decode('utf-8').encode(typeEncode)
print html