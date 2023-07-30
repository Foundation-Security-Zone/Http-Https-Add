import os
import sys
import time

os.system("clear")

print("\033[32;1m ")
os.system(" figlet HTTP/HTTPS ADD")
print("==========================")
print("1)HTTP://")
print("2)HTTPS://")
print("3)HTTP://www")
print("4)HTTPS://www")
print("5)About Tools")
print("6)Exit")
print("==========================")
select = input("Please Select:")
if select == "1":
	HTTP1 = input("Please Make Example google.com: ")
	print("Wait......")
	time.sleep(3)
	print("========================")
	print("your make: " "http://" + HTTP1)
	print("========================")
elif select == "2":
	HTTPS2 = input("Please Make Example google.com: ")
	print("Wait......")
	time.sleep(3)
	print("==========================")
	print("your make: " "https://" + HTTPS2)
	print("==========================")
elif select == "3":
	HTTP3 = input("Please Make Example google.com: ")
	print("Wait......")
	time.sleep(3)
	print("==========================")
	print("your make: " "http://www." + HTTP3)
elif select == "4":
	HTTPS4 = input("Please Make Example google.com: ")
	print("Wait......")
	time.sleep(3)
	print("==========================")
	print("your make: " "https://www." + HTTPS4)
	print("==========================")
elif select == "5":
	print("This Tools For Add Https In Url Link")
elif select == "6":
	print("GOOD BYE!")