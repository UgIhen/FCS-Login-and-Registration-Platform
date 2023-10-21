''' Import necessary function(s) from checkEmail.py file '''
from checkEmail import checked_email, check_password

'''Define global variables '''
userNames = []
userEmails = []
userPasswords = []

""" Define the required registration function """
def register(): 
    print("Username")
    user_name = input("Please enter a user name: ")

    while user_name in userNames:
        print("This username has already been take, please try again")
        print("Username")
        user_name = input("Please enter a user name: ")

    while True: #This tells the program that as long as it is still on the present user_name, run the blocks of code below
        print("Email Address")
        user_email = input("Please input a valid email address: \n") 

        while user_email in userEmails: 
            print("This username has already been take, please try again")
            print("Email Address")
            user_email = input("Please input a valid email address: \n") 

        if checked_email(user_email):
            while True: #This tells the program that while still on the current verified user_email, run the blocks of code below
                print("Password")
                user_password = input("Must be greater than 6 characters and have at least one symbol and one number : \n") 
                if check_password(user_password): 
                    if user_name not in userNames:
                        if user_email not in userEmails:
                            userNames.append(user_name)
                            userEmails.append(user_email)
                            userPasswords.append(user_password)
                            print("Account created successfully")

                            '''The below lines of code up to print("Password:", userPasswords[-1]) (line 43 to 45) can be deleted. 
                            It is just used to show the accurate credentials that were appended last, can be edited to see all appended 
                            credentials. ''' 
                            print("Username:", userNames[-1])
                            print("Email:", userEmails[-1])
                            print("Password:", userPasswords[-1])
                            return
                        else: 
                            print("This useremail has already been taken")
                            break
                    else: 
                        print("This username has already been taken")
                        break
                else: 
                    print("Kindly confirm password is greater than or equal to 6 characters. ")
                    

        else: 
            print("Email Invalid")
            continue #This will enable us to leave this else block and go back to the outer loop which will keep prompting user to enter a valid email


register()

