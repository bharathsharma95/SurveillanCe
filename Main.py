import os
import getpass
from datetime import datetime

def greetings():
	print("This will be the entry point...")
	currUser = str(input("Hi there..!!\nUse your username to login: "))
	#print("peekav eekala katta --> ive thaggichukunte manchidi")
	user = getpass.getuser()
	if(user==currUser):
		password = getpass.getpass("what's your password: ")
		print("Uid: {}\npswd: {}".format(currUser, password))
		#if(pwd==password):
			#main()
	else:
		print("Hard luck yo, exiting the program...\n\n")
		exit()

def main():
	print("Inka modalu...")



if __name__ == "__main__":
	greetings()
