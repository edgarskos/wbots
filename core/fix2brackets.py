from core.log import *
import re
from core.config import *

def fix2brackets(article, text):
	errorcount = 0
	text = str(text)
	oldtext = text
	saves = ''
	zeroedit = 0
	twobrackets = re.findall(r"\[(.*?)\]", text)
	for item in twobrackets:
		location = text.index(item)
		if '[' in item[0:2]:
			if 'https://' in item[0:10] or 'http://' in item[0:10]:
				if 'Tiedosto:' not in item and 'Kuva:' not in item and 'File:' not in item and 'Image:' not in item:
					errorcount += 1
					location = text.index(item)+len(item)
					if ']' in text[location+1:location+2]:

						olditem = '['+str(item)+']]'
						item = item.replace('[', '')
						item = '['+item+']'
						log('fix2brackets: '+article+'\n'+olditem+' --> '+item)
						text = text.replace(olditem, str(item))
					else:
						olditem = '['+str(item)+']'
						item = item.replace('[', '')
						item = '['+item+']'
						log('fix2brackets: '+article+'\n'+olditem+' --> '+item)
						text = text.replace(olditem, str(item))

	if text != oldtext:
		zeroedit = 1
		printlog('fix2brackets error found: '+ article)
		if errorcount > 1 and lang == 'fi':
			saves = u"Botti poisti ylimääräiset hakasulkeet ulkoisista linkeistä. "
		elif errorcount == 1 and lang == 'fi':
			saves = u"Botti poisti ylimääräiset hakasulkeet ulkoisesta linkistä. "
		elif errorcount > 1 and lang == 'en':
			saves = u"Bot has removed excessive brackets from external links. "
		elif errorcount == 1 and lang == 'en':
			saves = u"Bot has removed excessive brackets from external link. "

	elif errorcount == 0:
		printlog('fix2brackets error not found: '+ article)

	return errorcount, text, saves, zeroedit