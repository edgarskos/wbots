from core.log import *
from core.config import *

def categoryinen(article, text):
	if testmode == 1:
		printlog('testmode')
	errorcout = 0
	text = str(text)
	oldtext = text
	saves = ''
	zeroedit = 0
	printlog('categoryinen testing site: '+ article)
	