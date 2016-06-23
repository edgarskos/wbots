import sys
import re
from core.config import *
from core.log import *


def fixpiped(article ,text):
	if testmode == 1:
		printlog('testmode')
	fixeditem = None
	errorcout = 0
	saves = ''
	zeroedit = 0
	text = str(text)
	oldtext = text
	printlog('fixpiped testing site: '+ article)
	searchtext = text.replace(' ', '_')
	twobrackets = re.findall(r"\[(\S+?)\]", searchtext )

	for item in twobrackets:
		fixeditem = None
		originalitem = item
		if '|' in item:
			item = item.replace('[', '').replace(']', '')
			item = item.split('|')

			if item[0] == item[1]:
				fixeditem = '['+str(item[0])+''
				fixeditem = fixeditem.replace('_', ' ')
			if fixeditem != None:
				errorcout += 1
				originalitem = originalitem.replace('_', ' ')
				print(fixeditem)
				printlog(originalitem+'] --> '+fixeditem+']')
				text = text.replace(str(originalitem), str(fixeditem))
	if text != oldtext:
		if errorcout > 1 and lang == 'fi':
			saves = u'Botti poisti wikipedian sisäisistä linkeistä tekstin joissa se on sama kuin linkki. '
		elif errorcout == 1 and lang == 'fi':
			saves = u'Botti poisti wikipedian sisäisestä linkistä tekstin jossa se on sama kuin linkki. '
		elif errorcout > 1 and lang == 'en':
			saves = u"Bot has removed texts from pipedlinks because it's same as link. "
		elif errorcout == 1 and lang == 'en':
			saves = u"Bot has removed text from pipedlink because it's same as link. "

	elif errorcout == 0:
		printlog('fixpiped no invalid links found: '+ article)
		oldtext = text

	return errorcout, text, saves, zeroedit