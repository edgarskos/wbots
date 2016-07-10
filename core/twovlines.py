from core.log import *
import re
from core.config import *

def twovlines(article, text):
	if testmode == 1:
		printlog('testmode')
	errorcout = 0
	text = str(text)
	oldtext = text
	saves = ''
	zeroedit = 0
	printlog('2vline testing site: '+ article)
	brackets = re.findall(r"\[(.*?)\]", text)
	for item in brackets:
		if '||' in item:
			errorcout += 1
			olditem = '['+item+']]'
			item = '['+item+']]'
			item = item.replace('||', '|')
			printlog(olditem+' --> '+ item)
			text = text.replace(olditem, item)


	if text != oldtext:
		zeroedit = 1
		if errorcout > 1 and lang == 'fi':
			saves = u"Botti poisti ylimääräiset pystyviivat linkeistä. "
		elif errorcout == 1 and lang == 'fi':
			saves = u"Botti poisti ylimääräisen pystyviivan linkistä. "
		elif errorcout > 1 and lang == 'en':
			saves = u"Bot has removed excessive vertical line from link. "
		elif errorcout == 1 and lang == 'en':
			saves = u"Bot has removed excessive vertical lines from links. "

	elif errorcout == 0:
		printlog('fix2brackets no invalid links found: '+ article)
		oldtext = text

	return errorcout, text, saves, zeroedit