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

def createCustomer(mysql_cur, ssn, first_name, last_name):
    id = makeId()
    mysql_cur.execute(f"INSERT INTO Customer VALUES ('{id}', {ssn}, '{first_name}', '{last_name}')")
    print(f"Welcome, {first_name} {last_name}. Your customer ID is:")
    print(id)

def depositMoney(mysql_cur, account_num, amount):
    mysql_cur.execute('UPDATE Account SET balance = balance + ' + amount + ' WHERE account_num = ' + account_num)
    logTransaction(mysql_cur, account_num=account_num, trans_type="deposit", trans_amount=amount)
    return mysql_cur.fetchall()

def logTransaction(mysql_cur, account_num, trans_type, trans_amount):
    mysql_cur.execute("INSERT INTO Transaction_log VALUES ('" + datetime.now() + "', " + makeId() + ", " + account_num + ", " + trans_type + ", " + trans_amount + ")")
    return mysql_cur.fetchall()

def getCustomerID(mysql_cur, ssn):
    mysql_cur.execute('SELECT customer_id FROM Customer WHERE ssn = ' + ssn)
    return mysql_cur.fetchall()

def makeId():
    return uuid.uuid4().hex


# MAIN FUNCTION

def main():
    isRunning = True
    userLogin = False;
    mysql_conn = create_mysql_connection(db_user='root', db_password='password', host_name='104.197.101.227', db_name='bank')
    mysql_cur = mysql_conn.cursor()

    while (isRunning == True):
        print("\nHello, Welcome to <bank_name>! You can do the following:")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        inputSelection = int(input("Please select an option: "))


        # STARTING OPTIONS
        if (inputSelection == 1):
            loginCred = input("\nPlease enter valid login credentials to access your accounts: ")
            # LOGIN AND STORE WHICH USER IS LOGGING IN
            loginCheck = checkValidLogin(mysql_cur, loginCred)
            if (loginCheck == True):
                currentUser = loginCred
                userLogin = True
            else:
                loginCred = input("\nError. Not a valid login. Try again: ")

        elif (inputSelection == 2):
            # REGISTERING A USER
            print("\nTo create an account, please enter the following: ")
            ssn = input("SSN: ")
            firstName = input("First Name: ")
            lastName = input("Last Name: ")
            createCustomer(mysql_cur, ssn, firstName, lastName)
            # LOGIN AND STORE WHICH USER IS LOGGING IN
            mysql_conn.commit()
            loginCred = getCustomerID(mysql_cur, ssn)
            currentUser = loginCred
            userLogin = True
            # USER REGISTRATION IMMEDIATELY LEADS TO AN ACCOUNT CREATION PROMPT
            promptToCreateAccount(mysql_cur, currentUser)

        elif (inputSelection == 3):
            print("\nThank you for using <bank_name>!")
            mysql_conn.close()
            isRunning = False;
        else:
            print()
            inputSelection = int(input("Error. Not a valid input. Retry: "))


        # OPTIONS WHILE USER IS LOGGED IN
        while (userLogin == True):
            print("\n\nWelcome back to <bank_name>!\n")
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
                promptToCreateAccount()

            # CHECK BALANCE OF ACCOUNT
            elif (inputSelection == 2):
                accountNum = int(input("\nEnter your account number: "))
                if (currentUser == crossCheckCustomerAccount(mysql_cur, currentUser, accountNum)):
                    print("Your balance is: " + checkBalance(mysql_cur, accountNum))
                else:
                    print("You do not have access to the account you enterred.")
                pass

            # DEPOSIT MONEY IN ACCOUNT
            elif (inputSelection == 3):
                accountNum = int(input("\nEnter your account number: "))
                if (currentUser == crossCheckCustomerAccount(mysql_cur, currentUser, accountNum)):
                    depositAmt = float(input("Enter the amount you wish to deposit: $"))
                    depositMoney(mysql_cur, accountNum, depositAmt)
                    print("Success. Your balance after deposit is: " + checkBalance(mysql_cur, accountNum))
                else:
                    print("You do not have access to this account.")
                pass

            # WITHDRAW MONEY FROM ACCOUNT
            elif (inputSelection == 4):
                accountNum = int(input("\nEnter your account number: "))
                if (currentUser == crossCheckCustomerAccount(mysql_cur, currentUser, accountNum)):
                    withdrawAmt = float(input("Enter the amount you wish to withdraw: $"))
                    withdraw(mysql_cur, accountNum, withdrawAmt)
                    print("Success. Your balance after withdraw is: " + checkBalance(mysql_cur, accountNum))
                else:
                    print("You do not have access to this account.")
                pass

            # TRANSFER MONEY BETWEEN ACCOUNTS
            elif (inputSelection == 5):
                print()
                while (True):
                    accountNum1 = int(input("Please enter the account ID# you would like to transfer money out of: "))
                    if (currentUser == crossCheckCustomerAccount(mysql_cur, currentUser, accountNum1)):
                        accountNum2 = int(input("Please enter the account ID# you would like to transfer money into: "))
                        amount = 0
                        break
                    else:
                        print("The account you listed is not registered to you.")
                while(True):
                    amount = int(input("Please enter the amount of money you would like to transfer: "))
                    if (amount > 5000):
                        print("You can not transfer more than $5000 at a time. Please enter a valid amount: ")
                    else:
                        transferMoney(mysql_cur, accountNum1, accountNum2, amount)
                        break

            # UPDAATE CUSTOMER INFORMATION
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
                        break
                    elif (inputSelection == 2):
                        lastName = input("\nEnter new last name: ")
                        updateCustomerLastName(mysql_cur, currentUser, lastName)
                        break
                    elif (inputSelection == 3):
                        ssn = input("\nEnter first name: ")
                        updateCustomerSSN(mysql_cur, currentUser, ssn)
                        break
                    else:
                        print("The value you enterred is not valid. Please try again.")

            # LOGOUT OF ACCOUNT
            elif (inputSelection == 7):
                print("\nThank you for using the <bank_name> banking service. Now exitting..")
                mysql_conn.close()
                userLogin = False
                isRunning = False

            else:
                inputSelection = int(input("Error. Not a valid input. Retry: "))


    #mysql_pandas = pl.read_sql('SELECT * FROM test_table;', con=mysql_conn)
    #print(mysql_pandas.head())

if __name__ == "__main__":
    main()
