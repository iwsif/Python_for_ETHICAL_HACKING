#! /usr/bin/python3

from bs4 import BeautifulSoup
import requests
import cfscrape
import os
import requests
import sys
import subprocess
import optparse
import time
import colorama 
import multiprocessing
import urllib.parse
import stem.control
from stem import Signal

class Scraper:
    def __init__(self):
        self.RED = colorama.Fore.RED
        values = self.get_arguments()
        self.values = values
        self.is_installed = bool
        self.linux_distro = ""
        print("Checking if requirments are met ...")
        time.sleep(3)
        self.check_for_tor()
        if self.is_installed == True:
            pass
        else:
            self.check_system()
            self.install_tor()
        
        if __name__ == '__main__':
            os.environ["SOCKS4"] = "https://127.0.0.1:9050" 
            os.environ["SOCKS5"] = "https://127.0.0.1:9050"
        else:
            self.socks4 = "https://127.0.0.1:9050"
            self.socks5 = "https://127.0.0.1:9050"

    def check_for_tor(self):
        responce = subprocess.check_output(["which","torsocks"])
        if responce == "/usr/bin/torsocks":
            self.is_installed = True
        else:
            self.is_installed = False
    
    def install_tor(self):
        package_managers = ["yum","apt-get"]
        if self.linux_distro == "Debian/ubuntu":
            subprocess.call(["sudo",package_managers[1],"install","torsocks"])
            print({f"Done!!"})
        elif self.linux_distro == "Fedora":
            subprocess.call(["sudo",package_managers[0],"install","torsocks"])
            print({f"Done!!"})

    def check_system(self):
        if self.is_installed == True:
            system_info = os.uname()
            linux_distro = re.search("?:(\sversion=')(.*)'",system_info)
            if "Debian" or "Ubuntu"in linux_disto:
                self.linux_distro = "Debian/Ubuntu"
            elif "Fedora" in linux_distro:
                self.linux.distro = "Fedora"

    def get_arguments(self):
        parser = optparse.OptionParser()
        parser.add_option("-d","--domain",dest="domain",help="Type the domain that you want search for")
        parser.add_option("-s","--spoof",dest="spoof",help="Start a scraper that bypass anti-bot system(Type --spoof yes)")
        parser.add_option("-b","--burst",dest="burst",help="Increase scanning speed from 1 to 5(max=5,default=1)")
        parser.add_option("-a","--anon",dest="anon",help="Scrape with fake identity(Type --anon yes)")
        user_values = parser.parse_args()[0]
        if not user_values.domain:
            parser.error(self.RED + "You must type a domain name!!!")
        elif user_values.spoof and user_values.anon:
            parser.error(self.RED + "You must choose either the spoof option or anon,not both!!")
        else:
            return user_values 

    def get_response(self,domain,proxies=None):
        try:
            if "https://" not in domain:
                domain = "https://" + domain
                if proxies == proxies:
                    return requests.get(domain,proxies=proxies).content
                else:
                    return requests.get(domain).content
        except requests.exceptions.ConnectionError:
            pass
        except Exception:
            print(self.RED + "Invalid URL..")
            sys.exit(0)
    
    #def send_requests(self,domain):
        #response = self.get_response(domain)
        #return response 

    def link_extractor(self,response):
        base_url = self.values.domain
        link_list = []
        soup = BeautifulSoup(response)
        links = soup.find_all("link")
        for link in links:
            link = urllib.parse.urljoin(base_url,str(link))
            if base_url in link and link not in link_list:
                link_list.append(link)
            if "#" in link:
                link = link.split("#")[0]
        for link in link_list:
            print(link)
            try:
                self.link_extractor(link)
            except RecursionError:
                sys.setrecursionlimit(2000)
                continue

    def anti_bot_scraper(self,domain):
        scraper = cfscrape.create_scraper()
        if "https://" not in domain:
            domain = "https://" + domain
        response = scraper.get(domain)
        return response .content

    def anon(self,domain):
        if __name__ == "__main__":
            proxies = {"SOCKS4":os.getenv("SOCKS4"),"SOCKS5":os.getenv("SOCKS5")}
        else:
            proxies = {"SOCKS4":self.socks4,"SOCKS5":self.socks5}
        return self.get_response(domain,proxies=proxies)

    def renew_connection(self):
        with stem.control.Controller.from_port(port="9051") as controller:
            controller.authenticate()
            controller.signal(NEWNYM)
            
    def burst(self,response):
        process_pool = []
        number_of_processes = 4
        default_option = 1
        if self.values.burst == "2":
            number_of_processes = number_of_processes * 2
        elif self.values.burst == "3":
            number_of_processes = number_of_processes * 4
        elif self.values.burst == "4":
            number_of_processes = number_of_processes * 5
        elif self.values.burst == "5":
            number_of_processes == number_of_processes * 6
        for process in range(1,number_of_processes):
            process = multiprocessing.Process(target=self.link_extractor(response))
            process_pool.append(process)
        for process in process_pool:
            process.start()
    
    def start_game(self):
        if not self.values.spoof and not self.values.anon:
            response = self.get_response(self.values.domain)
            self.burst(response)
        elif self.values.spoof and not self.values.anon:
            response = self.anti_bot_scraper(self.values.domain)
            self.link_extractor(response)
        elif not self.values.spoof and self.values.anon:
            response = self.anon(self.values.domain)
            self.burst(response)
        
extract = Scraper()
extract.start_game()
