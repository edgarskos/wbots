import urllib.request
from html2text import html2text
import re

def getversion(url, article):

	#init result

	result = 'None'

	#fix invalid url
	if 'http://' not in url and 'https://' not in url:
		url = 'http://'+url

	print('checking newer version for', article)
	print('checking', url)
	#connect to website
	html = urllib.request.urlopen(url).read()
	#html to plain text
	plaintext = html2text(str(html).lower())

	try:
		result = re.search(article+'\s*([\d.]+)', plaintext).group(1)
	except AttributeError:
		pass

	if result == 'None':
		result = re.search(r'build\s*([\d.]+)', plaintext).group(1)
		result = 'Build '+result


	#last format
	strlen = len(result)

	if '.' in result[strlen-1]:
		result = result.replace(result[strlen-1], '')
		#update srtlen
		strlen = len(result)

	if ',' in result[strlen-1]:
		result = result.replace(result[strlen-1], '')
		strlen = len(result)

	#return version
	return result