import sys
import urllib2
import urllib
from bs4 import BeautifulSoup
import re
import urlparse
import os

def main():
	downloadSongsInFolder(sys.argv[1])

def downloadSongsInFolder(folder):
	print folder
	response = urllib2.urlopen(folder)
	html = response.read()
	dom = BeautifulSoup(html,"html.parser")
	
	links = dom.find_all('a')
	for link in links:
		linkURL = link.get('href')
		linkName = link.get_text()

		print linkName
		if linkName == " Parent Directory":
			continue

		if linkURL.find(".mp3") == -1:
			downloadSongsInFolder(folder + linkURL)
			continue
		
		songURLFinal = folder + linkURL 
		print songURLFinal
		
		parsedURL = urlparse.urlparse(songURLFinal)
		folderPath = '/Users/gchandok/Music'+os.path.dirname(parsedURL.path)
		folderPath = folderPath.replace("%20"," ")
		print folderPath

		if not os.path.exists(folderPath):
			os.makedirs(folderPath)

		filePath = os.path.join(folderPath,os.path.basename(parsedURL.path))
		filePath = filePath.replace("%20"," ")
		print filePath
		result = urllib.urlretrieve(songURLFinal, filePath)

if __name__ == '__main__':
  main()


