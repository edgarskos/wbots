from core.log import *
import re
from core.config import *

def brfix(article, text):
	errorcount = 0
	text = str(text)
	oldtext = text
	checktext = text
	saves = ''
	zeroedit = 0
	
	errorlist = re.findall(r"\<.*?\>", text)

	for item in errorlist:
		if 'br' in item and 'abbr' not in item and 'wbr' not in item and 'ref' not in item and '<!--' not in item and '>' in item:
			if 'clear' in item and '=' in item:
				if 'all' in item:
					text = text.replace(item, '{{clear}}')
					errorcount += 1
				elif 'left' in item:
					text = text.replace(item, '{{clear|left}}')
					errorcount += 1
				elif 'right' in item:
					text = text.replace(item, '{{clear|right}}')
					errorcount += 1
			elif '/' in item and item != '<br />' and 'clear' not in item and '=' not in item:
				text = text.replace(item, '<br />')
				errorcount += 1
			elif '/' not in item and item != '<br>' and 'clear' not in item and '=' not in item:
				text = text.replace(item, '<br>')
				errorcount += 1

	if text != oldtext:
		zeroedit = 1
		printlog('brfix error found: '+ article)
		if errorcount > 1 and lang == 'fi':
			saves = u"Botti korjasi br tagien syntaksit tai korvasi ne {{clear}} mallinnella. "
		elif errorcount == 1 and lang == 'fi':
			saves = u"Botti korjasi br tagin syntaksin tai korvasi sen {{clear}} mallinnella. "
		elif errorcount > 1 and lang == 'en':
			saves = u"Bot has fixed br tags syntaxes or did replace it with {{clear}}. "
		elif errorcount == 1 and lang == 'en':
			saves = u"Bot has fixed br tag syntax or did replace it with {{clear}}. "

	elif errorcount == 0:
		printlog('brfix error found: '+ article)

	return errorcount, text, saves, zeroedit