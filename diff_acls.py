#!/usr/local/python2.7.3/bin/python

"""
    This script takes 2 acl files and finds difference in the files
    It ignores lines that have remark keyword and lines starting with #

    This is how you run this

    ./diff_acls.py ./data/acl_profile_1 ./data/acl_profile_2

"""

import sys
import os, fnmatch
import subprocess
import re
from string import letters, lower

if len(sys.argv) < 3:
    print("USAGE: %s <ACL File 1> <ACL File 2>" % sys.argv[0])
    sys.exit(-1)

try:
    infile = open(str(sys.argv[1]), "r")
    lines = infile.readlines()
    infile.close()
except Exception as ex:
    print("Unable to to open %s for reading: %s" % (str(sys.argv[1]), str(ex)))
    sys.exit(-2)

try:
    infile1 = open(str(sys.argv[2]), "r")
    lines1 = infile1.readlines()
    infile1.close()
except Exception as ex:
    print("Unable to to open %s for reading: %s" % (str(sys.argv[2]), str(ex)))
    sys.exit(-2)

myAcl1Dic = {}
myAcl2Dic = {}

for line in lines:
    if line.strip():
        if line.startswith("#"):
            continue
        #if re.match("remark", line):   ## Matches only at the begining of the string
        if re.search("remark", line):  ## Matches anywhere in the string
            continue
        acl = ' '.join(line.split()[1:]) # Get everything except the first one and convert list to string
        #print acl
        if acl in myAcl1Dic: # Check if Key Exists
            myAcl1Dic[acl] += 1
            print ("Duplicate ACL %s in %s" % (acl, str(sys.argv[2])))
        else:
            myAcl1Dic[acl] = 1
for line1 in lines1:
     if line1.strip():
        if line1.startswith("#"):
            continue
        if re.search("remark", line1):  ## Matches anywhere in the string
            continue
        acl2 = ' '.join(line1.split()[1:]) # Get everything except the first one and convert list to string
        if acl2 in myAcl2Dic: # Check if Key Exists
            myAcl2Dic[acl2] += 1
            print ("Duplicate ACL %s in %s" % (acl2, str(sys.argv[3])))
        else:
            myAcl2Dic[acl2] = 1

for key in (myAcl1Dic.iterkeys()):
    if key not in myAcl2Dic:  # Check if Key does not Exists
        print ("%s not in %s" % (key, str(sys.argv[2])))

for key1 in (myAcl2Dic.iterkeys()):
    if key1 not in myAcl1Dic:  # Check if Key does not Exists
        print ("%s not in %s" % (key1, str(sys.argv[1])))
