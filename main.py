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

#SQL CREATE FUNCTIONS: NEED TO ADD ABILITY AND MOVES TO POKEMON CREATION
def CreatePokemon(mysql_cur, pokemon_name, pokemon_typeone, pokemon_typetwo):
    mysql_cur.execute(f"INSERT INTO Pokemon VALUES ('{pokemon_name}', {pokemon_typeone}, '{pokemon_typetwo}')")
    #mysql_cur.execute(f"INSERT INTO PokemonMoves VALUES ()")
    #mysql_cur.execute(f"INSERT INTO PokemonAbilities VALUES ()")

def CreateMove(mysql_cur, moves_name, moves_type, moves_uses, moves_damage, moves_accuracy):
    mysql_cur.execute(f"INSERT INTO Moves VALUES ('{moves_name}', {moves_type}, '{moves_uses}', '{moves_damage}', '{moves_accuracy}')")

def CreateAbility(mysql_cur, abilities_name):
    mysql_cur.execute(f"INSERT INTO Abilities VALUES ('{abilities_name}')")

# SQL UPDATE FUNCTIONS
def UpdatePokemonName(mysql_cur, old_pokemon_name, new_pokemon_name):
    mysql_cur.execute(f"UPDATE Pokemon SET pokemon_name = {new_pokemon_name} WHERE pokemon_name = '{old_pokemon_name}'")

def UpdatePokemonTypeOne(mysql_cur, pokemon_name, new_pokemon_typeone):
    mysql_cur.execute(f"UPDATE Pokemon SET pokemon_typeone = {new_pokemon_typeone} WHERE pokemon_name = '{pokemon_name}'")

def UpdatePokemonTypeTwo(mysql_cur, pokemon_name, new_pokemon_typetwo):
    mysql_cur.execute(f"UPDATE Pokemon SET pokemon_typetwo = {new_pokemon_typetwo} WHERE pokemon_name = '{pokemon_name}'")

def UpdateMovesName(mysql_cur, old_moves_name, new_moves_name):
    mysql_cur.execute(f"UPDATE Moves SET moves_name = {new_moves_name} WHERE moves_name = '{old_moves_name}'")

def UpdateMovesType(mysql_cur, moves_name, new_moves_type):
    mysql_cur.execute(f"UPDATE Moves SET moves_type = {new_moves_type} WHERE moves_name = '{moves_name}'")

def UpdateMovesUses(mysql_cur, moves_name, new_moves_uses):
    mysql_cur.execute(f"UPDATE Moves SET moves_uses = {new_moves_uses} WHERE moves_name = '{moves_name}'")

def UpdateMovesDamage(mysql_cur, moves_name, new_moves_damage):
    mysql_cur.execute(f"UPDATE Moves SET moves_damage = {new_moves_damage} WHERE moves_name = '{moves_name}'")

def UpdateMovesAccuracy(mysql_cur, moves_name, new_moves_accuracy):
    mysql_cur.execute(f"UPDATE Moves SET moves_accuracy = {new_moves_accuracy} WHERE moves_name = '{moves_name}'")

def UpdateAbilitiesName(mysql_cur, old_abilities_name, new_abilities_name):
    mysql_cur.execute(f"UPDATE Abilities SET abilities_name = {new_abilities_name} WHERE abilities_name = '{old_abilities_name}'")

#SQL DELETE FUNCTIONS: NEED TO ACCOUNT FOR HOW THESE DELETES IMPACT THE FOREIGN KEYS
def DeletePokemonByID(mysql_cur, pokemon_id):
    mysql_cur.execute(f"DELETE * FROM Pokemon WHERE pokemon_id = '{pokemon_id}'")

def DeletePokemonByName(mysql_cur, pokemon_name):
    mysql_cur.execute(f"DELETE * FROM Pokemon WHERE pokemon_name = '{pokemon_name}'")

def DeleteMoveByID(mysql_cur, moves_id):
    mysql_cur.execute(f"DELETE * FROM Moves WHERE moves_id = '{moves_id}'")

def DeleteMoveByName(mysql_cur, moves_name):
    mysql_cur.execute(f"DELETE * FROM Moves WHERE moves_name = '{moves_name}'")

def DeleteAbilityByID(mysql_cur, abilities_id):
    mysql_cur.execute(f"DELETE * FROM Abilities WHERE abilities_id = '{abilities_id}'")

