import sys
import urllib2
import urllib
from bs4 import BeautifulSoup
import re
import urlparse
import os

def main():
	response = urllib2.urlopen(sys.argv[1])
	html = response.read()
	dom = BeautifulSoup(html,"html.parser")
	
	tracks = dom.find_all(id=re.compile('tabs_'))
	for track in tracks:
		songID=track['song']
		songURL=urllib2.urlopen(urllib2.Request('http://www.sikhsangeet.com/ajax/download.php','id='+songID)).read()
		songURLDecoded=urllib2.unquote(songURL)
		songURLFinal = songURLDecoded.replace("+"," ")[::-1]
		print songURLFinal
		
		parsedURL = urlparse.urlparse(songURLFinal)
		folderPath = '/Users/gchandok/Music'+os.path.dirname(parsedURL.path)
		print folderPath
		if not os.path.exists(folderPath):
			os.makedirs(folderPath)

		filePath = os.path.join(folderPath,os.path.basename(parsedURL.path))
		print filePath
		result = urllib.urlretrieve(songURLFinal, filePath)

if __name__ == '__main__':
  main()


