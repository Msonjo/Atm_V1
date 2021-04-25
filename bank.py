import database
import random

def __init__():
	print("____________________Welcome at ASILI BANK____________________\n")
	member_login = int(input("Do you have an account with ASILI BANK: 1 for (yes) or 2 for (no)\n"))

	if member_login == 1:
		login_member()
	elif member_login == 2:
		register_member()
	else:
		print("Invalid option. Try again")

def register_member():
	print("______________Member Registration at ASILI BANK______________\n")
	F_name = input("Enter your first name:\n")
	L_name = input("Enter your last name:\n")
	Email = input("Enter your email:\n")
	PassWord = input("Enter your new password:\n")
	Account_No = Account_No_Generator()

	is_member_registered = database.create(Account_No, F_name, L_name, Email, PassWord)

	if is_member_registered:
		print("Your account has been successfully created.")
		print("_____________________________________________________________")
		print("This is your account number: %d" %Account_No)
		login_member()

	else:
		print("An error occured while generating your account number. Please try again")
		register_member()

def Account_No_Generator():
	return random.randrange(1111111111, 9999999999)

#def database_creation(Account_No, F_name, L_name, Email, PassWord):
#	member_record = F_name + "," + L_name + "," + Email + "," + PassWord + "," + str(0)

	#if Account_No_Exists(Account_No):
	#	return False

	#if Email_Exists(Email):
	#	print("The user already exists!")
	#	return False

	#completion_state = False

	#try:
#	f = open(path_to_database + str(Account_No) + ".txt", "x")

	#except FileExistsError:
	#	is_file_empty = read(path_to_database + str(Account_No) + ".txt", "x")
	#	if not is_file_empty:
	#		delete(Account_No)

#	else:
#		f.write(str(member_record));
#		completion_state = True
#
#	finally:
#	f.close();
#		return completion_state

def read(Account_No):
	is_check_validity = validity(Account_No)

	try:
		if is_check_validity:
			f = open(path_to_database + str(Account_No) + ".txt", "r")
		else:
			f =open(path_to_databse + Account_No + ".txt", "r")

	except File_Not_Found:
		print("The user has not been found!")

	except File_Not_Found:
		print("The user does not exist!")

	except TypeError:
		 print("Invalid account number format!")

	else:
		return f.readline()

	return False

def login_member():
	Account_No = input("What is your account number?\n")
	validity_check = validity(Account_No)

	if validity_check:
		PassWord = input("What is your password?\n")
		members = rightful_user(Account_No, PassWord);

		if members:
			bank_operations(members)
			print("Invalid account or password")
			login_member()

		else:
			print("Account number is invalid check and retry!")
			__init__()

def bank_operations():
	print("This are the available options")
	print("1. Withdraw")
	print("2. Deposit")
	print("3. Transfer")
	print("4. Complaints")

	selected_options = int(input("Please select an option:\n"))

	if (selected_option == 1):
		withdraw = input("How much would you like to withdraw?\n")

	elif (selected_option == 2):
		deposit = input("How much would like to deposit?\n")

	elif (selected_option == 3):
		transfer = input("How much would you like to transfer?\n")

	elif (selected_option == 4):
		complaint = input("what is your complaint?\n")

def validity(Account_No):
	if Account_No:
		try:
			int(Account_No)

			if len(str(Account_No)) == 10:
				return True

		except ValueError:
			return False

		except TypeError:
			return False

	return False

def is_account_exist(Account_No):
	all_members = os.listdir(path_to_database)

	for members in all_members:

		if members == str(Account_No) + ".txt":
			return True
	return False

def is_email_exist(Email):
	all_members = os.listdir(path_to_database)

	for members in all_members:
		member_record = str.split(read(members))
		if Email in member_record:
			return True

	return False

def rightful_user(Account_No, PassWord):
	if is_account_exist(Account_No):
		members = str.split(read(Account_No), ',')

		if PassWord == members[3]:
			return members

	return False


__init__()
