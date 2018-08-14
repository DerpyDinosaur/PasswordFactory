import hashlib

# Entry Function
# def createPassword(password, length):
# 	return hashlib.sha256(password.encode()).hexdigest()[:length]

# Extention Function
def createPassword(password, length):
	salt = input("\nEnter some characters to make some salt: ")
	length = int(length - len(password))

	saltHash = hashlib.sha256(salt.encode()).hexdigest()[:length]

	return password + saltHash + "\nKey used = " + salt


while True:
	# Welcome MOTD
	print(50 * "/")
	print("Welcome To The Password Factory")
	print(50 * "/")

	# User Input
	masterPass = input("\nPlease enter a basic short password: ")
	passwordLen = input("\nHow many characters would you like, it is better if they are even: ")

	# Make sure user has not used a string
	try:
		# This attempts to make an INT rather
		# Than using it as a STRING
		passwordLen = int(passwordLen)
	except ValueError:
		# This will reset the loop to the beggining
		print("\n")
		continue

	# Call create password function
	saltPass = createPassword(masterPass, passwordLen)

	# Print out new password
	print("\nHere is your new password")
	print("\n" + saltPass)

	# Check if user would like to repeat again
	repeat = input("\nWould you like to make another password: ").lower()
	if repeat in ["n", "no"]:
		break
