#! /usr/bin/env python3

#import built in modules
import sys
#path append
sys.path.append('core/libs/')
from core.fixlinks import fixlink
from core.fix2brackets import fix2brackets
from core.fixpiped import fixpiped
from core.log import *

def main():
	fixcout = 0
	articles = open('core/db/articles.db', 'r')
	#for line in articles:
	#	fixcout += fix2brackets(line)
	#fixlink('testbot')

	fixcout = fixpiped('testbot')
	printlog('fixcout: '+str(fixcout))

if __name__ == '__main__':
	main()