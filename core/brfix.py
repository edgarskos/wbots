from core.log import *
import re
from core.config import *

def brfix(article, text):
	errorcout = 0
	text = str(text)
	oldtext = text
	checktext = text
	saves = ''
	zeroedit = 0
	
	errorlist = re.findall(r"\<.*?\>", text)

	for item in errorlist:
		if 'br' in item and 'abbr' not in item and 'wbr' not in item and 'ref' not in item:
			if 'clear' in item and '=' in item:
				if 'all' in item:
					text = text.replace(item, '{{clear}}')
					errorcout += 1
				elif 'left' in item:
					text = text.replace(item, '{{clear|left}}')
					errorcout += 1
				elif 'right' in item:
					text = text.replace(item, '{{clear|right}}')
					errorcout += 1
			elif '/' in item and item != '<br />' and 'clear' not in item and '=' not in item:
				text = text.replace(item, '<br />')
				errorcout += 1
			elif '/' not in item and item != '<br>' and 'clear' not in item and '=' not in item:
				text = text.replace(item, '<br>')
				errorcout += 1

	if text != oldtext:
		zeroedit = 1
		printlog('brfix error found: '+ article)
		if errorcout > 1 and lang == 'fi':
			saves = u"Botti korjasi br tagien syntaksit tai korvasi ne {{clear}} mallinnella. "
		elif errorcout == 1 and lang == 'fi':
			saves = u"Botti korjasi br tagin syntaksin tai korvasi sen {{clear}} mallinnella. "
		elif errorcout > 1 and lang == 'en':
			saves = u"Bot has fixed br tags syntaxes or did replace it with {{clear}}. "
		elif errorcout == 1 and lang == 'en':
			saves = u"Bot has fixed br tag syntax or did replace it with {{clear}}. "

	elif errorcout == 0:
		printlog('brfix error found: '+ article)
		oldtext = text

	return errorcout, text, saves, zeroedit