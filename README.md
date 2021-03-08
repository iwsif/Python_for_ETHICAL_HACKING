# Python_For_Ethical_Hacking
***Python tools for security testing***
***Dos tool and Logger ARE ONLY FOR TESTING PURPOSES!!!***

**Denial of Service vulnerability testing**
*Steps:
  Download python3 meterpreter(FOR WINDOWS USERS)
  
  Check if permissions are right
  Else type chmod u+x + FILENAME 
  
  Type "./"  + programs name and the you need to pass the target ip,your fake ip address,and how many processes you want to  start for this program(Start several    processes with multiprocessing module).
  control + c for exit.*

**PyKeylogger**
**Simple keyboard logger**.
*Written in python3.
    Run pip3 install pynput(Module needed for keyboard listening!!)
    Extract the program by typing python3 + programs name or simply "./"  and programs name.
    Pass your email,your password,time to wait before sending another event to your gmail account.
    This programs uses gmail stmp server(Turn off the security setting at your gmail account in order to receive events)
    Start program.*

**Random_Word-Generator**
**Word generator that produces number of words and save them to a file.**
  *Start the program with python3 programs name or "./" and programs name.
  Pass as arguments the length of each word,how many words you want to generate and the file in which you want to save the results.*

**FTP brute-forcer**
*If you dont have ftplib do pip3 install ftplib and run the script with python3.
  OPTIONS:
  --target for target ip address.
  --list pass the wordlist file.
  Port optional argument default=21 port.*





