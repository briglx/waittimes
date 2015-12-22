
import urllib
import datetime

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import re

class Station():
	def __init__(self, name):
		self.name = name
		self.address = ""
		self.waitTime = 0;
	def name(self):
		return self.name
	def address(self):
		return self.address
	def waitTime(self):
		return self.waitTime

class MyHTMLParser(HTMLParser):
	def __init__(self):
	
		now = datetime.datetime.now()
		
		HTMLParser.__init__(self)
		self.titlebar = "Date            \t"
		self.timebar = now.strftime("%Y-%m-%d %H:%M") + '\t'
		
	
	def handle_data(self, data):
		#print data
		
		match = re.search(r'((M|P)\d\d)', data)
			
		if match:   
			
			self.titlebar = self.titlebar + match.group(1) + "\t"
		
		match = re.search(r'Wait Time: ((\d\d) min|--)', data)
			
		if match:   
			
			if match.group(2) is not None:
				
				self.timebar = self.timebar + match.group(2) + "\t"
			else:
				
				self.timebar = self.timebar + "--\t"
				
			
	def getTitle(self):
	
		print self.titlebar
		
		
	def getData(self):
	
		
		print self.timebar

		
		
	
	

parser = MyHTMLParser()

# Get a file-like object for the Python Web site's home page.
f = urllib.urlopen("http://65.82.88.75/queuecam/stationview.exe")
# Read from the object, storing the page's contents in 's'.
s = f.read()


parser.feed(s)
parser.getData()





f.close()


