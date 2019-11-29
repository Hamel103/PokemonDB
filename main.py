import pymysql
import pandas as pl
import uuid
from datetime import datetime

def create_mysql_connection(db_user, db_password, host_name, db_name):
    conn = None
    try:
        conn = pymysql.connect(user=db_user, password=db_password, host=host_name, db=db_name)
    except:
        print("Connection failed..")
    return conn


# USING THESE AS EXAMPLE METHODS FROM ASSIGNMENT 3 AS A GUIDELINES TO CREATE METHODS USING SQL

def createCustomer(mysql_cur, id, ssn, first_name, last_name):
    mysql_cur.execute(f"INSERT INTO Customer VALUES ('{id}', {ssn}, '{first_name}', '{last_name}')")
    print(f"Welcome, {first_name} {last_name}. Your customer ID is:")
    print(id)
    print("\nMake sure to write this down so you can access your information in the future!")

def depositMoney(mysql_cur, account_num, amount):
    mysql_cur.execute(f"UPDATE Account SET balance = balance + {amount} WHERE account_num = '{account_num}'")
    logTransaction(mysql_cur, account_num=account_num, trans_type="deposit", trans_amount=amount)

def logTransaction(mysql_cur, account_num, trans_type, trans_amount):
    mysql_cur.execute(f"INSERT INTO Transaction_log VALUES ('{datetime.now()}', '{makeId()}', '{account_num}', '{trans_type}', '{trans_amount}')")
    return mysql_cur.fetchall()

def getCustomerID(mysql_cur, ssn):
    mysql_cur.execute(f"SELECT customer_id FROM Customer WHERE ssn = {ssn}")
    result = mysql_cur.fetchone()
    return str(result[0])

def makeId():
    return uuid.uuid4().hex


# MAIN FUNCTION