def DeleteAbilityByName(mysql_cur, abilities_name):
    mysql_cur.execute(f"DELETE * FROM Abilities WHERE abilities_name = '{abilities_name}'")

# CRUD FUNCTIONS

def ReadData():     #COULD USE AGGREGATE FUNCTIONS FOR MORE SPECIFIC SEARCH RESULTS (ie, search for pokemon by type, by moves, etc)
    readingData = True

    while (readingData):
        print("\nWhat data would you like to view?")
        print("1. \nPokemon")
        print("2. Moves")
        print("3. Abilities")
        #print("4. Types")                IF WE ADD A TYPES TABLE
        print("5. Return to previous menu")

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
                    pokeTypeOne = int(input("\nEnter the Type ID of the Pokemon: "))
                    count += 1
                elif (count == 2):
                    pokeTypeTwo = int(input("\nEnter the second Type ID of the pokemon (If it does not have one, leave the input empty): "))
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
                    moveType = int(input("\nEnter the Type ID of the move: "))
                    count += 1
                elif (count == 2):
                    moveUses = input("\nEnter the number of uses of the move: ")
                    count += 1
                elif (count == 3):
                    moveDamage = int(input("\nEnter the move's damage (integer): "))
                    count += 1
                elif (count == 4):
                    moveAccuracy = int(input("\nEnter the move's accuracy (integer): "))
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
    updatingData = True

    #POKEMON: Name, Type One, Type Two
    #MOVES: Name, Type, Uses, Damage, accuracy
    #ABILITIES: Name

    while (updatingData):
        print("\nWhat data would you like to update?")
        print("1. \nPokemon")
        print("2. Moves")
        print("3. Abilities")
        #print("4. Types")                IF WE ADD A TYPES TABLE
        print("5. Return to previous menu")

        inputSelection = int(input("\nPlease select an option: "))

        if (inputSelection == 1):
            print("First Option Selected")
            print("\nWhat would you like to update?")
            print("1. \nName")
            print("2. First Type")
            print("3. Second Type")
            print("4. Return to previous menu")

            while (True):
                inputSelection = int(input("\nPlease select an option: "))

                if (inputSelection == 1):
                    print("First Option Selected")
                    currPokeName = input("\nPlease enter the Pokemon's current name that you would like to change: ")
                    oldPokeName = input("\nPlease enter the Pokemon's new name: ")
                    UpdatePokemonName(mysql_cur, currPokeName, newPokeName)
                    break
                elif (inputSelection == 2):
                    print("Second Option Selected")
                    pokeName = input("\nPlease enter the name of the Pokemon whose type you would like to update: ")
                    newTypeOne = int(input("\nPlease enter the new Type ID: "))
                    UpdatePokemonTypeOne(mysql_cur, pokeName, newTypeOne))
                    break
                elif (inputSelection == 3):
                    print("Third Option Selected")
                    pokeName = input("\nPlease enter the name of the Pokemon whose type you would like to update: ")
                    newTypeTwo = int(input("\nPlease enter the new Type ID: "))
                    UpdatePokemonTypeOne(mysql_cur, pokeName, newTypeTwo))
                    break
                elif (inputSelection == 4):
                    break
                else:
                    print("\nThe input given was invalid.")
        elif (inputSelection == 2):
            print("You chose option 2")
            print("\nWhat would you like to update?")
            print("1. \nName")
            print("2. Type")
            print("3. Uses")
            print("4. Damage")
            print("5. Accuracy")
            print("6. Return to previous menu")
            while (True):
                inputSelection = int(input("\nPlease select an option: "))

                if (inputSelection == 1):
                    print("First Option Selected")
                    currMovesName = input("\nPlease enter the move's current name that you would like to change: ")
                    oldMovesName = input("\nPlease enter the move's new name: ")
                    UpdatePokemonName(mysql_cur, currMovesName, newMovesName)
                    break
                elif (inputSelection == 2):
                    print("Second Option Selected")
                    movesName = input("\nPlease enter the move's name whose type you would like to update: ")
                    newMovesType = int(input("\nPlease enter the new Type ID: "))
                    UpdatePokemonTypeOne(mysql_cur, movesName, newMovesType))
                    break
                elif (inputSelection == 3):
                    print("Third Option Selected")
                    movesName = input("\nPlease enter the move's name whose uses you would like to update: ")
                    newMovesUses = input("\nPlease enter the new amount of uses: ")
                    UpdatePokemonTypeOne(mysql_cur, movesName, newMovesUses))
                    break
                elif (inputSelection == 4):
                    print("Fourth Option Selected")
                    movesName = input("\nPlease enter the move's name whose damage you would like to update: ")
                    newMovesDamage = input("\nPlease enter the new type: ")
                    UpdatePokemonTypeOne(mysql_cur, movesName, newMovesDamage))
                    break
                elif (inputSelection == 5):
                    print("Fifth Option Selected")
                    movesName = input("\nPlease enter the move's name whose accuracy you would like to update: ")
                    newMovesAccuracy = input("\nPlease enter the new type: ")
                    UpdatePokemonTypeOne(mysql_cur, movesName, newMovesAccuracy))
                    break
                elif (inputSelection == 6):
                    break
                else:
                    print("\nThe input given was invalid.")
        elif (inputSelection == 3):
            print("You chose option 3")
            print("\nWhat would you like to update?")
            print("1. \nName")
            print("2. Return to previous menu")
            while (True):
                inputSelection = int(input("\nPlease select an option: "))

                if (inputSelection == 1):
                    currAbilitiesName = input("\nPlease enter the name of the ability you would like to update: ")
                    newAbilitiesName = input("\nPlease enter the new name: ")
                    UpdateAbilitiesName(mysql_cur, currAbilitiesName, newAbilitiesName))
                    break
                elif (inputSelection == 2):
                    break
                else:
                    print("The input was invalid.")
        elif (inputSelection == 5):
            print("You chose option 5")
            updatingData = False
        else:
            print("\nThe input was invalid.")

