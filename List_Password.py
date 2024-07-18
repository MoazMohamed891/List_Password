import os
import sys
import time
import random
#######################################
print ("\033[31m")
os.system("figlet Hallo To Moaz Mohamed script")
time.sleep(3)
os.system("clear")
print ("\033[32m")
os.system("figlet List Password")


print ("\033[35m")
print ("BY.Moaz Mohamed")
print ("\033[36m")
print ("Github : https://github.com/MoazMohamed891")
print ("Linkedin : https://www.linkedin.com/in/moaz-mohamed-10b807318")

print ("\033[33m---------------------------------------------------------------------------------")
#####################################
print ("\033[1;37m")
a = input("Enter Name :\033[1;31m ")
l = a.lower()
print ("\033[1;37m")
m = input("Enter Age :\033[1;31m ")
print ("\033[1;37m")
x = input("Enter Your Number :\033[1;31m ")
print ("\033[1;34m")
###################################
upper, lower, nums, nums = True, True, True, True

all = ""

if upper:
    all += a
if lower:
     all += l
if nums:
     all += m
if nums:
    all += x

el = 10

am = 100

for x in range(am):
       password = "".join(random.sample(all, el))
       print (password)