def main():
    #currentUser
    isRunning = True
    userLogin = False
    mysql_conn = create_mysql_connection(db_user='root', db_password='rMxtwa024OfAi7iF', host_name='35.226.194.71', db_name='banking_app')
    mysql_cur = mysql_conn.cursor()

    while (isRunning == True):
        print("Hello, Welcome to <bank_name>! You can do the following:")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        inputSelection = int(input("Please select an option: "))

        # STARTING OPTIONS
        if (inputSelection == 1):

            loginCred = input("\nEnter your Customer ID: ")
            # LOGIN AND STORE WHICH USER IS LOGGING IN
            loginCheck = checkValidLogin(mysql_cur, loginCred)
            while(not loginCheck):
                userContinue = input("\nThat was not a valid entry. Would you like to try again? (y/n): ")
                if (userContinue == 'y' or userContinue == 'Y'):
                    loginCred = input("\nEnter your Customer ID: ")
                    if (checkValidLogin(mysql_cur, loginCred)):
                        currentUser = loginCred
                        userLogin = True
                        loginCheck = True
                elif (userContinue == 'n' or userContinue == 'N'):
                    break
            if(loginCheck):
                userLogin = True
                currentUser = loginCred


        elif (inputSelection == 2):

            # REGISTERING A USER
            print("\nTo create an account, please enter the following: ")
            ssn = int(input("SSN: "))
            firstName = input("First Name: ")
            lastName = input("Last Name: ")
            id = makeId()
            createCustomer(mysql_cur, id, ssn, firstName, lastName)
            # LOGIN AND STORE WHICH USER IS LOGGING IN
            mysql_conn.commit()
            currentUser = id
            userLogin = True
            # USER REGISTRATION IMMEDIATELY LEADS TO AN ACCOUNT CREATION PROMPT
            promptToCreateAccount(mysql_cur, currentUser)
            mysql_conn.commit()

        elif (inputSelection == 3):
            print("\nThank you for using <bank_name>! Now exiting...\n")
            mysql_conn.close()
            isRunning = False;

        else:
            inputSelection = int(input("\nError. Not a valid input. Retry: "))


        # OPTIONS WHILE USER IS LOGGED IN
        while (userLogin == True):
            print("\nWelcome back to <bank_name>!\n")
            print("1. Create Account")
            print("2. Check Balance")
            print("3. Deposit Money")
            print("4. Withdraw Money")
            print("5. Transfer Money")
            print("6. Update Account Information")
            print("7. Logout\n")

            inputSelection = int(input("Please select an option: "))

            # CREATE AN ACCOUNT
            if (inputSelection == 1):
                promptToCreateAccount(mysql_cur, currentUser)
                mysql_conn.commit()

            # CHECK BALANCE OF ACCOUNT
            elif (inputSelection == 2):
                accountNum = input("\nEnter your account number: ")
                if (currentUser == crossCheckCustomerAccount(mysql_cur, currentUser, accountNum)):
                    print("\nYour balance is: $" + str(checkBalance(mysql_cur, accountNum)))
                else:
                    print("\nYou do not have access to the account you entered.")
                pass

            # DEPOSIT MONEY IN ACCOUNT
            elif (inputSelection == 3):
                accountNum = input("\nEnter your account number: ")
                if (currentUser == crossCheckCustomerAccount(mysql_cur, currentUser, accountNum)):
                    depositAmt = float(input("Enter the amount you wish to deposit: $"))
                    depositMoney(mysql_cur, accountNum, depositAmt)
                    mysql_conn.commit()
                    print("Success. Your balance after deposit is: " + str(checkBalance(mysql_cur, accountNum)))
                else:
                    print("You do not have access to this account.")
                pass

            # WITHDRAW MONEY FROM ACCOUNT
            elif (inputSelection == 4):
                accountNum = input("\nEnter your account number: ")
                if (currentUser == crossCheckCustomerAccount(mysql_cur, currentUser, accountNum)):
                    withdrawAmt = float(input("Enter the amount you wish to withdraw: $"))
                    withdrawMoney(mysql_cur, accountNum, withdrawAmt)
                    mysql_conn.commit()
                    print("Success. Your balance after withdraw is: " + str(checkBalance(mysql_cur, accountNum)))
                else:
                    print("You do not have access to this account.")
                pass

            # TRANSFER MONEY BETWEEN ACCOUNTS
            elif (inputSelection == 5):
                print()
                while (True):
                    accountNum1 = input("Please enter the account ID# you would like to transfer money out of: ")
                    if (currentUser != crossCheckCustomerAccount(mysql_cur, currentUser, accountNum1)):
                        print("The account you listed is not registered to you.")
                    else:
                        break
                while(True):
                    accountNum2 = input("Please enter the account ID# you would like to transfer money into: ")
                    if (accountNum2 != crossCheckAccount(mysql_cur, accountNum2)):
                        print("The account you listed does not exist.")
                    else:
                        break
                while(True):
                    amount = float(input("Please enter the amount of money you would like to transfer: "))
                    if (amount > 5000):
                        print("You can not transfer more than $5000 at a time. Please enter a valid amount: ")
                    else:
                        transferMoney(mysql_cur, accountNum1, accountNum2, amount)
                        mysql_conn.commit()
                        break

            # UPDATE CUSTOMER INFORMATION
            elif (inputSelection == 6):
                print("\nInformation available:")
                print("1. Change Fist Name")
                print("2. Change Last Name")
                print("3. Change SSN")

                while (True):
                    inputSelection = int(input("Enter the number of the information you would like to change: "))
                    if (inputSelection == 1):
                        firstName = input("\nEnter new first name: ")
                        updateCustomerFirstName(mysql_cur, currentUser, firstName)
                        mysql_conn.commit()
                        break
                    elif (inputSelection == 2):
                        lastName = input("\nEnter new last name: ")
                        updateCustomerLastName(mysql_cur, currentUser, lastName)
                        mysql_conn.commit()
                        break
                    elif (inputSelection == 3):
                        ssn = int(input("\nEnter new SSN: "))
                        updateCustomerSSN(mysql_cur, currentUser, ssn)
                        break
                    else:
                        print("The value you enterred is not valid.")

            # LOGOUT OF ACCOUNT
            elif (inputSelection == 7):
                print("\nThank you for using the <bank_name> banking service. Now exitting..\n")
                userLogin = False

            else:
                inputSelection = int(input("Error. Not a valid input. Retry: "))


    #mysql_pandas = pl.read_sql('SELECT * FROM test_table;', con=mysql_conn)
    #print(mysql_pandas.head())

if __name__ == "__main__":
    main()
