'''Define global variables '''
# symbols = "@"
domains = ["gmail.com", "yahoo.com", "hotmail.com", "yahoo.co.za"]
other_symbols = ["!", "£", "%", "^", "&", "(", ")", "/", "<", ">", "?", "#", "~", "*", "_", "-", "+", "=", "[", "]", "@", "'"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

""" Define the required email check function """
def checked_email (email):
    if "@" in email: #This will ensure that the email contains the "@" symbol 
        for domain in domains: #This takes one domain at a time from the domain list, i.e. it loops through domain list
            if domain in email: #For each domain, it checks if its present in the email, that way it ascertains the email is valid. 
                return True #If the email is valid, it will return True
            
    return False #If the email is not valid, it returns False.


def check_password (password): 
    # The password has to be greater than 6 characters, contain at least one symbol and contain at least one number
    # The numbers list will be converted to str type because a user input is interpreted as a string.
    if len(password) >= 6 and any(symbol in password for symbol in other_symbols) and any(number in password for number in str(numbers)):
        return True 
    return False