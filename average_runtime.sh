#! /bin/bash

VERSION=v24
LEVEL=13

grep "$VERSION" total_runtimes.txt | \
	grep "rand2 fe2141bf2591a193986a3e506640302f $LEVEL " | \
	awk '{ total += $0; count++ } END { print total/count }' 
