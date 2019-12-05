import pymysql
import pandas as pl
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


# SQL SELECT FUNCTIONS: DONT KNOW IF THESE FOUR WILL WORK PROPERLY; THEY MAY ONLY RETURN A SINGLE ATTRIBUTE INSTEAD OF ALL
def SearchByPokeName(mysql_cur, pokemon_name):
    mysql_cur.execute(f"SELECT * FROM Pokemon WHERE pokemon_name = {pokemon_name}")
    result = mysql_cur.fetchone()
    return str(result[0])

def SearchByPokeDex(mysql_cur, pokemon_id):
    mysql_cur.execute(f"SELECT * FROM Pokemon WHERE pokemon_id = {pokemon_id}")
    result = mysql_cur.fetchone()
    return str(result[0])

def SearchByMoveName(mysql_cur, moves_name):
    mysql_cur.execute(f"SELECT * FROM Moves WHERE moves_name = {moves_name}")
    result = mysql_cur.fetchone()
    return str(result[0])

def SearchByAbilityName(mysql_cur, abilities_name):
    mysql_cur.execute(f"SELECT * FROM Abilities WHERE abilities_name = {abilities_name}")
    result = mysql_cur.fetchone()
    return str(result[0])

#NEED TO ADD ABILITY AND MOVES TO POKEMON CREATION
def CreatePokemon(mysql_cur, pokemon_name, pokemon_typeone, pokemon_typetwo):
    mysql_cur.execute(f"INSERT INTO Pokemon VALUES ('{pokemon_name}', {pokemon_typeone}, '{pokemon_typetwo}')")
    #mysql_cur.execute(f"INSERT INTO PokemonMoves VALUES ()")
    #mysql_cur.execute(f"INSERT INTO PokemonAbilities VALUES ()")

def CreateMove(mysql_cur, moves_name, moves_type, moves_uses, moves_damage, moves_accuracy):
    mysql_cur.execute(f"INSERT INTO Moves VALUES ('{moves_name}', {moves_type}, '{moves_uses}', '{moves_damage}', '{moves_accuracy}')")

def CreateAbility(mysql_cur, abilities_name):
    mysql_cur.execute(f"INSERT INTO Abilities VALUES ('{abilities_name}')")


# __________ FUNCTIONS

def ReadData():     #COULD USE AGGREGATE FUNCTIONS FOR MORE SPECIFIC SEARCH RESULTS (ie, search for pokemon by type, by moves, etc)
    readingData = True

    print("\nWhat data would you like to view?")
    print("1. \nPokemon")
    print("2. Moves")
    print("3. Abilities")
    #print("4. Types")                IF WE ADD A TYPES TABLE
    print("5. Return to previous menu")

    while (readingData):
        inputSelection = int(input("\nPlease select an option: "))

        if (inputSelection == 1):
            print("First Option Selected")
            print("\nWould you like to search by Name or Pokedex Number?")
            print("1. \nName")
            print("2. Pokedex Number")

            while (True):
                inputSelection = int(input("\nPlease select an option: "))

                if (inputSelection == 1):
                    print("First Option Selected")
                    pokeName = input("\nPlease enter the Pokemon's Name: ")
                    print(SearchByPokeName(mysql_cur, pokeName))
                    break
                elif (inputSelection == 2):
                    print("Second Option Selected")
                    dexNum = int(input("\nPlease enter the Pokedex Number: "))
                    print(SearchByPokeDex(mysql_cur, dexNum))
                    break
                else:
                    print("\nThe input given was invalid.")

        elif (inputSelection == 2):
            print("Second Option Selected")

            moveName = input("\nPlease enter the name of the move: ")
            print(SearchByMoveName(mysql_cur, moveName))

        elif (inputSelection == 3):
            print("Third Option Selected")

            abilityName = input("\nPlease enter the name of the move: ")
            print(SearchByAbilityName(mysql_cur, abilityName))

        #elif (inputSelection == 4):
        #    print("Fourth Option Selected")
        elif (inputSelection == 5):
            print("Fifth Option Selected")
            readingData = False
        else:
            print("\nThe input given was invalid.")

