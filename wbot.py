#! /usr/bin/env python3

try:
	#import built in modules
	import sys
	from glob import glob
	import datetime
	#path append
	sys.path.append('core/libs/')
	#import core and libs
	import pywikibot
	from pywikibot import pagegenerators
	from core.fixreflinks import fixreflink
	from core.fix2brackets import fix2brackets
	from core.fixpiped import fixpiped
	from core.log import *
	from core.config import *
	from core.fixblinks import fixblink
	from core.twovlines import twovlines
	from core.brfix import brfix
	from core.centerfix import centerfix
	from core.smallfix import smallfix
	from core.typofix import typofix
	from core.fixreflist import fixreflist

	def main():
		methods = ['fix2brackets', 'fixpiped', 'fixreflink', 'fixblink', 'twovlines', 'brfix', 'centerfix', 'smallfix', 'typofix', 'fixreflist']
		start_time = datetime.datetime.now()
		fixcout = 0
		zeroedit = 1
		if testmode == 0:
			print('test mode disabled\n')
		else:
			print('test mode enabled\n')
		filename = input('list for bots file name: ')
		filenamef = 'core/lfb/'+filename+'.lfb'
		#list of articles
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
		#check article
		for article in articles:
			saves = ''
			site = pywikibot.Site()
			page = pywikibot.Page(site, article)
			try:
				text = str(page.text)
			except pywikibot.exceptions.InvalidTitle:
				continue
			if text == '':
				printlog("this page is empty or it doesn't exist")
				continue
			oldtext = text

			for method in methods:
				func = globals()[method]
				infoback = func(article, text)
				text = infoback[1]
				fixcout += infoback[0]
				saves += infoback[2]
				zeroedit -= infoback[3]
			
			if testmode == 1:
				if saves != '':
					printlog(saves)
				if fixcout > 0:
					log('found something')
			
			#write changes
			if text != oldtext and zeroedit < 1 and testmode == 0:
				page.text = text
				page.save(saves)
				printlog(saves)
			if text != oldtext and zeroedit == 1:
				printlog("bot didn't make changes to "+article+ " because zeroedit")
		printlog('fixcout: '+str(fixcout))
		stop_time = datetime.datetime.now()
		total_time = stop_time - start_time
		printlog("bot duration: "+str(total_time))

	if __name__ == '__main__':
		main()
except KeyboardInterrupt:
	printlog('bot terminated')
