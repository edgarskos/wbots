from core.log import *
import re
from core.config import *

def twovlines(article, text):
	errorcout = 0
	text = str(text)
	oldtext = text
	saves = ''
	zeroedit = 0
	brackets = re.findall(r"\[(.*?)\]", text)
	for item in brackets:
		if '||' in item:
			errorcout += 1
			olditem = '['+item+']]'
			item = '['+item+']]'
			item = item.replace('||', '|')
			log('twovlines invalid link found: '+article+'\n'+olditem+' --> '+item)
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
		printlog('fix2brackets invalid links not found: '+ article)
		oldtext = text

	return errorcout, text, saves, zeroedit