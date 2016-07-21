from core.log import *
from core.config import *

def reftosrc(article, text):
	errorcount = 0
	text = str(text)
	oldtext = text
	saves = ''
	zeroedit = 0
	error = 0
	
	
	textlist = text.split('\n')
	if '==Lähteet==' in text or '== Lähteet ==' in text or '== Lähteet==' in text or '==Lähteet ==' in text:
		for l,i in enumerate(textlist):
			if i=='==Viitteet==' or i=='== Viitteet ==' or i=='== Viitteet==' or i=='==Viitteet ==':
				textlist[l]='===Viitteet==='
				error = 1
	else:
		for l,i in enumerate(textlist):
			if i=='==Viitteet==' or i=='== Viitteet ==' or i=='== Viitteet==' or i=='==Viitteet ==':
				textlist[l]='==Lähteet=='
				error = 2

	text = '\n'.join(textlist)
	if text != oldtext:
		zeroedit = 1
		errorcount += 1
		printlog('reftosrc error found: '+ article)
		if error == 1:
			saves = u"Botti siirsi Viitteet osion oikealle tasolle. "
		elif error == 2:
			saves = u"Botti muutti ==Vitteet== osion muotoon ==Lähteet==. "


	elif errorcount == 0:
		printlog('reftosrc error not found: '+ article)

	return errorcount, text, saves, zeroedit