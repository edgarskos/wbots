#! /usr/bin/env python3
import urllib.request
from urllib.parse import quote

def IsInt(value):
	try: 
		int(value)
		return True
	except ValueError:
		return False
try:
	def main():
		filename = input('list for bots file name: ')
		filenamef = 'core/lfb/'+filename+'.lfb'
		try:
			articles = open(filenamef, 'r')
		except FileNotFoundError:
			print('error: file not found')
			listfiles = glob('core/lfb/*.lfb')
			print('\navailable lists:\n')
			for item in listfiles:
				print(item.replace('core/lfb/', '').replace('.lfb', ''))
			print()
			main()
		listid = input('enter list id: ')
		if IsInt(listid) == False:
			print('error: id must be integer')

		for article in articles:
			article = article.replace('\n', '')
			print('sending request')
			url = 'https://tools.wmflabs.org/checkwiki/cgi-bin/checkwiki.cgi?project=fiwiki&view=only&id='+listid+'&title='+quote(article)+'&offset=0&limit=100'
			page = urllib.request.urlopen(url)

			print(article.replace('%20', ' ')+' has marked as done')

		print('done')
except KeyboardInterrupt:
	print('terminated')


if __name__ == '__main__':
	main()