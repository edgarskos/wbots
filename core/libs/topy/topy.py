#!/usr/bin/env python3

from __future__ import unicode_literals
import sys
import os
from optparse import OptionParser
from difflib import unified_diff

import re as regex
from bs4 import BeautifulSoup
from core import adiffer


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
	oldtextlist = oldtext.split('\n')
	textlist = text.split('\n')
	if replaced > 0:
		for oldline, line in zip(oldtextlist, textlist):
			if oldline != line:
				adiffer.show_diffl(oldline, line)

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