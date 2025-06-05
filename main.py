
log = "log: "
import socket
import random
import string
import os
from time import sleep
felix = "dev_15/13"




i = input("please enter password:")


def main():

 p = input("input number of keys generated ")
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
  if x => p
     break




def pass_check():
 if i == felix:
  print(log, "correct password")
  print(log, "proceeding")
  main()
 elif not i == felix:
  print(log, "wrong password")
  print(log, "shutting down")
  if os.name == "nt":
    os.system('shutdown /s /f')
  elif os.name == "posix":
   os.system('shutdown -h now')
pass_check()





