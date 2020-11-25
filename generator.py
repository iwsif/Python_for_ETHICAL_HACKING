#! /usr/bin/python3

import optparse 
import random
import os
import time

#Starting the class with the constructor 
class word_generator:
    def __init__(self):
        self.lower_chars = ["a","b","c","d","q","w","e","r","t","y","u","i","o","p","f","g","h","j","k","l","z","x","c","v","b","n","m"]
        self.upper_chars = []
        for char in self.lower_chars:
            self.upper_chars.append(char.upper())
        parser = optparse.OptionParser()
        parser.add_option("-l","--length",dest="length",help="Type how many chars you want to include in your word")
        parser.add_option("-w","--words",dest="words",help="Type in how many words you want to generate")
        parser.add_option("-f","--file",dest="file",help="Type the name of the file in which you want to save the list")
        values = parser.parse_args()[0]
        if not values.length:
            parser.error("Type in how many chars you want me to include in the word")
        elif not values.file:
            parser.error("Type in the the name of the file,where you want to save the list")
        elif not values.words:
            parser.error("Type in how many words you want to generate")
        else:
            self.length = values.length 
            self.file = values.file 
            self.number_of_words = values.words 

    def generate_words(self):
        self.random_chars = []
        random_words = []
        self.word = ""
        self.wordlist = []
        for char in self.lower_chars:
            self.random_chars.append(self.lower_chars[random.randrange(0,len(self.lower_chars))])
        self.algo(self.random_chars,self.word,self.length,self.wordlist,self.number_of_words)
        if(len(self.wordlist) < int(self.number_of_words)):
            remaining_words = int(self.number_of_words) - len(self.wordlist)
            self.algo(self.random_chars,self.word,self.length,self.wordlist,remaining_words)       
        self.write_to_file(self.file,self.wordlist)
                           
    def algo(self,random_char_list,word,length,wordlist,number_of_words):
        for number in range(int(number_of_words)):
            for i in range(0,int(length)): 
                if len(word)!= len(range(0,int(length))):
                    word = word + random.choice(random_char_list)
                else:
                    wordlist.append(word) 
                    word = ""
                    continue                                    

    def write_to_file(self,filename,wordlist):
        with open(filename,"w") as file:
            for word in wordlist:
                file.write(word + "\n") 

def start_process():
    print("Welcome!!")
    print("Starting process...")
    time.sleep(2)
    generator = word_generator()
    generator.generate_words()
    time.sleep(2)
    print("\nDone!!!")
    time.sleep(2)

start_process()

