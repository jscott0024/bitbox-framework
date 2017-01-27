import os
import sys
import time
import socket

def main():
	os.system("clear")
	print("[*] BitBox is loading...")
	time.sleep(5)
	bitbox()

def bitbox():
	os.system("clear")
	print('''

BBBBBBBBBBBBBBBBBB  OOOOOO    TTTTTT    BBBBBBBBBBBBBBBBBB  OOOOOOOOOOOOOOOO XXXXX    XXXXX
BB               BB OO  OO    TTTTTT    BB               BB OO            OO  XXXX    XXXX
BB               BB OOOOOO    TTTTTT    BB               BB OO            OO   XXX   XXX       {v1.0}
BB               BB IIIIII TTTTTTTTTTTT BB               BB OO            OO    XXX XXX
BBBBBBBBBBBBBBBBBB  IIIIII TTTTTTTTTTTT BBBBBBBBBBBBBBBBBB  OO            OO       X
BB               BB IIIIII    TTTTTT    BB               BB OO            OO    XXX XXX
BB               BB IIIIII    TTTTTT    BB               BB OO            OO   XXX   XXX
BB               BB IIIIII    TTTTTT    BB               BB OO            OO  XXXX   XXXX
BBBBBBBBBBBBBBBBBB  IIIIII    TTTTTT    BBBBBBBBBBBBBBBBBB  OOOOOOOOOOOOOOOO XXXXX   XXXXX

                           Type 'help' for commands

''')
	print("")
	main = raw_input("BitBox> ")
	if "xip" in main:
		ip()
	elif "xdos" in main:
		doss()
	elif "help" in main:
		help()
	elif "exit" in main:
		os.system("clear")
		sys.exit()

def ip():
	print("")
	print("Type in a url")
	print("")
	url = raw_input("BitBox(xip)> ")
	print("")
	ip = socket.gethostbyname(url)
	print("IP for " + url + ": " + ip)
	time.sleep(5)
	bitbox()

def doss():
	print("")
	print("Type in a url or ip")
	print("")
	urlip = raw_input("bitbox(xdos)> ")
	print("")
	os.system("sudo ping -f " + urlip)
	time.sleep(3)
	bitbox()

def help():
	print("")
	print("Commands: xip, xdos, help, exit")
	print("")
	raw_input("Press 'enter'...")
	bitbox()

main()
