#! /usr/bin/env python3

#built in modules
import sys

#core modules
sys.path.append('core/libs/')
from core.findversion import getversion

def main():

	article = 'sublime ted'
	article = article.lower()
	verion = getversion('https://www.sublimetext.com/3', article)

	print('found this version:', verion)


if __name__ == '__main__':
	main()