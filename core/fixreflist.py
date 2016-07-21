from core.log import *
import re
from core.config import *

def fixreflist(article, text):
	errorcount = 0
	text = str(text)
	oldtext = text
	checktext = text
	saves = ''
	zeroedit = 0

	donttouch = 0

	position2 = 0
	position3 = 0
	if '==Lähteet==' in text:
		position2 = text.find('==Lähteet==')
	if '== Lähteet==' in text:
		position2 = text.find('== Lähteet==')
	if '==Lähteet ==' in text:
		position2 = text.find('==Lähteet ==')
	if '== Lähteet ==' in text:
		position2 = text.find('== Lähteet ==')
	if '==Aiheesta muualla==' in text:
		position3 = text.find('==Aiheesta muualla==')
	if '== Aiheesta muualla==' in text:
		position3 = text.find('== Aiheesta muualla==') 
	if '==Aiheesta muualla ==' in text:
		position3 = text.find('==Aiheesta muualla ==') 
	if '== Aiheesta muualla ==' in text:
		position3 = text.find('== Aiheesta muualla ==')
	if '==Kirjallisuutta==' in text:
		position3 = text.find('==Kirjallisuutta==')
	if '== Kirjallisuutta==' in text:
		position3 = text.find('== Kirjallisuutta==')
	if '==Kirjallisuutta ==' in text:
		position3 = text.find('==Kirjallisuutta ==')
	if '== Kirjallisuutta ==' in text:
		position3 = text.find('== Kirjallisuutta ==')



	if '</ref>' in text and '{{viitteet' not in text and '<references/>' not in text and '{{Viitteet' not in text and '<references />' not in text:
		if  '==Lähteet==' not in text and '== Lähteet ==' not in text and '== Lähteet==' not in text and '==Lähteet ==' not in text:
			textlen = len(text)
			usenextline = 0
			placingposition = 0

			if '==Aiheesta muualla==' in text or '== Aiheesta muualla ==' in text or '== Aiheesta muualla==' in text or '==Aiheesta muualla ==' in text or '==Kirjallisuutta==' in text or '== Kirjallisuutta==' in text or '==Kirjallisuutta ==' in text or '== Kirjallisuutta ==' in text:
				position = 0
				if '==Aiheesta muualla==' in text:
					position = text.find('==Aiheesta muualla==')

				if '== Aiheesta muualla==' in text:
					position = text.find('== Aiheesta muualla==')

				if '==Aiheesta muualla ==' in text:
					position = text.find('==Aiheesta muualla ==')

				if '== Aiheesta muualla ==' in text:
					position = text.find('== Aiheesta muualla ==')

				if '==Kirjallisuutta==' in text:
					position = text.find('==Kirjallisuutta==')

				if '== Kirjallisuutta==' in text:
					position = text.find('== Kirjallisuutta==')

				if '==Kirjallisuutta ==' in text:
					position = text.find('==Kirjallisuutta ==')

				if '== Kirjallisuutta ==' in text:
					position = text.find('== Kirjallisuutta ==')

				if position != 0:
					text_data = list(text)
					text_data.insert(position, '\n==Lähteet==\n{{viitteet}}\n\n')
					text = ''.join(text_data)
					errorcount += 1
					error = 3

			else:

				for line in reversed(text.split('\n')):
					if len(line) > 40:
						placingposition = text.rfind(line)+len(line)
						break
					elif '{{Tynkä' in line or '{{tynkä' in line and usenextline == 0:
						usenextline = 1
					elif '[[Luokka:' in line or '[[luokka:' in line and usenextline == 0:
						usenextline = 1
					elif '{{täsmennyssivu}}' in line or '{{Täsmennyssivu}}' in line and usenextline == 0:
						usenextline = 1
					elif line == '':
						usenextline = 1
						continue
					elif line == ' ':
						usenextline = 1
					elif '[[' in line and ':' in line and usenextline == 0:
						usenextline = 1
					elif usenextline == 1 and '*' in line[0:2]:
						placingposition = text.rfind(line)+len(line)
						break
					elif usenextline == 1 and '{{kesken' in line:
						placingposition = text.rfind(line)+len(line)
						break
					elif usenextline == 1 and '{{juonipaljastus loppu}}' in line:
						placingposition = text.rfind(line)+len(line)
						break
					elif usenextline == 1 and '{{Kesken}}' in line:
						placingposition = text.rfind(line)+len(line)
						break
					elif usenextline == 1 and '<ref' in line:
						placingposition = text.rfind(line)+len(line)
						break
					elif usenextline == 1 and '{{' in line[0:2]:
						continue
					elif usenextline == 1 and line == '\n':
						continue
					elif usenextline == 1 and '[[' in line[0:2] and ':' in line:
						continue
					elif usenextline == 1:
						placingposition = text.rfind(line)+len(line)
						break

					else:
						placingposition = text.rfind(line)+len(line)
						break
				if placingposition != 0:
					text_data = list(text)
					text_data.insert(placingposition, '\n\n==Lähteet==\n{{viitteet}}\n')
					text = ''.join(text_data)
					errorcount += 1
					error = 3

		elif position2 != 0 and position3 != 0 and position2 > position3:
			text = text.replace('==Lähteet==', '')
			text = text.replace('== Lähteet ==', '')
			if position3 != 0:
				text_data = list(text)
				text_data.insert(position3, '\n==Lähteet==\n{{viitteet}}\n\n')
				text = ''.join(text_data)
				donttouch = 1
				errorcount += 1
				error = 4


		else:
			print(position2, position3)
			if position2 < position3 or position3 == 0:
				print('ok')
				addreferences = 0
				endposition = 0
				foundlist = 0
				foundpos = 0
				for line in reversed(text.split('\n')):
					if '==Lähteet==' in line or '== Lähteet==' in line or '==Lähteet ==' in line or '===Viitteet===' in line or ' ===Viitteet===' in line or '===Viitteet ===' in line or '=== Viitteet ===' in line or '== Lähteet ==' in line:
						startposition = text.rfind(line)
						if line == '===Viitteet===':
							endposition = startposition + len(line)
							break
						elif line == '=== Viitteet===':
							endposition = startposition + len(line)
							break
						elif line == '===Viitteet ===':
							endposition = startposition + len(line)
							break
						elif line == '=== Viitteet ===':
							endposition = startposition + len(line)
							break
						elif line == '==Lähteet==':
							addreferences = 1
							endposition = startposition + len(line)
							break
						elif line == '== Lähteet==':
							addreferences = 1
							endposition = startposition + len(line)
							break
						elif line == '==Lähteet ==':
							addreferences = 1
							endposition = startposition + len(line)
							break
						elif line == '== Lähteet ==':
							addreferences = 1
							endposition = startposition + len(line)
							break
				if endposition != 0:
					if '*' in text[endposition:endposition+3] or '{{Commons' in text[endposition:endposition+11] or '{{commons' in text[endposition:endposition+11] or '{{Kirjaviite'  in text[endposition:endposition+20] or '{{kirjaviite'  in text[endposition:endposition+20] or '{{Lehtiviite'  in text[endposition:endposition+20] or '{{lehtiviite'  in text[endposition:endposition+20] or '{{Verkkoviite'  in text[endposition:endposition+20] or '{{verkkoviite'  in text[endposition:endposition+20] or '{{Karttaviite' in text[endposition:endposition+20] or '{{karttaviite' in text[endposition:endposition+20] or '{{Standardiviite' in text[endposition:endposition+20] or '{{standardiviite' in text[endposition:endposition+20]:
						lastposition = 0
						lastlen = 0
						time = 0
						print(text[endposition:].split('\n'))
						for line in text[endposition:].split('\n'):
							time += 1
							if '*' in line or '{{Commons' in line or '{{commons' in line or '{{kirjaviite' in line or '{{Kirjaviite' in line or '{{Lehtiviite' in line or '{{lehtiviite' in line or '{{Verkkoviite' in line or '{{verkkoviite' in line or '{{Karttaviite' in line or '{{karttaviite' in line or '{{Standardiviite' in line or '{{standardiviite' in line or '{{IMDb-h' in line and foundlist != 1:
								foundlist = 1
								lastposition = text[endposition:].find(line)
								lastlen = len(line)
							if '*' not in line and '{{Commons' not in line and '{{commons' not in line and '{{kirjaviite' not in line and '{{Kirjaviite' not in line and '{{Lehtiviite' not in line and '{{lehtiviite' not in line and '{{Verkkoviite' not in line and '{{verkkoviite' not in line and '{{Karttaviite' not in line and '{{karttaviite' not in line and '{{Standardiviite' not in line and '{{standardiviite' not in line and '|' not in line and '{{IMDb-h' not in line and line != '' and lastlen != 0 and lastposition != 0 or time == len(text[endposition:].split('\n')):
								if addreferences == 1 and foundlist == 1 and line != '\n':
									endposition = endposition + lastposition + lastlen
									text_data = list(text)
									text_data.insert(endposition, '\n\n===Viitteet===\n{{viitteet}}\n')
									text = ''.join(text_data)
									errorcount += 1
									error = 1
									break

								elif addreferences == 1 and foundlist == 1 and line == '\n':
									endposition = endposition + lastposition
									text_data = list(text)
									text_data.insert(endposition, '\n\n===Viitteet===\n{{viitteet}}\n')
									text = ''.join(text_data)
									errorcount += 1
									error = 1
									break

								else:
									endposition = endposition + lastposition + lastlen
									text_data = list(text)
									text_data.insert(endposition, '\n{{viitteet}}')
									text = ''.join(text_data)
									errorcount += 1
									error = 2
									break

					else:
						text_data = list(text)
						text_data.insert(endposition, '\n{{viitteet}}')
						text = ''.join(text_data)
						errorcount += 1
						error = 2

	if position2 != 0 and position3 != 0 and position2 > position3 and donttouch == 0:
		if '{{viitteet}}' in text or '{{Viitteet}}' in text or '<references/>' in text or '<references />' in text:
			data_list = text.split('\n')
			try:
				data_list.remove('==Lähteet==')
			except:
				pass
			try:
				data_list.remove('== Lähteet==')
			except:
				pass
			try:
				data_list.remove('==Lähteet ==')
			except:
				pass
			try:
				data_list.remove('== Lähteet ==')
			except:
				pass
			try:
				data_list.remove('{{viitteet}}')
			except:
				pass
			try:
				data_list.remove('{{Viitteet}}')
			except:
				pass
			try:
				data_list.remove('<references/>')
			except:
				pass
			try:
				data_list.remove('<references />')
			except:
				pass
			text = '\n'.join(data_list)
			if position3 != 0:
				text_data = list(text)
				text_data.insert(position3, '\n==Lähteet==\n{{viitteet}}\n\n')
				text = ''.join(text_data)
				errorcount += 1
				error = 5


	if text != oldtext:
		zeroedit = 1
		printlog('fixreflist error found: '+ article)
		if errorcount == 1 and lang == 'fi' and error == 1:
			saves = u"Botti lisäsi puuttuvan viitteet osion. "
		elif errorcount == 1 and lang == 'fi' and error == 2:
			saves = u"Botti lisäsi puuttuvan viitteet mallinen. "
		elif errorcount == 1 and lang == 'fi' and error == 3:
			saves = u"Botti lisäsi puuttuvan lähteet osion. "
		elif errorcount == 1 and lang == 'fi' and error == 4:
			saves = u"Botti siirsi lähteet osion oikeaan kohtaan, ja lisäsi viitteet mallinen. "
		elif errorcount == 1 and lang == 'fi' and error == 5:
			saves = u"Botti siirsi lähteet osion oikeaan kohtaan. "
		elif errorcount == 1 and lang == 'en' and error == 2:
			saves = u"Bot has added missing references template. "
		elif errorcount == 1 and lang == 'en' and error == 1:
			saves = u"Bot has added missing references section. "


	elif errorcount == 0:
		printlog('fixreflist error not found: '+ article)

	return errorcount, text, saves, zeroedit