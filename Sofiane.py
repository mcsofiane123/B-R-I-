import os
import sys
from subprocess import *
import time
from V7xStyle import *
########################
os.system ('clear')
an= Animation
backtomenu_banner= """
[00] Back to main menu
[99] Exit the Tools
"""
def restart_program():
    python = sys.executable
    os.execl(python,python, * sys.argv)
def backtomenu_option():
    os.system('clear')
    print(backtomenu_banner)
    backtomenu = input("ꪶŌssꫂ...... ᵈᶻ > ")
    if backtomenu == "00":
        os.system('clear')
        os.system('clear')
        os.system('clear')
        os.system('clear')
        restart_program()
    elif backtomenu == "99":
        sys.exit()
    else:
        print("\nERROR: Wrong Input")
        time.sleep(2)
        restart_program()
ins = '#########Installing#########'
apt = 'apt update && apt upgrade -y'
def social_engineering():
    os.system('clear')
    an.DL(text = '               R#Wait Please ')
    os.system('clear')
    banner = Style("""G#              ____             _       _
G#             / ___|  ___   ___(_) __ _| |
G#             \___ \ / _ \ / __| |/ _` | |
Y#              ___) | (_) | (__| | (_| | |
Y#             |____/ \___/ \___|_|\__,_|_|
Y#
G# _____             _                      _
G#| ____|_ __   __ _(_)_ __   ___  ___ _ __(_)_ __   __ _
G#|  _| | °_ \ / _° | | °_ \ / _ \/ _ \ °__| | °_ \ / _` |
Y#| |___| | | | (_| | | | | |  __/  __/ |  | | | | | (_| |
Y#|_____|_| |_|\__, |_|_| |_|\___|\___|_|  |_|_| |_|\__, |
Y#             |___/                                |___/    """).Square(cols=1,Equal=False)
    print (banner)


    menu = Style ("G#[01]C#SELLFISH","G#[02]C#WEEMAN","G#[03]C#BLACK EYE","G#[04]C#SOCIAL FISH","G#[05]C#HIDDEN EYE","G#[06]C#SetTooLkit").Square(cols=2,
    	                                                                                                                                Equal=True,
    	                                                                                                                            padding_y=1,
    	                                                                                                                            padding_x=6,
    	                                                                                                                            space=3)
    print (menu)
    s = input ("\033[1;37mꪶŌssꫂ...... ᵈᶻ >")
    if s== '1':
        print (ins)
        os.system (apt)
        os.system ('git clone https://github.com/thelinuxchoice/shellphish ')
        os.system ('mv shellphish ~')
        print ('Your tools is succesfuly install..!')
    elif s== '2':
        print (ins)
        os.system (apt)
        os.system ('git clone https://github.com/evait-security/weeman')
        os.system ('mv weeman ~')
        print ("Your tools is installing..!")
    elif s == '3':
        print (ins)
        os.system (apt)
        os.system ('git clone https://github.com/thelinuxchoice/blackeye')
        os.system ('mv blackeye ~')
        print ("black eye is installing..!")
    elif s == '4':
        print (ins)
        os.system (apt)
        os.system ('git clone https://github.com/UndeadSec/SocialFish ')
        os.system ('mv SocialFish ~')
        print ("social fish is installing..!")
    elif s == "5" :
        print (ins)
        os.system(apt)
        os.system('git clone https://github.com/DarkSecDevelopers/HiddenEye')
        os.system ('mv HiddenEye ~')
        print ("Hidden eye is installing...!")
    elif s == "6":
        print (ins)
        os.system(apt)
        os.system('git clone https://github.com/trustedsec/social-engineer-toolkit')
        os.system("mv social-engineer-toolkit ~")
        print ("setToolkit is installing succesfuly..!")
    else:
        print ("Error...!"*100)
        restart_program()
    backtomenu_option()