def AddNewData():   #NEED FUNCTIONALITY TO ADD MOVES TO A POKEMON
    addingData = True

    while (addingData):
        print("\nWhat data would you like to add?")
        print("1. \nNew Pokemon")
        print("2. New Moves")
        print("3. New Abilities")
        #print("4. New Types")                IF WE ADD A TYPES TABLE
        print("5. Return to previous menu")

        inputSelection = int(input("\nPlease select an option: "))

        if (inputSelection == 1):
            print("First Option Selected")
            count = 0
            while (count < 4):
                exitCreatingPokemon = input("\nType 'y' to cancel: ")
                if (exitCreatingPokemon == 'y' or exitCreatingPokemon == 'Y'):
                    break
                elif (count == 0):
                    pokeName = input("\nEnter the name of the new Pokemon: ")
                    count += 1
                elif (count == 1):
                    pokeTypeOne = input("\nEnter the type of the Pokemon: ")
                    count += 1
                elif (count == 2):
                    pokeTypeTwo = input("\nEnter the second type of the pokemon (If it does not have one, enter 'None'): ")
                    count += 1
                elif (count == 3):
                    CreatePokemon(mysql_cur, pokeName, pokeTypeOne, pokeTypeTwo)
                    count += 1
                else:
                    print("Invalid input given.")
        elif (inputSelection == 2):
            print("Second Option Selected")
            count = 0
            while (count < 6):
                exitCreatingPokemon = input("\nWould you like to cancel? (y/n)")
                if (exitCreatingPokemon == 'y' or exitCreatingPokemon == 'Y'):
                    break
                elif (count == 0):
                    moveName = input("\nEnter the name of the new move: ")
                    count += 1
                elif (count == 1):
                    pokeTypeOne = input("\nEnter the type of the move: ")
                    count += 1
                elif (count == 2):
                    pokeTypeTwo = input("\nEnter the number of uses of the move: ")
                    count += 1
                elif (count == 3):
                    pokeTypeTwo = inputint(("\nEnter the move's damage (integer): "))
                    count += 1
                elif (count == 4):
                    pokeTypeTwo = input(int("\nEnter the move's accuracy (integer): "))
                    count += 1
                elif (count == 5):
                    CreateMove(mysql_cur, moveName, moveType, moveUses, moveDamage, moveAccuracy)
                    count += 1
                else:
                    print("Invalid input given.")
        elif (inputSelection == 3):
            print("Third Option Selected")
            count = 0
            while (count < 2):
                exitCreatingPokemon = input("\nWould you like to cancel? (y/n)")
                if (exitCreatingPokemon == 'y' or exitCreatingPokemon == 'Y'):
                    break
                elif (count == 0):
                    abilityName = input("\nEnter the name of the new ability: ")
                    count += 1
                elif (count == 1):
                    CreateAbility(mysql_cur, abilityName)
                    count += 1
                else:
                    print("Invalid input given.")
        #elif (inputSelection == 4):
        #    print("Fourth Option Selected")
        elif (inputSelection == 5):
            print("Fifth Option Selected")
            addingData = False
        else:
            print("\nThe input given was invalid.")

def UpdateData():
    print("\nUpdating Data...")

def DeleteData():
    print("\nDeleting Data...")

# MAIN FUNCTION

def main():

    mysql_conn = create_mysql_connection(db_user='root', db_password='rMxtwa024OfAi7iF', host_name='35.226.194.71', db_name='banking_app')
    mysql_cur = mysql_conn.cursor()

    isRunning = True

    print("\nHello, Welcome to The Pokemon Database! What would you like to do?")

    while (isRunning == True):

        print("1. \nFind a pokemon")
        print("2. Add on to our existing data")
        print("3. Update the data we have")
        print("4. Delete an entry from our data")
        print("5. Exit")

        inputSelection = int(input("\nPlease select an option: "))

        if (inputSelection == 1):
            print("First Option Selected")
            ReadData()                              #IMPLEMENTED WITHOUT TESTING OR ERROR HANDLING
        elif (inputSelection == 2):
            print("Second Option Selected")
            AddNewData()                            #LIMITED IMPLEMENTATION
        elif (inputSelection == 3):
            print("Third Option Selected")
            UpdateData()                            #NO IMPLEMENTATION
        elif (inputSelection == 4):
            print("Fourth Option Selected")
            DeleteData()                            #NO IMPLEMENTATION
        elif (inputSelection == 5):
            print("Fifth Option Selected")
            print("\nThank you for using our program!")
            isRunning = False
        else:
            print("\nThe input given was invalid.")

    #mysql_pandas = pl.read_sql('SELECT * FROM test_table;', con=mysql_conn)
    #print(mysql_pandas.head())

if __name__ == "__main__":
    main()
