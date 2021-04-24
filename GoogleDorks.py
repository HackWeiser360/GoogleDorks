#!/usr/bin/env/python3
# This Python file uses the following encoding: utf-8

# Author: HackWeiser360(MådMâx)
# Github: Github.com/HackWeiser360
# Twitter: Twitter.com/503_madmax
# Instagram: Instagram.com/madmax4708
# If you copy or use any part of this program give HackWeiser360 the credits they deserve



from __future__ import print_function
try:
    from googlesearch import search

except ImportError:
    print("")

import sys
import time


# GoogleDorks v1.0


if sys.version[0] in "2":
    print ("\n[x]  GoogleDorks Is Not Supported For python 2.x Use Python 3.x \n")
    print ("\n\n\tGoogleDorks \033[1;91mI like to see you hacking boy \033[0m😃\n\n")
    exit()


class colors:
    CRED2 = "\33[91m"
    CBLUE2 = "\33[94m"
    ENDC = "\033[0m"


banner = ("""

  ____                   _        ____             _
 / ___| ___   ___   __ _| | ___  |  _ \  ___  _ __| | _____
| |  _ / _ \ / _ \ / _` | |/ _ \ | | | |/ _ \| '__| |/ / __|
| |_| | (_) | (_) | (_| | |  __/ | |_| | (_) | |  |   <\__ \
  \____|\___/ \___/ \__, |_|\___| |____/ \___/|_|  |_|\_\___/
                   |___/    
      
        
          
            
              
                  v1.0 """)


for col in banner:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0025)

x = ("""
                Github: Github.com/HackWeiser360
                Twitter: Twitter.com/503_madmax
                Instagram: madmax4708 \n """)
for col in x:
    print(colors.CBLUE2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

y = "\n\t\tHi there. Let's play a game😈\n"
for col in y:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

z = "\n"
for col in z:
    print(colors.ENDC + col, end="")
    sys.stdout.flush()
    time.sleep(0.4)


try:
    data = input("\n[+] Do You Like To Save The Output In A File? (Y/N) ").strip()
    l0g = ("")

except KeyboardInterrupt:
        print ("\n")
        print ("\033[1;91m[!] User Interruption Detected..!\033[0")
        time.sleep(0.5)
        print ("\n\n\t\033[1;91m[!] Follow us on github for more tools \033[0m😃\n\n")
        time.sleep(0.5)
        sys.exit(1)


def logger(data):
    file = open((l0g) + ".txt", "a")
    file.write(str(data))
    file.write("\n")
    file.close()


if data.startswith("y" or "Y"):
    l0g = input("[~] Give The File a Name: ")
    print ("\n" + "  " + "»" * 78 + "\n")
    logger(data)
else:
    print ("[!] Saving is Skipped...")
    print ("\n" + "  " + "»" * 78 + "\n")


def dorks():
    try:
        dork = input("\n[+] Enter The Dork Search Query: ")
        amount = input("[+] Enter The Number Of Websites To Display: ")
        print ("\n ")

        requ = 0
        counter = 0

        for results in search(dork, tld="com", lang="en", num=int(amount), start=0, stop=None, pause=2):
            counter = counter + 1
            print ("[+] ", counter, results)
            time.sleep(0.1)
            requ += 1
            if requ >= int(amount):
                break

            data = (counter, results)

            logger(data)
            time.sleep(0.1)

    except KeyboardInterrupt:
            print ("\n")
            print ("\033[1;91m[!] User Interruption Detected..!\033[0")
            time.sleep(0.5)
            print ("\n\n\t\033[1;91m[!] Don't use me for illegal purposes \033[0m🤒\n\n")
            time.sleep(0.5)
            sys.exit(1)

    print ("[•] Done... Exiting...")
    print ("\n\t\t\t\t\033[34mGoogleDorks\033[0m")
    print ("\t\t\033[1;91m[!] Follow on Instagram \033[0m😃\n\n")
    sys.exit()


# =====# Main #===== #
if __name__ == "__main__":
    dorks()