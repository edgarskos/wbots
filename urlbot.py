#! /usr/bin/env python3

#import built in modules
import sys
#path append
sys.path.append('core/libs/')
import pywikibot
from pywikibot import pagegenerators
from core.fixreflinks import fixreflink
from core.fix2brackets import fix2brackets
from core.fixpiped import fixpiped
from core.log import *
from core.config import *
from core.fixblinks import fixblink
try:
	def main():
		fixcout = 0
		zeroedit = 1
		articles = open('core/db/articles.db', 'r')
		for article in articles:
			saves = ''
			site = pywikibot.Site()
			page = pywikibot.Page(site, article)
			text = str(page.text)
			oldtext = text
			infoback = fix2brackets(article, text)
			text = infoback[1]
			fixcout += infoback[0]
			saves += infoback[2]
			zeroedit -= infoback[3]
			infoback = fixpiped(article, text)
			text = infoback[1]
			fixcout += infoback[0]
			saves += infoback[2]
			zeroedit -= infoback[3]
			infoback = fixreflink(article, text)
			text = infoback[1]
			fixcout += infoback[0]
			saves += infoback[2]
			zeroedit -= infoback[3]
			infoback = fixblink(article, text)
			text = infoback[1]
			fixcout += infoback[0]
			saves += infoback[2]
			zeroedit -= infoback[3]
			
			if testmode == 1:
				printlog(saves)
				if fixcout > 0:
					log('found something')

			if text != oldtext and zeroedit < 1 and testmode == 0:
				page.text = text
				page.save(saves)
				printlog(saves)
			if text != oldtext and zeroedit == 1:
				printlog("bot didn't make changes to "+article+ " because zeroedit")
		printlog('fixcout: '+str(fixcout))

	if __name__ == '__main__':
		main()
except KeyboardInterrupt:
	printlog('bot terminated')