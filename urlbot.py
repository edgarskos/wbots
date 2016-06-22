#! /usr/bin/env python3

#import built in modules
import sys
#path append
sys.path.append('core/libs/')
from core.fixlinks import fixlink
from core.fix2brackets import fix2brackets

def main():
	#fixlink('testbot')
	fix2brackets('testbot')

if __name__ == '__main__':
	main()