###############✓....DDOS_ATTACK....✓####################
def DDos_Attack():
    os.system('clear')
    an.DL(text = '               R#Wait Please  ')
    os.system('clear')
    
    s=Style(""" Y#____  ____                 _   _   _             _
G#|  _ \|  _ \  ___  ___     / \ | |_| |_ __ _  ___| | __
P#| | | | | | |/ _ \/ __|   / _ \| __| __/ _` |/ __| |/ /
G#| |_| | |_| | (_) \__ \  / ___ \ |_| || (_| | (__|   <
Y#|____/|____/ \___/|___/ /_/   \_\__|\__\__,_|\___|_|\_\
""").Square(cols=1,Equal=False)
    print (s)
    tools =Style("G#[1] C#SlowLoris","G#[2] C#Websploit","G#[3] C#DDos Attack","G#[4] C#Xerves","G#[5] C#Hammer","G#[6] C#Golden eye").Square(cols=2,
                                                                                            Equal=True,
                                                                                              space=3,
                                                                                              padding_y=1,
                                                                                              padding_x=5)     
    print (tools)
    R = input ("\033[1;37mꪶŌssꫂ...... ᵈᶻ >")
    if R == '1':
        print (ins)
        os.system(apt)
        os.system('git clone https://github.com/gkbrk/slowloris')
        os.system ('mv slowloris ~')
        print ('slowloris is installing SuccesFuly...!')    
    elif R == '2':
        print (ins)
        os.system(apt)
        os.system('git clone https://github.com/websploit/websploit')
        os.system('mv websploit ~')
        print('websploit is Installing succesfuly...!')
    elif R == '3':
        print (ins)
        os.system(apt)
        os.system('git clone https://github.com/Ha3MrX/DDos-Attack')
        os.system('mv DDos-Attack ~')
        print ('DDos-Attack is Installing SuccesFuly...!')
    elif R == '4':
        print (ins)
        os.system(apt)
        os.system('git clone https://github.com/sepehrdaddev/Xerxes')
        os.system('mv Xerxes ~')
        print('Xerxes is Installing SuccesFuly...!')
    elif R == '5':
        print (ins)
        os.system(apt)
        os.system('git clone https://github.com/cyweb/hammer')
        os.system('mv hammer ~')
        print ('hammer is Installing SuccesFuly....!')
    elif R == '6':
        print (ins)
        os.system(apt)
        os.system('git clone https://github.com/jseidl/GoldenEye')
        os.system('mv GoldenEye ~')
        print ('GoldenEye is Installing SuccesFuly...!')
    else:
        print ('Error...!'*100)
        restart_program()
    backtomenu_option()
def Linux_Distro():
    os.system("clear")
    an.DL(text = '               R#Wait Please ')
    os.system('clear')
    ban = Style("""           B#  _     _
           C# | |   (_)_ __  _   ___  __
           B# | |   | | '_ \| | | \ \/ /
           C# | |___| | | | | |_| |>  <
           B# |_____|_|_| |_|\__,_/_/\_\
                
                                                        """).Square(cols=1,Equal=False)
    print (ban)
    List=Style("C#[1] G#Sudo","C#[2] G#Fedora","C#[3] G#Ubuntu","C#[4] G#Nethunter","C#[5] G#Kali Linux","C#[6]G# Parrot").Square(cols=2,
    	                                                                 Equal=True,
                                                                     padding_x=6,
    	                                                                 padding_y=1,
    	                                                                 space=2) 
    print (List)
