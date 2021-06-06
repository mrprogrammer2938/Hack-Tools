# hackingmenu
# This code write by (Mr.nope)
# version 1.0.0
import os
import time
import sys
class color:
    green = '\033[92m'
    red = '\033[91m'
    blue = '\033[96m'
    End = '\033[0m'
    darkblue = '\033[34m'
    org = '\033[33m'
# choose
def cls():
    os.system("clear")
def menu():
    os.system("printf '\033]2;Hacking Menu\a'")
    cls()
    print(color.red + """
      ( (   (   (  (      )    ) :            ) )  )    (   
     )\)\: )\  (\ )\  ( ((.  ()))      ( (  (\(  ((.   )\  
    (_)(_)(_() (\((_) )\))\ ()(())     )\)\  )(| ))\  ((_) 
    | || |(_)()( ) |___)(_))/ _` |    (_((_) ()\((_))((_)) 
    | __ | _` | _| / / | ' \)__. |    | '  \/ -_) ' \) || |
    |_||_|__/_|__|_\_\_|_||_|___/     |_|_|_|___|_||_|\_._|
    
    (【H】【a】【c】【k】【i】【n】【g】   【m】【e】【n】【u】)
""")
    print(color.red + "\t{1}."+color.blue+"Testweb" , color.red + "\t \t {2}."+color.blue +"fsociety")
    print(color.red + "\t{3}."+color.blue+"brutex", color.red + "\t \t {4}."+color.blue +"phsihmailer")
    print(color.red + "\t{5}."+color.blue+"cupp",color.red + "\t \t {6}."+color.blue+"soial-Enginners-setoolkit")
    print(color.red + "\t{7}."+color.blue+"hackingtool" ,color.red + "\t {8}."+color.blue+"cam-hackers")
    print(color.red + "\t{9}."+color.blue+"Help" ,color.red + "\t \t {10}."+color.blue+"Exit")
    choose = input(color.green + "\nHacker/> " + color.End)
# working
    if choose == '1':
      cls()
      os.system("figlet Testweb")
      os.system("git clone https://github.com/msprogrammer2938/testweb")
      try1 = input("\npress Enter... ")
      if try1 == '':
          menu()
      else:
          menu()
    elif choose == '2':
        cls()
        os.system("figlet fsociety")
        os.system("git clone https://github.com/Manisso/fsociety")
        time.sleep(1)
        print("\nfinish !")
        try2 = input("\npress Enter... ")
        if try2 == '':
          menu()
        else:
            menu()
        
    elif choose == '3':
       cls()
       os.system("figlet brutex")
       os.system("git clone https://github.com/1N3/brutex")
       time.sleep(1)
       print("finish!")
       try3 = input("\npress Enter...")
       if try3 == '':
         menu()
       else:
           menu()
    elif choose == '4':
        cls()
        os.system("figlet phishmailer")
        os.system("git clone https://github.com/BiZken/PhishMailer/ phishmailer/")
        try4 = input("\npress Enter... ")
        if try4 == '':
          menu()
        else:
             menu()
    elif choose == '5':
        cls()
        os.system("figlet cupp")
        os.system("git clone https://github.com/Mebus/cupp")
        time.sleep(1)
        print("finish")
        try5 = input("\npress Enter... ")
        if try5 == '':
           menu()
        else:
            menu()
    elif choose == '6':
        cls()
        os.system("figlet set")
        os.system("git clone https://github.com/trustedsec/social-engineer-toolkit/ set/")
        time.sleep(1)
        print("finish!")
        try6 = input("\npress Enter... ")
        if try6 == '':
          menu()
        else:
            menu()
    elif choose == '7':
        cls()
        os.system("figlet hachingtool")
        os.system("git clone https://github.com/Z4nzu/hackingtool")
        time.sleep(1)
        print("\nfinish!")
        try7 = input("\npress Enter... ")
        if try7 == '':
           menu()
        else:
            menu()
    elif choose == '8':
        cls()
        os.system("figlet cam Hackers")
        os.system("git clone https://github.com/AngelSecurityTeam/Cam-Hackers/ camhackers/")
        time.sleep(1)
        print("\nfinish!")
        try8 = input("\npress Enter... ")
        if try8 == '':
           menu()
        else:
             menu()
    elif choose == '9':
        cls()
        print(color.green + """
This code write by (ms.nope)
usage:
     1 - and install testweb
     2 - and install fsociety
     3 - and install brutex
     4 - and install phishmailer
     5 - and instal cupp
     6 - aad install cupp))
     7 - and install hackingtool
     8 - and install camhackers
     9 - and install informtions package !
     10 - Exit package !
""" + color.End)
        try9 = input(color.red + "press Enter... " + color.End)
        if try9 == '':
          menu()
        else:
            menu()
    elif choose == '10':
        cls()
        print(color.green + "Exiting..." + color.End)
        exit()
# Commands
    elif choose == 'developer':
        cls()
        print(color.org)
        os.system("figlet Ms.nope")
        print(color.End)
        print(color.green + "(" + color.red + "This code write by" + color.blue + " Ms.nope" + color.green + ")" + color.End)
        print("\nGithub: " + color.darkblue + "https://github.com/msprogrammer2938" + color.End)
        print("\nInstagram: " + color.red + "https://instagram.com/programmer2938" + color.End)
        time.sleep(2)
        try10 = input("\npress Enter...")
        if try10 == '':
          menu()
        else:
            menu() 
    elif choose == 'exit':
        exit()
    elif choose == 'quit':
        exit()
    elif choose == 'neofetch':
        cls()
        print("""
      ( (   (   (  (      )    ) :            ) )  )    (   
     )\)\: )\  (\ )\  ( ((.  ()))      ( (  (\(  ((.   )\  
    (_)(_)(_() (\((_) )\))\ ()(())     )\)\  )(| ))\  ((_) 
    | || |(_)()( ) |___)(_))/ _` |    (_((_) ()\((_))((_)) 
    | __ | _` | _| / / | ' \)__. |    | '  \/ -_) ' \) || |
    |_||_|__/_|__|_\_\_|_||_|___/     |_|_|_|___|_||_|\_._|""")
        try11 = input("\npress Enter... ")
        if try11 == '':
          menu()
        else:
            menu()
# try to menu
    elif choose == '':
        menu()
    elif choose == ' ':
        menu()
    elif choose == '  ':
        menu()
    else:
        cls()
        print(color.red + "Error 532 !" + color.End)
        time.sleep(1)
        try12 = input(color.green + "\npress Enter... " + color.End)
        if try12 == '':
          menu()
        else:
             menu()
if __name__ == '__main__':
  try:
     menu()
  except KeyboardInterrupt:
      print("\nCtrl + C")
      print("Exiting...")
      sys.exit()
# hackingmenu
