import datetime
now = datetime.datetime.now()

name = input("What is your name?\n")
allowedUsers = ['Seyi','Mike','Love']
allowedPassword = ['PasswordSeyi','PasswordMike','PasswordLove']

if(name in allowedUsers):
	password = input("Your Password?\n")
	userId = allowedUsers.index(name)

	if(password == allowedPassword[userId]):
		print("Welcome %s" % name)
		print( "Today is: ", now)
		print("These are the available options: ")
		print("1. Withdrawal")
		print("2. Cash Deposit")
		print("3. Complaint")

		selectedOption = int(input("Please select an option: "))

		if(selectedOption == 1):
			print("You selected %s" % selectedOption)
			withdraw = int(input("How much would you like to withdraw?\n"))
			balance = 5000

			if (withdraw < balance):
				print("Take your cash: ", withdraw)
			else:
				print("You do not have enough credit in your account. Please try a lower ammount or make a deposit.")

		elif(selectedOption == 2):
			print("You selected %s" % selectedOption)
			deposit = int(input("How much would you like to deposit?\n"))
			balance = 5000
			bank = deposit + balance
			print("Your total bank balance is: ", bank)

		elif(selectedOption == 3):
			print("You selected %s" % selectedOption)
			complaint =  input("What issue will you like to report?")
			print("Thank you for contacting us.")

		else:
			print("Invalid option selected, Please try again!")

	else:
		print("Password Incorrect, Please try again!")

else:
	print("Name not found, Please try again!")
