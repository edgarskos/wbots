from core.log import *
import re
from core.config import *
from topy import topy
import sys

def typofix(article, text):
	errorcout = 0
	text = str(text)
	oldtext = text
	checktext = text
	saves = ''
	zeroedit = 0

	if text != '':
		text = topy.fixtypo(text)
	
	if text != oldtext:
		errorcout += 1
		zeroedit = 1
		printlog('typofix typos found: '+ article)
		if errorcout == 1 and lang == 'fi':
			saves = u"Botti korjasi typon. "
		elif errorcout == 1 and lang == 'en':
			saves = u"Bot has fixed typo. "

	elif errorcout == 0:
		printlog('typofix typos not found: '+ article)
		oldtext = text

	return errorcout, text, saves, zeroedit