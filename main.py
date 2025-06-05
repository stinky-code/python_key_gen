
log = "log: "
import socket
import random
import string
import os
from time import sleep
dev1 = "dev_15/13"
guest = "guest"






def main():
 
 p = input("input number of keys generated ")
 x = 1
 k = int(p) + 1
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
  if x >= int(k):
     break


def pass_check():
 i = input("please enter password (enter guest if not dev) ")
 if i == dev1:
  print(log, "correct password")
  print(log, "proceeding")
  main()
 elif i == guest:
    print("welcome guest")
    main()
 elif not i == guest or dev1:
   print("wrong password")
pass_check()
