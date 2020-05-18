import os
os.system ("clear")
from V7xStyle import *
from time import *
import random
from Sofiane import *
#############################################
an=Animation
logo=Style("""
   G#   ╔═╗────╔╗────╔╗─  ─╔╗────  ╔═╗╔╗────────────
  G#    ║╬║╔═╗─║╚╗╔═╗║╚╗  ╔╝║╔═╗─  ║═╣╠╣╔╗─╔═╦═╗╔═╗─
   G#   ║╗╣║╬╚╗║╬║║╩╣║║║  ║╬║║╬╚╗  ╠═║║║║╚╗╚╗║╔╝║╬╚╗
   G#   ╚╩╝╚══╝╚═╝╚═╝╚╩╝  ╚═╝╚══╝  ╚═╝╚╝╚═╝─╚═╝─╚══╝
   G#   ────────────────  ───────  ─────────────────
                                                   Y#  BY:Sofiane✓""").Square(Equal=True)
#############################################
sleep(1)
os.system("clear")
#############################################
an.SlowIndex(logo,t=0.002)
ls = Style(
	"Y#{1} C#Social Engineering",

	"Y#{2} C#DOS,DDOS Attacks",
	
	"Y#{3} C#Linux Distro",

	"Y#{4} C#Password Generator",
	
	"Y#{5} C#Web Hacking",
	
	"Y#{6} C#Other Tools"
).Square(cols=2,
        Equal=True,
        space=2,
        padding_x=4,
        padding_y=1)
cd= Style('Y#[7]P# ☬⫷🄲 🄾 🄼 🄸 🄽 🄶  🅂 🄾 🄾 🄽⫸☬  ').Square(Equal=True,padding_x=17)       

    
an.SlowIndex(ls, t=0.0007) 
print(cd)
t3 =an.SlowText("\033[1;39m ꪶŌssꫂ...... ᵈᶻ > ")
num = input ()
#################################
if   num == '1':social_engineering() 
elif num == '2':DDos_Attack()
elif num == '3':Linux_Distro()
elif num == '4':Password_List()
elif num == '5':web_Hacking()
elif num == '6':other()
elif num == '7':
   os.system('git clone https://github.com/mcsofiane123/B-R-I-')
else:
    print ('Error...!'*100)
    sleep (1)
    os.system('clear')
    backtomenu_option()
    os.system('clear')

