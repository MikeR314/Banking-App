"""
TASK: Design a safe banking app.
The new system should allow users to perform common banking operations like
checking balances, transferring funds between accounts, and depositing or
withdrawing money. However, with the convenience of online banking comes the
responsibility of ensuring transactions are error-free and secure. For instance, a
user shouldn't be able to transfer negative amounts or over-withdraw beyond
their account balance.
"""

# Create a dictionary for user details, from a saved txt file "userinfo"
# This file shows info as: USERNAME,PASSWORD,BALANCE

# Start two new blank dictionaries, one for user/password and one for user/balance
users_pw = {}
users_bal = {}
file = open("userinfo.txt","r")

# Loop through the file and add lines to the dictionary
for lines in file :

    # Remove any excess spaces with strip, and split by the comma
    temp = lines.strip().split(",")
    
    user = temp[0]
    passw = temp[1]
    bal = float(temp[2])
      
    users_pw[user] = passw
    users_bal[user] = bal

# Now the users and passwords are saved in the dictionary "users_pw"
# And the users and balances are saved in the dictionary "users_bal"
    
# Add a dummy value to the user/password dictionary, to use as an escape
users_pw["x"] = "x"
    
# Ask user to enter their username or x to escape
user_name = input("Please enter your username, or type 'x' to exit : ").lower()

# Use a while loop to repeat through until a username from the dictionary is entered
while user_name not in users_pw.keys() :
    user_name = input("Invalid username, please try again, or type 'x' to cancel : ").lower()
        
# Ask user to enter a password
pass_word = input("Please enter your password, or type 'x' to cancel : ")

# Use a while loop to repeat until the correct password for that user is entered
while pass_word != users_pw[user_name] :
    pass_word = input("Invalid password, please try again, or type 'x' to cancel : ")

# Display the leaving message if they terminated with an x, or a welcome message if not.
if user_name == "x" :
    print("Session Terminated. Thank you")

else :
    print(f"\nWelcome to the SafeBank App {user_name.capitalize()}")
    
    # Everything from here down still needs to be in the else statement
    # Define a new variable called service
    service = 0

    while service != "5" :
        service = input(f"""
        What service would you like to use today {user_name.capitalize()}?
          
        1. See your balance
        2. Make a payment
        3. Withdraw money
        4. Deposit money
        5. Log out

        Please select a value 1,2,3,4 or 5
        Remember to log out when you are finished
          
        """)
    
        # Option for seeing balance
        if service == "1" :

            # Print the correct balance using the dictionary defined at the start
            print(f"{user_name.capitalize()}, your current balance is £{users_bal[user_name]}")

        # Option for making a payment
        elif service == "2" :

            payee = input("Please enter the name of the payee : ").lower()
            amount = float(input("Please enter the amount to pay : "))

            # Decline the transfer if they don't have enough money
            if amount > users_bal[user_name] :
                print(f"Sorry, you only have £{users_bal[user_name]} in your account.")

            else :
                users_bal[user_name] -= amount
                print(f"You have paid {payee.capitalize()} an amount of £{amount}. You have £{users_bal[user_name]} remaining")

                # Add the amount to the payee's account, if they already exist in the dictionary
                if payee in users_bal.keys() :
                    users_bal[payee] += amount

                # Else add the new user to the dictionary, with the amount as their balance
                else :
                    users_bal[payee] = amount

        # Option for making a withdrawal
        elif service == "3" :
            withdraw = int(input("Enter the value of the amount you would like to withdraw : "))

            # Decline if they don't have enough money
            if withdraw > users_bal[user_name] :
                print(f"Sorry, you only have £{users_bal[user_name]} in your account")

            else :
                users_bal[user_name] -= withdraw
                print(f"Here is £{withdraw}. You have £{users_bal[user_name]} remaining.")

        # Option for making a deposit
        elif service == "4" :
            
            # Ask for the deposit amount and change to float, then add to balance
            deposit = float(input("Enter the value of the amount you would like to deposit : "))
            users_bal[user_name] += deposit
            print(f"Deposit of £{deposit} sucessfully received. You now have £{users_bal[user_name]} in your account.")

