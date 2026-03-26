# Simple Password Authentication Program
# This program checks whether the entered password is correct
# and also ensures the password has at least 8 characters.

# Stored password (assumed to be already set by the system)
stored_password = "Admin@123"

# Asking the user to enter their password
entered_password = input("Please enter your password: ")

# First check: password length
if len(entered_password) >= 8:
    
    # Second check: whether it matches the stored password
	if entered_password == stored_password:
        print("Access Granted. Welcome!")
	else:
		print("The password you entered is incorrect.")

else:
    print("Password must contain at least 8 characters.")