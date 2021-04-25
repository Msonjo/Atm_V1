import os
import bank

path_to_database = "data/user_record/"

def create(Account_No, F_name, L_name, Email, PassWord):
	member_record = F_name + ", " + L_name + ", " + Email + ", " + PassWord + ", " + str(0)

	if bank.is_account_exist(Account_No):
		return False

	if bank.is_email_exist(Email):
		print("User already exists!")
		return False

	completion_state = False

	try:
		f = open(path_to_database + str(Account_No) + ".txt", "x")

	except FileExistsError:
		is_file_data_present = read(path_to_database + str(Account_No) + ".txt")
		if not is_file_data_present:
			delete(Account_No)

	else:
		f.write(str(member_record));
		completion_state = True

	finally:
		f.close();
		return completion_state

def delete(Account_No):
	is_delete_true = False

	if os.path.exists(path_to_database + str(Account_No) + ".txt"):

		try:
			os.remove(path_to_database + str(Account_No) + ".txt")
			is_delete_true = True

		except:
			print("User not found")

		finally:
			return is_delete_true
