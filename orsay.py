import httplib2
from httplib2 import Http
from urllib import urlencode
from HTMLParser import HTMLParser
from urllib2 import urlopen

h = httplib2.Http(".cache")
resp, content = h.request("http://www.orsai.bitacoras.com/", "GET")


def fill_form():
	h = Http()
	data = dict(name="Joe", comment="A test comment")
	resp, content = h.request("http://bitworking.org/news/223/Meet-Ares", "POST", urlencode(data))
	print resp
	# {'status': '200', 'transfer-encoding': 'chunked', 'vary': 'Accept-Encoding,User-Agent',
	# 'server': 'Apache', 'connection': 'close', 'date': 'Tue, 31 Jul 2007 15:29:52 GMT', 
	# 'content-type': 'text/html'}
	
class Spider(HTMLParser):
	def __init__(self, url): 
		HTMLParser.__init__(self) 
		req = urlopen(url) 
        	self.atri = []
		self.feed(req.read()) 		      
	def handle_starttag(self, tag, attrs): 
		attrs = dict(attrs) 
		if tag == 'div' and  attrs[attrs.keys()[0]]  == 'texto_gran_titulo':
                        self.atri.append(attrs[attrs.keys()[0]])
		ifr tag=='a': 
			self.atri.append(attrs[attrs.keys()[0]])
		#if tag == 'a':
                #        self.atri.append(attrs[0][1])
		#	print "Found link => %s" % attrs
		#if tag=='a'
			
		#if tag == 'a' and attrs: 
		#	print "Found link => %s" % attrs

#	def handle_endtag(self, tag):
#                if tag == 'div':
#                        print "Found end => %s" % attrs
#			print "end"
	
a= Spider('http://www.orsai.bitacoras.com/')

print a.atri
