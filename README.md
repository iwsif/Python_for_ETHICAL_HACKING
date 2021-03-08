
![](https://media.giphy.com/media/dLolp8dtrYCJi/giphy.gif)



# Python_For_Ethical_Hacking
***Python tools for security testing***

***FOR PEN-TEST PURPOSES ONLY***

**[dos_tool.py(Denial of Service vulnerability testing)]**

*Steps:
  Download python3 meterpreter(FOR WINDOWS USERS)
  
  Check if permissions are right
  Else type chmod u+x + FILENAME 
  
  Type "./"  + programs name and the you need to pass the target ip,your fake ip address,and how many processes you want to  start for this program(Start several    processes with multiprocessing module).
Control + c for exit.*

**[PyKeylogger]**
**Simple keyboard logger**

*Implemented python3.
    Run pip3 install pynput(Module needed for keyboard listening!!)
    Extract the program by typing python3 + programs name or simply "./"  and programs name.
    Pass your email,your password,time to wait before sending another event to your gmail account.
    This programs uses gmail stmp server(Turn off the security setting at your gmail account in order to receive events)
    Start program.*

**[Random_Word-Generator]**
**Word generator that produces number of words and save them to a file.**
  *Start the program with python3 programs name or "./" and programs name.
  Pass as arguments the length of each word,how many words you want to generate and the file in which you want to save the results.*

**[FTP brute-forcer]**
*If you dont have ftplib do pip3 install ftplib and run the script with python3.
  OPTIONS:
  --target for target ip address.
  --list pass the wordlist file.
  Port optional argument default=21 port.*

**[encrypt_fs.py]**

**DONT USE THIS PROGRAM IF YOU DONT KNOW WHAT YOU DOING**

**RISK FOR WHOLE SYSTEM!!**

*You need to download python3 meterpreter(FOR WINDOWS USERS ONLY)
  STEPS:
  pip3 install cryptography && pip3 install paramiko(SSH CLIENT)  chmod -x && chmod u+x FILENAME(User only permission to extract..)
  Type FILENAME --help(FOR HELP WITH ARGUMENTS)  Start program by typing ./ or python3 + FILENAME + arguments*
  EVIL MODE ENCRYPTS  WHOLE FILESYSTEM AND SENDS THE KEY TO EVIL SERVER VIA SSH*
  
 **[extract_info.py]** 
 
 ***EXTRACT LINKS FROM WEBSITE (RISK WEBSITE OVERLOADING DUE TO HIGH RECURSION_LIMIT)***
 
 *pip3 install requests && 
    pip3 install stem &&
    pip3 install cfscrape &&
    pip3 install bs4*
 
 *chmod -x FILENAME && chmod u+x FILENAME  ANON MODE(TOR BYPASS-FOR ANTIBOT SYSTEMS)  CFSCRAPE MODULE (FOR BYPASSING ANTIBOT SYSTEMS)*





