from core.log import *
import re
from core.config import *

def fixreflist(article, text):
	errorcout = 0
	text = str(text)
	oldtext = text
	checktext = text
	saves = ''
	zeroedit = 0
	if '</ref>' in text and '{{viitteet}}' not in text and '<references/> ' not in text:
		if '==Viitteet==' not in text and '==Lähteet==' not in text and '== Viitteet ==' not in text and '== Lähteet ==' not in text:
			textlen = len(text)
			usenextline = 0
			placingposition = 0
			for line in reversed(text.split('\n')):
				if '{{Tynkä' in line:
					print('tynkä')
					usenextline = 1
				elif '[[Luokka:' in line:
					print('luokka')
					usenextline = 1
				elif usenextline == 1 and '*' in line[0:1]:
					print('*')
					placingposition = text.rfind(line)+len(line)
					break
				elif usenextline == 1 and '{{' in line[0:2]:
					print('{{')
					continue
				elif usenextline == 1 and line == '':
					print('linebreak')
					continue 
				elif usenextline == 1:
					print('useline')
					placingposition = text.rfind(line)+len(line)
					break

				else:
					print('else')
					placingposition = text.rfind(line)+len(line)
					break
			if placingposition != 0:
				text_data = list(text)
				text_data.insert(placingposition, '\n\n==Viitteet==\n{{viitteet}}\n')
				text = ''.join(text_data)
				errorcout += 1
				error = 1
		else:
			for line in text.split('\n'):
				if '==Viitteet==' in line or '==Lähteet==' in line or '== Viitteet ==' in line or '== Lähteet ==' in line:
					startposition = text.rfind(line)
					if line == '==Viitteet==':
						endposition = startposition + 12
					elif line == '==Lähteet==':
						endposition = startposition + 11
					elif line == '== Viitteet ==':
						endposition = startposition + 14
					elif line == '== Lähteet ==':
						endposition = startposition + 13
					text_data = list(text)
					text_data.insert(endposition, '\n{{viitteet}}')
					text = ''.join(text_data)
					errorcout += 1
					error = 2


	if text != oldtext:
		zeroedit = 1
		printlog('fixreflist invalid ref list found: '+ article)
		if errorcout == 1 and lang == 'fi' and error == 1:
			saves = u"Botti lisäsi puuttuvan viitteet osion. "
		elif errorcout == 1 and lang == 'fi' and error == 2:
			saves = u"Botti lisäsi puuttuvan viitteet mallinen. "
		elif errorcout == 1 and lang == 'en' and error == 2:
			saves = u"Bot has added missing references template. "
		elif errorcout == 1 and lang == 'en' and error == 1:
			saves = u"Bot has added missing references section. "


	elif errorcout == 0:
		printlog('fixreflist invalid ref list not found: '+ article)
		oldtext = text

	return errorcout, text, saves, zeroedit