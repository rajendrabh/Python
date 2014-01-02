#!/usr/bin/env python
"""
     Usage : cleanupVideoAssetFiles.py -i <inputfile> -c <list|delete>
             inputfile -> should contain the .pck files to list or delete
             command -> option should either be list or delete

     Description :
         This script will clean-up JITP assets associated with the .pck files.
         Always use the list command option to list the files to be deleted. Verify it
         and if possible ask the requester or the ticket creator to verify it.
         Then use the delete command option to delete the files.
         Always attach the files listed and deleted to the ticket.

         Make sure you have a ticket before you run this script. 
         Sample input file -> ./data/12-09-13_cleanup_assets_vss.csv
     
"""

import os
import sys, getopt

def countFoldersFilesSize(rootDir):
    fileList = []
    fileSize = 0
    folderCount = 0

    for root, subFolders, files in os.walk(rootDir):
        folderCount += len(subFolders)
        for file in files:
            f = os.path.join(root,file)
            fileSize = fileSize + os.path.getsize(f)
            #print(f)
            fileList.append(f)

    print("Total Size is {0} bytes".format(fileSize))
    print("Total Files ", len(fileList))
    print("Total Folders ", folderCount)

def listFilesRecursively(rootDir):
    fileList = []
    if (os.path.exists(rootDir)):
        for root, subFolders, files in os.walk(rootDir):
            for file in files:
                fileList.append(os.path.join(root,file))
        #print fileList
        for file1 in fileList:
            print file1
    else:
        print ("%s - This directory does not exist ---ERROR--- " % (rootDir))

def deleteFilesRecursively(rootDir):
    fileList = []
    if (os.path.exists(rootDir)):
        for root, subFolders, files in os.walk(rootDir):
            for file in files:
                fileList.append(os.path.join(root,file))
        for file1 in fileList:
            print ("Deleting file %s" % (file1))
            os.remove(file1) # Remove the files
    else:
        print ("%s - This directory does not exist ---ERROR--- " % (rootDir))

def listFiles(assetFiles):
    aFILES = open(assetFiles, "rt")
    asf = aFILES.readlines()
    for i in asf:
        i = i.strip()
        if not os.path.isfile(i):
            print ("%s file does not exist ---ERROR--- " % (i)) 
        dir = os.path.dirname(os.path.abspath(i))
        if (os.path.exists(dir)):
            print ("File name = %s \nDirectory = %s" % (i, dir))
            print ("=============================================================")
            print "List of file(s) under the directory %s are:" % dir
            #for files in os.listdir(dir):
            #    print files
            listFilesRecursively(dir)
            countFoldersFilesSize(dir)
            print ("=============================================================")
        else:
            print ("%s - This directory does not exist ---ERROR--- " % (dir))
            print ("=============================================================")

def deleteFiles(assetFiles):
    aFILES = open(assetFiles, "rt")
    asf = aFILES.readlines()
    for i in asf:
        i = i.strip()
        if not os.path.isfile(i):
            print ("%s file does not exist ---ERROR--- " % (i)) 
        dir = os.path.dirname(os.path.abspath(i))
        if (os.path.exists(dir)):
            print ("File name = %s \nDirectory = %s" % (i, dir))
            print ("=============================================================")
            print "List of file(s) under the directory %s to be deleted are:" % dir
            deleteFilesRecursively(dir)
            print ("Deleting the directory %s" % (dir))
            os.rmdir(dir) ## Remove the directory after all the files in this directory are removed
            print ("=============================================================")
        else:
            print ("%s - This directory does not exist ---ERROR--- " % (dir))
            print ("=============================================================")

def usage():
    print 'cleanUpJitpAssets.py -i <inputfile> -c <list|delete>'
    print 'inputfile should contain the .pck files to list or delete'
    print 'command option should either be list or delete'
    

def main(argv):
    inputfile = ''
    command = ''
    try:
        opts, args = getopt.getopt(argv,"hi:c:",["ifile=","comm="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'cleanUpJitpAssets.py -i <inputfile> -c <list|delete>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-c", "--comm"):
            command = arg
    if (os.path.isfile(inputfile)):
        if command == 'list':
            listFiles(inputfile)
        elif command == 'delete':
            deleteFiles(inputfile)
        else:
            print "Wrong comand option entered, choose list or delete" 
            sys.exit(2)
    else:
        print ("Input file [%s] does not exist. Exiting." % (inputfile))
        sys.exit(2)

if __name__ == '__main__':
    main(sys.argv[1:])
