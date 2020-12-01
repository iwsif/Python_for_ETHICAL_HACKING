#! /usr/bin/python3

import re
import requests
import optparse
import colorama
import multiprocessing

GREEN = colorama.Fore.GREEN

class subdomains:
    def __init__(self):
        self.target = ""
        self.list = ""
        self.get_arguments()
    
    def get_arguments(self):
        parser = optparse.OptionParser()
        parser.add_option("-t","--target",dest="target",help="Type your target domain name")
        parser.add_option("-l","--list",dest="list",help="Pass me the list in order to start looking for subdomains")
        user_values = parser.parse_args()[0]
        if not user_values.target:
            parser.error("You have to type the domain_name of your target,type --help for more info")
        elif not user_values.list:
            parser.error("You have to pass me the list in order to search for posible domain names,type --help for more info")
        else:
            self.target = user_values.target 
            self.list = user_values.list 

    def check_connection(self,word):
        try:
            return requests.get("http://" + word)
        except requests.exceptions.ConnectionError:
            pass

    def check_for_subdomains(self):
        with open(self.list,"r") as wordlist:
            for word in wordlist:
                word = word.strip("\n")
                word = word + "." + self.target
                response = self.check_connection(word)
                if response:
                    print(GREEN + "Domain name found " + word)


start = subdomains()
start.check_for_subdomains()


        
    