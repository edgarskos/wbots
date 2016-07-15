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
	if '</ref>' in text and '{{viitteet}}' not in text and '<references/> ' not in text and '{{Viitteet}}' not in text:
		if '==Viitteet==' not in text and '==Lähteet==' not in text and '== Viitteet ==' not in text and '== Lähteet ==' not in text:
			textlen = len(text)
			usenextline = 0
			placingposition = 0
			for line in reversed(text.split('\n')):
				if '{{Tynkä' in line:
					usenextline = 1
				elif '[[Luokka:' in line:
					usenextline = 1
				elif line == '':
					continue
				elif usenextline == 1 and '*' in line[0:1]:
					placingposition = text.rfind(line)+len(line)
					break
				elif usenextline == 1 and '{{kesken}}' in line:
					placingposition = text.rfind(line)+len(line)
					break
				elif usenextline == 1 and '{{juonipaljastus loppu}}' in line:
					placingposition = text.rfind(line)+len(line)
					break
				elif usenextline == 1 and '{{Kesken}}' in line:
					placingposition = text.rfind(line)+len(line)
					break
				elif usenextline == 1 and '{{' in line[0:2]:
					continue
				elif usenextline == 1 and line == '':
					continue
				elif usenextline == 1:
					placingposition = text.rfind(line)+len(line)
					break

				else:
					placingposition = text.rfind(line)+len(line)
					break
			if placingposition != 0:
				text_data = list(text)
				text_data.insert(placingposition, '\n\n==Viitteet==\n{{viitteet}}\n')
				text = ''.join(text_data)
				errorcout += 1
				error = 1
		else:
			addreferences = 0
			endposition = 0
			foundlist = 0
			foundpos = 0
			for line in reversed(text.split('\n')):
				if '==Viitteet==' in line or '==Lähteet==' in line or '== Viitteet ==' in line or '===Viitteet===' in line or '=== Viitteet ===' in line or '== Lähteet ==' in line:
					startposition = text.rfind(line)
					if line == '==Viitteet==':
						endposition = startposition + 12
						break
					elif line == '== Viitteet ==':
						endposition = startposition + 14
						break
					elif line == '===Viitteet===':
						endposition = startposition + 14
						break
					elif line == '=== Viitteet ===':
						endposition = startposition + 16
						break
					elif line == '==Lähteet==':
						addreferences = 1
						endposition = startposition + 11
						break
					elif line == '== Lähteet ==':
						addreferences = 1
						endposition = startposition + 13
						break
			if endposition != 0:
				if '*' in text[endposition:endposition+3] or '{{Commons' in text[endposition:endposition+11]:
					lastposition = 0
					lastlen = 0
					for line in text[endposition:].split('\n'):
						if '*' in line or '{{Commons' in line:
							foundlist = 1
							lastposition = text[endposition:].find(line)
							lastlen = len(line)
						if '*' not in line and lastlen != 0 and lastposition != 0:
							if addreferences == 1 and foundlist == 1:
								endposition = endposition + lastposition + lastlen
								text_data = list(text)
								text_data.insert(endposition, '\n\n===Viitteet===\n{{viitteet}}\n')
								text = ''.join(text_data)
								errorcout += 1
								error = 1
								break

							else:
								endposition = endposition + lastposition + lastlen
								text_data = list(text)
								text_data.insert(endposition, '\n{{viitteet}}')
								text = ''.join(text_data)
								errorcout += 1
								error = 2
								break

				else:
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