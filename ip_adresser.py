#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import sys

def main(argv):
	if len(argv) < 2:
		print "Usage: %s <log-file-to-parse>" % argv[0];
		sys.exit();

	f = open(argv[1], "r");
#	f = open("access.log-20141026", "r");
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
	main(sys.argv)
