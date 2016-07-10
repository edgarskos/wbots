from core.log import *
import re
from core.config import *

def brfix(article, text):
	if testmode == 1:
		printlog('testmode')
	errorcout = 0
	text = str(text)
	oldtext = text
	checktext = text
	saves = ''
	zeroedit = 0
	printlog('brfix testing site: '+ article)
	errorcout = text.count('< br >')+text.count('< br>')+text.count('<br >')+text.count('</br>')+text.count('< /br >')+text.count('< /br>')+text.count('</br >')+text.count('< br />')+text.count('< br/>')+text.count('<br/ >')+text.count('< br/ >')+text.count('<br clear="all">')+text.count('< br clear="all" >')+text.count('<br clear="all" >')+text.count('< br clear="all">')

	text = text.replace('< br >', '<br>').replace('< br>', '<br>').replace('<br >', '<br>')
	text = text.replace('</br>', '<br />').replace('< /br >', '<br />').replace('< /br>', '<br />').replace('</br >', '<br />')
	text = text.replace('< br/ >', '<br />').replace('< br/>', '<br />').replace('< br />', '<br />').replace('< br/ >', '<br />')
	text = text.replace('<br clear="all">', '{{clear}}').replace('< br clear="all" >', '{{clear}}').replace('< br clear="all">', '{{clear}}').replace('<br clear="all" >', '{{clear}}')

	if text != oldtext:
		zeroedit = 1
		if errorcout > 1 and lang == 'fi':
			saves = u"Botti korjasi br tagien syntaksit tai korvasi ne {{clear}} mallineella. "
		elif errorcout == 1 and lang == 'fi':
			saves = u"Botti korjasi br tagin syntaksin tai korvasi sen {{clear}} mallineella. "
		elif errorcout > 1 and lang == 'en':
			saves = u"Bot has fixed br tags syntaxes or did replace it with {{clear}}. "
		elif errorcout == 1 and lang == 'en':
			saves = u"Bot has fixed br tag syntax or did replace it with {{clear}}. "

	elif errorcout == 0:
		printlog('brfix no invalid links found: '+ article)
		oldtext = text

	return errorcout, text, saves, zeroedit