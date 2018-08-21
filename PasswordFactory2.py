import hashlib
import random

while True:
	# Welcome MOTD
	print(50 * "/")
	print("Welcome To The Password Factory")
	print(50 * "/")

	# User Input
	masterPass = input("\nPlease enter a basic short password: ")
	passLength = input("\nHow many characters would you like: ")
	website	= input("\nWhat website is this password for (eg. facebook.com): ")

	# Make sure user has not used a string
	try:
		# This attempts to make an INT rather
		# Than using it as a STRING
		passLength = int(passLength)
		passLength = int(round(passLength / 2))
	except ValueError:
		# This will reset the loop to the beggining
		print("\n")
		continue

	# Create Password
	hashPass = hashlib.sha256(masterPass.encode()).hexdigest()[:passLength]
	hashWebsite = hashlib.sha256(website.encode()).hexdigest()[:passLength]
	saltPass = hashPass + hashWebsite

	# Print out new password
	print("\nHere is your new password")
	print("\n" + saltPass)

	# Check if user would like to repeat again
	repeat = input("\nWould you like to make another password: ").lower()
	if repeat in ["n", "no"]:
		break