def DeleteData():
    deletingData = True

    while (deletingData):
        print("\nWhat data would you like to delete?")
        print("1. \nPokemon")
        print("2. Moves")
        print("3. Abilities")
        #print("4. Types")                IF WE ADD A TYPES TABLE
        print("5. Return to previous menu")

        inputSelection = int(input("\nPlease select an option: "))

        if (inputSelection == 1):
            print("First Option Selected")
            print("\nWould you like to delete by Name or Pokedex Number(ID)?")
            print("1. \nName")
            print("2. Pokedex Number(ID)")

            while (True):
                inputSelection = int(input("\nPlease select an option: "))

                if (inputSelection == 1):
                    print("First Option Selected")
                    pokeName = input("\nPlease enter the Pokemon's Name: ")
                    DeletePokemonByName(mysql_cur, pokeName)
                    break
                elif (inputSelection == 2):
                    print("Second Option Selected")
                    dexNum = int(input("\nPlease enter the Pokedex Number(ID): "))
                    DeletePokemonByID(mysql_cur, dexNum)
                    break
                else:
                    print("\nThe input given was invalid.")
        elif (inputSelection == 2):
            print("Second Option Selected")
            print("\nWould you like to delete by Name or ID Number?")
            print("1. \nName")
            print("2. ID Number")

            while (True):
                inputSelection = int(input("\nPlease select an option: "))

                if (inputSelection == 1):
                    print("First Option Selected")
                    moveName = input("\nPlease enter the move's Name: ")
                    DeleteMoveByName(mysql_cur, moveName)
                    break
                elif (inputSelection == 2):
                    print("Second Option Selected")
                    moveID = int(input("\nPlease enter the Pokedex Number: "))
                    DeleteMoveByID(mysql_cur, moveID)
                    break
                else:
                    print("\nThe input given was invalid.")
        elif (inputSelection == 3):
            print("Third Option Selected")
            print("\nWould you like to delete by Name or ID Number?")
            print("1. \nName")
            print("2. ID Number")

            while (True):
                inputSelection = int(input("\nPlease select an option: "))

                if (inputSelection == 1):
                    print("First Option Selected")
                    abilityName = input("\nPlease enter the ability's Name: ")
                    DeleteAbilityByName(mysql_cur, abilityName)
                    break
                elif (inputSelection == 2):
                    print("Second Option Selected")
                    abilityID = int(input("\nPlease enter the Pokedex Number: "))
                    DeleteAbilityByID(mysql_cur, abilityID)
                    break
                else:
                    print("\nThe input given was invalid.")
        elif (inputSelection == 5):
            deletingData = False
        else:
            print("\nThe input given was invalid.")

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
