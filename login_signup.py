#Create a simple version of Projectube
#When run program:
#1. Use program
#2. Stop program
#If user choose 2 stop program immediately
#If user choose 1:
#1. User
#2. Orgination
#Then even user choose 1 or 2:
#1. Sign in 
#2. Sign up
#If user choose 1:
# Email: 
# Password:
#If email and password is not correct ask email and password again
#If user choose 2:
# Email:
# Password:
# Confirm password:
#If 2 passowrd is not the same ask email and 2 password again
#After user login as a User
#1. See events
#2. See orgs
#If user choose 1 list all current events with their number
#If user choose number print decriptions of this events
#If user choose 2 list all current organizations with their number
#If user choose number print decriptions of this organization
#Then:
#1. Continue to see 
#2. Logout
#If user choose 1 return to ask see events or see orgs
#If user choose 2 return to ask use program or stop program
#after user login as a Organization
#If this organation is new ask their description
#After that
#1. See events
#2. See orgs
#3. Create events
#If user choose 1 or 2 will be the same action above
#If use choose 3
#Ask how many events want to add (maximum 5)
#Then ask name of events and description
#Then:
#1. Continue to see or creaete event
#2. Logout
#If user choose 1 return to ask see events or see orgs or create events
#If user choose 2 return to ask use program or stop programs
def sign_in(accounts):
    while(True):
        email=input('Enter your email: ')
        password=input('Enter your password: ')
        if email not in accounts:
            print('Your account doese not exist. Please try again!')
        else:
            if accounts[email]!=password:
                print('Your password is not correct. Please try again!')
            else:
                break
def sign_up(accounts):
    while(True):
        while(True):
            email=input('Enter your email: ')
            if email in accounts:
                print('Your email exited. Please try another email.')
            else:
                break
        password=input('Create your password: ')
        confirm=input('Confirm your password: ')
        if confirm!=password:
            print('Your password does not match. Please try again!')
        else:
            accounts[email]=password
            
            break
accounts={'phananh12042003':'khongmatkhau','pinkmay2005':'123','khanhha':'hello'}



# while(True):
#     print("""
#     #1. Use program
#     #2. Stop program
#     """)
#     use_program=input('Choose your option(1 or 2): ')
#     if use_program=="2":
#         break
#     else:
#         user_action=input('Sign in or sign up(1 or 2): ')
#         if user_action=='1':
#             sign_in(accounts)
#         else:
#             sign_up(accounts)
#         print(    
#     """
# #1. User
# #2. Orgination
# """)
#         role=input('Choose your role(1 or 2): ')
#         if role=="1":
#         else:
