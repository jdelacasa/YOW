"""
    YOW - Your Own Wordlist
    Authors:
        Juan Antonio Velasco Gomez (@juanvelascogomez)
        Antonio Solis Izquierdo (@asolisi)
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


#Compatibility Python2 and Python3 for input
try:
    input = raw_input
except NameError:
    pass

#---------------------------------------------------
# WELCOMO TO YOW TOOL
#---------------------------------------------------
print("\n##################################")
print("WELCOME TO YOW - Your Own Wordlist \n")
print(" Authors: \n     @juanvelascogomez \n     @asolisi")
print("################################## \n")

#---------------------------------------------------
#Creating a file for output
#---------------------------------------------------
file_name=input("Introduce the name for your output file -->  ")
doc=open(file_name+".txt","w")

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

if len(sys.argv)>=2:
    doc2=open(sys.argv[1],"r")
    lines=doc2.readlines()
    for li in lines:
        if li != "\n":
            word_list.append(li.replace("\n",""))
else:
    #---------------------------------------------------
    #Introduce words in the wordlist
    #---------------------------------------------------
    word=input("Introduce a key word : \n")
    while word != "quit":
        word_list.append(word)
        word=input("Introduce more key words (type 'quit' to finish)\n")

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
