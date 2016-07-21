from core.log import *
import re
from core.config import *
from topy import topy
import sys

def typofix(article, text):

	errorcount = 0
	text = str(text)
	oldtext = text
	checktext = text
	saves = ''
	zeroedit = 0

	if typofix == 1 and text != '':
		text = topy.fixtypo(text)
	
	if text != oldtext:
		errorcount += 1
		zeroedit = 1
		printlog('typofix error found: '+ article)
		if errorcount == 1 and lang == 'fi':
			saves = u"Botti korjasi typon. "
		elif errorcount == 1 and lang == 'en':
			saves = u"Bot has fixed typo. "

	elif errorcount == 0:
		printlog('typofix error not found: '+ article)

	return errorcount, text, saves, zeroedit