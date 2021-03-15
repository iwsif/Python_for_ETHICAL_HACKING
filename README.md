

# //\\//\\//\\  Python_For_Ethical_Hacking  //\\//\\//\\

**Python tools for security testing**

**For PEN-TEST purposes ONLY**

**[dos_tool.py]**

Steps:

  *Download python3 meterpreter(for WINDOWS users).*
  
  *Check if permissions are right.*
  
  *Else type >> chmod u+x + FILE.*  
  
  *Type "./"  + programs name and the you need to pass the target ip,your fake ip address,and how many processes you want to start for this program(Start several  processes with multiprocessing module).*
  
  *Control + c for exit.*


_________________________________________________________________________________________________________________________________________________________________


**[PyKeylogger]**

**Simple keyboard logger.**

*Written in python3.**
    
*Run pip3 install pynput(Module needed for keyboard listening!!)*
    
*Extract the program by typing python3 + programs name or simply "./"  and programs name.*
    
*Pass your email,your password,time to wait before sending another event to your gmail account.*
    
*This programs uses gmail stmp server(Turn off the security setting at your gmail account in order to receive events).*
    
*Start program.*
    
 _________________________________________________________________________________________________________________________________________________________________



**[Random_Word-Generator]**

**Word generator that produces number of words and save them to a file.**

*Start the program with python3 programs name or "./" and programs name.*
 
*Pass as arguments the length of each word,how many words you want to generate and the file in which you want to save the results.*


__________________________________________________________________________________________________________________________________________________________________


**[FTP brute-forcer]**

*If you dont have ftplib do pip3 install ftplib and run the script with python3.
  
  Options:
  
  *--target //  for target ip address.*
  
  *--list //  pass the wordlist file.*
  
  *--port //  optional argument default=21 port.*


__________________________________________________________________________________________________________________________________________________________________


**[encrypt_fs.py]**

**DONT USE THIS PROGRAM IF YOU DONT KNOW WHAT YOU DOING!!**

**RISK FOR WHOLE SYSTEM!!**

*You need to download python3 meterpreter(for WINDOWS users ONLY)*.
 
 Steps:
 
 *pip3 install cryptography && pip3 install paramiko(SSH client) chmod -x && chmod u+x FILE.*
  
 *Type  >> FILE --help(to see arguments).Start program by typing ./ or python3 + FILE + arguments.*
  
 *Evil mode ENCRYPTS whole filesystem and sends the key to EVIL server via SSH.*
  
__________________________________________________________________________________________________________________________________________________________________


 **[extract_info.py]** 
 
 **Extracts links from website**
 
 **RISK website OVERLOADING due to HIGH RECURSION limit!!**
 
 *pip3 install requests && pip3 install stem && pip3 install cfscrape && pip3 install bs4*
 
 *chmod -x FILE && chmod u+x FILE  \\//\\// anon mode(Tor Bypass for ANTIBOT systems) \\//\\// cfscrape module for bypassing ANTIBOT systems*


__________________________________________________________________________________________________________________________________________________________________


**[domain.py]**

**Find web domain.**

*You need a dictionary with possible domain names for this program.* 

 *pip3 install requests && chmod -x FILE && chmod u+x FILE.*
 
 *Type  >>  ./ or python3 to extract the program.See --help for program info.*
  

_________________________________________________________________________________________________________________________________________________________________





