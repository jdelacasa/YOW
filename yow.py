"""
    YOW - Your Own Wordlist
    Authors:
        Juan Antonio Velasco Gómez (@juanvelascogomez)
        Antonio Solis Izquierdo (@asolisi)
"""

#Creating a file for output
file_name=input("Introduce a name for your output file -->  ")
doc=open(file_name+".txt","w")

#Creating two list for the wordlist
word_list=[]
word_list_new=[]

#Introduce words in the wordlist
word=input("Introduce a key word : \n")
while word != "quit":
    word_list.append(word)
    word=input("Introduce more key words (type 'quit' to finish)\n")

#Printing the input words
#print(word_list)

for i in word_list:
    for j in word_list:
        if(i!=j):
            word_list_new.append(i+j)

#Printing the new wordlist
#print(word_list_new)

#Writting the new wordlist in the output file
for i in word_list_new:
    doc.write(i + "\n")

doc.close()
