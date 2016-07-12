#!/usr/bin/env python3

from __future__ import unicode_literals
import sys
import os
from optparse import OptionParser
from difflib import unified_diff

import re as regex
from bs4 import BeautifulSoup
from prettytable import PrettyTable


RETF_FILENAME = 'retf-fi.txt'
ENCODING = 'utf8'

# some rules are not working with regex or are not useful
disabled = {
	"Etc.",
	"e.g.",
	"i.e.",
	"Currency symbol before number",
	"et al.",
	" ,",
	"F (farad)",  # replaces .nf => .nF ?!?
	"Newly",      # replaces newly-created => newly created
	"Recently",   # recently-commtted => recently committed, breaks "least-recently-used"
	"Highly",
	"exactly the same",  # only stylistic
	"of xxx of xxx",     # causes an infinite loop in regex?
	"Apache",
	"Arabic",
}

PY2 = sys.version_info[0] <= 2


def load_rules(filename):

	with open(filename) as rulefile:
		soup = BeautifulSoup(rulefile, 'html.parser')
	regs = []

	n_disabled = 0
	n_errors = 0
	n_loaded = 0

	for typo in soup.findAll('typo'):
		if 'word' not in typo.attrs or typo.attrs['word'] in disabled:
			n_disabled += 1
			continue

		word = typo.attrs['word']
		find = typo.attrs['find']
		replace = typo.attrs['replace']

		try:
			r = regex.compile(find)
			replace = replace.replace('$', '\\')

			regs.append((word, r, replace))
			n_loaded += 1
		except:
			pass

	return regs


def handle_article(regs, article):

	oldtext = text = article
	if not text:
		return

	replaced = 0
	for word, r, replace in regs:
		newtext, count = r.subn(replace, text)
		if count > 0 and newtext != text:
			replaced += count
		text = newtext
	oldtextlist = oldtext.split()
	textlist = text.split()
	list3 = oldtextlist + textlist
	outputlist = []
	for i in range(0, len(list3)):
		if ((list3[i] not in oldtextlist) or (list3[i] not in textlist)) and (list3[i] not in outputlist):
			outputlist[len(outputlist):] = [list3[i]]
	if replaced > 0:
		time = 0
		t = PrettyTable(['before', ' ', 'after'])
		t.add_row(['------','', '-----'])
		t.align = 'l'
		t.valing = 'm'
		t.border = False
		for item in outputlist:
			try:
				t.add_row([item,'-->', outputlist[int(len(outputlist) / 2+time)]])
			except:
				pass
			time += 1

		print(t)
		print()

		answer = input('do you agree these changes? [Y/N] ')
		if answer == 'y' or answer == 'yes':
			return text
		else:
			return oldtext
	else:
		return oldtext

def fixtypo(article):
	regs = load_rules('core/libs/topy/retf-fi.txt')

	text = handle_article(regs, article)
	return text