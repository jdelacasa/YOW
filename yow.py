"""
    YOW - Your Own Wordlist
    Authors:
        Juan Antonio Velasco Gomez (@juanvelascogomez)
        Antonio Solis Izquierdo (@asolisi)
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os

# colors
yellow="\033[33m"
red="\033[31m"
reset="\033[0m"

#Compatibility Python2 and Python3 for input
try:
    input = raw_input
except NameError:
    pass


banner =  """ _   _  _____      __
| | | |/ _ \ \ /\ / /
| |_| | (_) \ V  V / 
 \__, |\___/ \_/\_/  
 |___/ %sAuthors:%s @juanvelascogomez & @asolisi              
 Your Own Wordlist!\n"""

menu = ['--version', '--update', '--help']
v = "v1.2"

def main():
    # Check if argv [1] is in the menu  
    if sys.argv[1] in menu:
        for i in menu:
            if sys.argv[1] == i:
                command = str(i).replace("--", "")
                # Execute function
                globals()[command]()
    
    # Banner
    print banner %(yellow, reset)
    
    # argv[1] is the name of the new dictionary
    if len(sys.argv) == 2:
        if os.path.isfile(sys.argv[1]):
            doc=open("new_" + sys.argv[1], "w")
        doc=open(sys.argv[1], "w")
    else:
        #Creating a file for output
        try:
            file_name=input("[%s?%s] Name of the dictionary: " %(yellow, reset))
        except KeyboardInterrupt:
            print "\nGood Bye!"
            sys.exit()

        if os.path.isfile(file_name):
            doc=open("new_" + file_name, "w")
        doc=open(file_name, "w")
    
    #---------------------------------------------------
    #Creating two list for the wordlist
    #---------------------------------------------------
    word_list=[]
    word_list_aux=[]
    
    word_list_new=[]
    word_list_second=[]
    
    #---------------------------------------------------
    #Read
    #---------------------------------------------------
    
    #Introduce words in the word_list
    try:
        # Enter the keywords as follows: hello; Friend; Dog; Cat
        word = input("[%s*%s] keywords: " %(yellow,reset))
    except KeyboardInterrupt:
        print "\nGood Bye!"
        sys.exit()

    # To convert vb to a list    
    word_list = word.split("; ")

    #---------------------------------------------------
    #Init inicial wordlist with words in:
    #   - All words in lower case
    #   - All words in upper case
    #   - All words with first letter capitalize
    #---------------------------------------------------
    
    #Set all initial words in lower
    for i in word_list:
        word_list_aux.append(i.lower())
    
    #Reset initial wordlist
    word_list[:] = []
    
    #Fill initial wordlist with all new words
    for i in word_list_aux:
        word_list.append(i)
        word_list.append(i.upper())
        word_list.append(i.capitalize())
    
    
    #---------------------------------------------------
    #Loop for combination of two words
    #---------------------------------------------------
    for i in word_list:
        for j in word_list:
            if(i!=j):
                word_list_new.append(i+j)
    
    #---------------------------------------------------
    #Loop for combination of three words
    #---------------------------------------------------
    for i in word_list:
        for j in word_list_new:
            if(i!=j):
                word_list_second.append(i+j)
    
    #---------------------------------------------------
    #Writting the new wordlist in the output file
    #---------------------------------------------------
    for i in word_list_new:
        doc.write(i + "\n")

    for i in word_list_second:
        doc.write(i+"\n")

    doc.close()

def version():
    print banner %(yellow, reset)
    print "%s Version: %s%s"%(yellow,reset,v)
    sys.exit()

def help():
    print """ Help YOW
    use: python yow.py <file_name>

    --help      Show help
    --version   Show verion
    --update    Update YOW"""
    sys.exit()

def update():
    print "update ..."
    try:
        os.system('git pull')
        print "[%s!%s] Please restart YOW\n" %(yellow, reset)
    except:
        print "[%s*%s] E: Please use <git pull> to update\n" %(red,reset)
    sys.exit()

if __name__ == '__main__':
    main()
