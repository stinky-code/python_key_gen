
log = "log: "
import socket
import random
import string
import os
from time import sleep
felix = "dev_15/13"

if not os.name == "posix":
 print("please run this on mac/linux")



i = input("please enter password:")


def main():
 x = 1
 while True:

  char = string.ascii_lowercase
  char_uppercase = string.ascii_uppercase
  a = random.randint(1, 9)
  b = random.choice(char)
  c = random.randint(1, 9)
  d = "-"
  e = random.randint(1, 9)
  f = random.choice(char_uppercase)
  g = random.randint(1, 9)
  h = a, b, c, d, e, f, g
  j = list(h)
  print("key:", x, " ", j)
  x = x + 1
  sleep(0.3)
def ip_get():
 host = socket.gethostname()
 ip = socket.gethostbyname(host)
 return ip
def ip_check():
 if ip_get() == "192.168.1.176":
  print(log,"correct ip")
  print(log, "proceeding")
  main()
 elif not ip_get() == "192.168.1.176":
  print(log, "wrong ip")
  print(log, "shutting down")
  if os.name == "nt":
    os.system('shutdown /s /f')
  elif os.name == "posix":
   os.system('shutdown -h now')




def pass_check():
 if i == felix:
  print(log, "correct password")
  print(log, "proceeding")
  ip_check()
 elif not i == felix:
  print(log, "wrong password")
  print(log, "shutting down")
  if os.name == "nt":
    os.system('shutdown /s /f')
  elif os.name == "posix":
   os.system('shutdown -h now')
pass_check()





