from core.log import *
from core.config import *

def reftosrc(article, text):
	errorcout = 0
	text = str(text)
	oldtext = text
	checktext = text
	saves = ''
	zeroedit = 0
	
	
	textlist = text.split('\n')
	for l,i in enumerate(textlist):
		if i=='==Viitteet==':
			textlist[l]='==Lähteet=='

	text = '\n'.join(textlist)
	if text != oldtext:
		zeroedit = 1
		printlog('reftosrc error found: '+ article)
		saves = u"Botti muutti ==Vitteet== osion muotoon ==Lähteet==. "

	elif errorcout == 0:
		printlog('reftosrc error found: '+ article)
		oldtext = text

	return errorcout, text, saves, zeroedit