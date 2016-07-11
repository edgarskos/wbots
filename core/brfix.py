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
	errorcout += text.count('< br >')+text.count('< br>')+text.count('<br >')+text.count('</br>')+text.count('< /br >')+text.count('< /br>')+text.count('</br >')+text.count('< br />')+text.count('< br/>')+text.count('<br/ >')+text.count('< br/ >')
	errorcout += text.count('<br clear="all">')+text.count('< br clear="all" >')+text.count('<br clear="all" >')+text.count('< br clear="all">')+text.count('<br clear="all" />')+text.count('< br clear="all" />')+text.count('< br clear="all"/>')+text.count('<br clear="all"/>')
	errorcout += text.count('<br clear=all>')+text.count('< br clear=all >')+text.count('<br clear=all >')+text.count('< br clear=all>')+text.count('<br clear=all />')+text.count('< br clear=all />')+text.count('< br clear=all/>')+text.count('<br clear=all/>')
	errorcout += text.count('<br clear="left">')+text.count('< br clear="left" >')+text.count('<br clear="left" >')+text.count('< br clear="left">')+text.count('<br clear="left" />')+text.count('< br clear="left" />')+text.count('< br clear="left"/>')+text.count('<br clear="left"/>')
	errorcout += text.count('<br clear="right">')+text.count('< br clear="right" >')+text.count('<br clear="right" >')+text.count('< br clear="right">')+text.count('<br clear="right" />')+text.count('< br clear="right" />')+text.count('< br clear="right"/>')+text.count('<br clear="right"/>')
	errorcout += text.count('<br clear=left>')+text.count('< br clear=left >')+text.count('<br clear=left >')+text.count('< br clear=left>')+text.count('<br clear=left />')+text.count('< br clear=left />')+text.count('< br clear=left/>')+text.count('<br clear=left/>')
	errorcout += text.count('<br clear=right>')+text.count('< br clear=right >')+text.count('<br clear=right >')+text.count('< br clear=right>')+text.count('<br clear=right />')+text.count('< br clear=right />')+text.count('< br clear=right/>')+text.count('<br clear=right/>')

	text = text.replace('< br >', '<br>').replace('< br>', '<br>').replace('<br >', '<br>')
	text = text.replace('</br>', '<br />').replace('< /br >', '<br />').replace('< /br>', '<br />').replace('</br >', '<br />')
	text = text.replace('< br/ >', '<br />').replace('< br/>', '<br />').replace('< br />', '<br />').replace('< br/ >', '<br />')
	text = text.replace('<br clear="all">', '{{clear}}').replace('< br clear="all" >', '{{clear}}').replace('< br clear="all">', '{{clear}}').replace('<br clear="all" >', '{{clear}}')
	text = text.replace('<br clear="all" />', '{{clear}}').replace('<br clear="all"/>', '{{clear}}').replace('< br clear="all" />', '{{clear}}').replace('< br clear="all"/>', '{{clear}}')
	text = text.replace('<br clear="left">', '{{clear|left}}').replace('< br clear="left" >', '{{clear|left}}').replace('< br clear="left">', '{{clear|left}}').replace('<br clear="left" >', '{{clear|left}}')
	text = text.replace('<br clear="left" />', '{{clear|left}}').replace('<br clear="left"/>', '{{clear|left}}').replace('< br clear="left" />', '{{clear|left}}').replace('< br clear="left"/>', '{{clear|left}}')
	text = text.replace('<br clear="right">', '{{clear|right}}').replace('< br clear="right" >', '{{clear|right}}').replace('< br clear="right">', '{{clear|right}}').replace('<br clear="right" >', '{{clear|right}}')
	text = text.replace('<br clear="right" />', '{{clear|right}}').replace('<br clear="right"/>', '{{clear|right}}').replace('< br clear="right" />', '{{clear|right}}').replace('< br clear="right"/>', '{{clear|right}}')
	text = text.replace('<br clear=all>', '{{clear}}').replace('< br clear=all >', '{{clear}}').replace('< br clear=all>', '{{clear}}').replace('<br clear=all >', '{{clear}}')
	text = text.replace('<br clear=all />', '{{clear}}').replace('<br clear=all/>', '{{clear}}').replace('< br clear=all />', '{{clear}}').replace('< br clear=all/>', '{{clear}}')
	text = text.replace('<br clear=left>', '{{clear|left}}').replace('< br clear=left >', '{{clear|left}}').replace('< br clear=left>', '{{clear|left}}').replace('<br clear=left >', '{{clear|left}}')
	text = text.replace('<br clear=left />', '{{clear|left}}').replace('<br clear=left/>', '{{clear|left}}').replace('< br clear=left />', '{{clear|left}}').replace('< br clear=left/>', '{{clear|left}}')
	text = text.replace('<br clear=right>', '{{clear|right}}').replace('< br clear=right >', '{{clear|right}}').replace('< br clear=right>', '{{clear|right}}').replace('<br clear=right >', '{{clear|right}}')
	text = text.replace('<br clear=right />', '{{clear|right}}').replace('<br clear=right/>', '{{clear|right}}').replace('< br clear=right />', '{{clear|right}}').replace('< br clear=right/>', '{{clear|right}}')

	if text != oldtext:
		zeroedit = 1
		printlog('brfix invalid tags found: '+ article)
		if errorcout > 1 and lang == 'fi':
			saves = u"Botti korjasi br tagien syntaksit tai korvasi ne {{clear}} mallinnella. "
		elif errorcout == 1 and lang == 'fi':
			saves = u"Botti korjasi br tagin syntaksin tai korvasi sen {{clear}} mallinnella. "
		elif errorcout > 1 and lang == 'en':
			saves = u"Bot has fixed br tags syntaxes or did replace it with {{clear}}. "
		elif errorcout == 1 and lang == 'en':
			saves = u"Bot has fixed br tag syntax or did replace it with {{clear}}. "

	elif errorcout == 0:
		printlog('brfix invalid tags not found: '+ article)
		oldtext = text

	return errorcout, text, saves, zeroedit