#######################################################   
    k = input ("\033[1;37mꪶŌssꫂ...... ᵈᶻ >")
    if k == '1':
        print (ins)
        os.system(apt)
        os.system('git clone https://github.com/st42/termux-sudo ')
        os.system('mv termux-sudo ~')
        print ("Sudo is SuccèsFuly installed...! ")
    elif k =='2':
        print (ins)
        os.system(apt)
        os.system('wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh')
        os.system('mv termux-fedora.sh ~')
        print ('Fedora is Installed succesFuly...!')
    elif k =='3':
        print (ins)
        os.system(apt)
        os.system('git clone https://github.com/Neo-Oli/termux-ubuntu')
        os.system('mv termux-ubuntu ~')
        print ('Ubuntu is Installed SuccesFuly...!')
    elif k =='4':
        print (ins)
        os.system(apt)
        os.system('git clone https://github.com/Hax4us/Nethunter-In-Termux')
        os.system('mv Nethunter-In-Termux ~') 
        print ('Kali NethHunter  is Installed SuccesFuly...!')
    elif k == "5" :
        print (ins)
        os.system(apt)
        os.system('pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh')
        print ('Kali Linux Is installed succesFuly...!')
    elif k == "6" :
        print (ins)
        os.system(apt)
        os.system('pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Parrot/parrot.sh && bash parrot.sh')
        print ("Parrot Is Installed SuccesFuly...!")
    else:
        print("Error...!"*700)
        restart_program()
    backtomenu_option()
def Password_List():
    os.system('clear')
    an.DL(text = '               R#Wait Please ')
    os.system('clear')
    lg =Style(""" Y#  ____                                      _
Y#  |  _ \ __ _ ___ _____      _____  _ __ __| |
Y#  | |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |
Y#  |  __/ (_| \__ \__ \\ V  V / (_) | | | (_| |
Y#  |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|
                                                """).Square(cols=1,Equal=False)
    print(lg)
    lst= Style("C#[01] G#Cupp","C#[2] G#Ninja","C#[3] G#Goblin","C#[4] G#Word Gen","C#[5] G#CRUNCH","C#[6] G#Cewl").Square(cols=2,Equal=True,
    	padding_y=1,
    	padding_x=5,
    	space=2)
    print (lst)
    e = input("\033[1;37mꪶŌssꫂ...... ᵈᶻ >")
#######################################
    if e == '1':
        print (ins)
        os.system(apt)
        os.system('git clone https://github.com/Mebus/cupp')
        os.system('mv cupp ~')
        print ('Cupp Is installed Done...!')
    elif e == '2':
        print (ins)
        os.system(apt)
        os.system('git clone https://github.com/ninja-build/ninja')
        os.system('mv ninja ~')
        print('Ninja Word List Is installed Done...!')
    elif e == '3':
        print(ins)
        os.system(apt)
        os.system('git clone https://github.com/UndeadSec/GoblinWordGenerator')
        os.system('mv GoblinWordGenerator ~')
        print('Goblin is Installed Done..!')
    elif e == '4':
        print (ins)
        os.system(apt)
        os.system('git clone https://github.com/pfrazee/wordgen')
        os.system('mv wordgen ~')
        print ('Word Gen is installed Done...!')
    elif e == '5':
        print (ins)
        os.system(apt)
        os.system('git clone https://github.com/crunchsec/crunch')
        os.system('mv crunch ~')
        print('Crunch Is installed Done..!')
    elif e == '6':
        print (ins)
        os.system(apt)
        os.system('git clone https://github.com/digininja/CeWL')
        os.system('mv CeWL ~')
        print ('Cewl is Installed Done..!')
    else:
        print ('Error..!'*700)
        restart_program()
    backtomenu_option()
