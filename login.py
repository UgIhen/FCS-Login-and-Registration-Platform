''' Import necessary function(s) and lobal variables from registration.py file '''
from registration import register 
from registration import userEmails 
from registration import userPasswords 
from registration import userNames


""" Define the required login function """
def login(): 
    print("\n")
    print("Login session")
    
    user_email_attempts = 3
    while user_email_attempts > 0:
        print("Email Address")
        user_email = input("Please input a valid email address: \n") 
        if user_email.lower() in userEmails: 
            break #This enables the program to leave the if-else block and proceeds to the next block i.e. the password block.
        else:
            user_email_attempts -= 1
            print("Attempting to login, Incorrect Email")

            if user_email_attempts == 0:
                print("You do not have an email with Us, kindly register.")
                register() 
                login()
    password_attempts = 3 
    while password_attempts > 0: 
        print("Password")
        user_password = input("Please enter your password: \n")
        index1 = userEmails.index(user_email) 

        if user_password == userPasswords[index1]: 
            print("Welcome", userNames[index1])
            exit()
        else:
            password_attempts -= 1 # This is the same as writing "password_attempts = password_attempts - 1"
            print("Incorrect username/password", password_attempts, "attempts remaining") 
            
            # Once the password attempts is = 0, the program leaves this else loop and proceed to the next line.
    print("Password exceeded limit. Please retrieve your password") 
    register()
    login()

login()