#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import random
import hashlib
import sys

def main():
	f = open("access.log-20141026", "r");
	fo = open("output_ip.txt", "a");
	i = 0;

	for l in f:	
		#print l;
		#print len(l);
		ip = l[-17:];
		ip = ip.replace('"', '');
		fo.write(ip);

	f.close();
	fo.close();

if __name__ == "__main__":
	main()