def web_Hacking():
    os.system('clear')
    an.DL(text = '               R#Wait Please ')
    os.system('clear')
    xn=Style("""            Y#    _       _                _    _
Y#  __      _____| |__   | |__   __ _  ___| | _(_)_ __   __ _
C#  \ \ /\ / / _ \ '_ \  | '_ \ / _` |/ __| |/ / | '_ \ / _` |
C#   \ V  V /  __/ |_) | | | | | (_| | (__|   <| | | | | (_| |
  R#  \_/\_/ \___|_.__/  |_| |_|\__,_|\___|_|\_\_|_| |_|\__, |
    B#                                                  |___/       """).Square(cols=1,Equal=True)
    print (xn)
    xl=Style("C#[01]Y#sqlmap","C#[02]Y#websploit","C#[03]Y#admin pannel login","C#[04]Y#Striker","C#[05]Y#Website-Vulnerability","C#[06]Y#nmap").Square(cols=2,Equal=True,padding_y=1,padding_x=3,space=2)
    print(xl)
    q=input('\033[1;37mꪶŌssꫂ...... ᵈᶻ >')
    if q == '1':
        print (ins)
        os.system(apt)
        os.system('git clone https://github.com/sqlmapproject/sqlmap')
        os.system('mv sqlmap ~')
        print ('sqlmap is installed done..!')
    elif q == '2':
        print (ins)
        os.system(apt)
        os.system('git clone https://github.com/websploit/websploit')
        os.system('mv websploit ~')
        print ('web sploit is installed done...!')
    elif q == '3':
        print (ins)
        os.system(apt)
        os.system('git clone https://github.com/MonroCoury/admin-panel-finder')
        os.system('mv admin-panel-finder ~')
        print ('admin pannel login is installed done...!')
    elif q == '4':
        print(ins)
        os.system(apt)
        os.system('git clone https://github.com/s0md3v/Striker')
        os.system('mv Striker ~ ')
        print('Striker is installed Done..!')
    elif q == '5':
        print (ins)
        os.system(apt)
        os.system('git clone https://github.com/ShubhamTuts/ShubhamWebScript-Website-vulnerability-Checker')
        os.system('mv ShubhamWebScript-Website-vulnerability-Checker ~')
        print('ShubhamWebScript-Website-vulnerability-Checker is installed..! Done..✓')
    elif q == '6':
        print (ins)
        os.system(apt)
        os.system('git clone https://github.com/nmap/nmap')
        os.system('mv nmap ~')
        print ('nmap is Installed SuccesFuly')
    else:
        print ('Error..!'*100)
        restart_program()
    backtomenu_option
def other():
    os.system('clear')
    an.DL(text = '               R#Wait Please ')
    os.system('clear')
    ls=Style("""
P#  ╔═╗  ╔══╗  ╔╗╔╗  ╔═╗  ╔═╗  ╔══╗
P#  ║║║  ╚╗╔╝  ║╚╝║  ║╦╝  ║╬║  ║══╣
P#  ║║║  ─║║─  ║╔╗║  ║╩╗  ║╗╣  ╠══║
P#  ╚═╝  ─╚╝─  ╚╝╚╝  ╚═╝  ╚╩╝  ╚══╝
P#  ───  ────  ────  ───  ───  ────       
                                  """).Square(cols=2,Equal=True)
    print(ls) 
    nano=Style('Y#[1] G#Lazymux','Y#[2]G# Tool-X','Y#[3] G#V7x-Tool','Y#[4]G# Fuck Admin',).Square(space=1,cols=1,Equal=True,padding_x=13,padding_y=1)
    print (nano)
    s=input('\033[1;37mꪶŌssꫂ...... ᵈᶻ >')
    if s =='1':
        print(ins)
        os.system(apt)
        os.system('git clone https://github.com/Gameye98/Lazymux')
        os.system('mv Lazymux ~')
        print('Lazymux is installed Done...! ')
    elif s =='2':
        print (ins)
        os.system(apt)
        os.system('git clone https://github.com/rajkumardusad/Tool-X')
        os.system('mv Tool-X ~')
        print ('Tool-X is installed Done...!')
    elif s == '3':
        print (ins)
        os.system(apt)
        os.system('git clone https://github.com/Vairous7x/V7x-Tool')
        os.system('mv V7x-Tool ~')
        print ('V7x-Tool is Installed Done..!')
    elif s == '4':
        print (ins)
        os.system(apt)
        os.system('git clone https://github.com/Anonime7x/fuckadmin')
        os.system('mv fuckadmin ~')
        print ('Fuck Admin is installed Done..!')
   
    else:
        print ('Error..!'*100)
        restart_program()
    backtomenu_option()
