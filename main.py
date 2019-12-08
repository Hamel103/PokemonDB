import pymysql
from datetime import datetime

def create_mysql_connection(db_user, db_password, host_name, db_name):
    conn = None
    try:
        conn = pymysql.connect(user=db_user, password=db_password, host=host_name, db=db_name)
    except:
        print("Connection failed..")
    return conn

#SQL GENERAL FUNCTIONS
def getPokemonName(mysql_cur, pokemon_id):
    mysql_cur.execute(f"SELECT pokemon_name FROM Pokemon WHERE pokemon_id = '{pokemon_id}'")
    result = mysql_cur.fetchone()
    return str(result[0])

# SQL SELECT FUNCTIONS: DONT KNOW IF THESE FOUR WILL WORK PROPERLY; THEY MAY ONLY RETURN A SINGLE ATTRIBUTE INSTEAD OF ALL
def viewAllPokemon(mysql_cur):
    mysql_cur.execute(f"SELECT * FROM Pokemon")
    result = mysql_cur.fetchone()
    return str(result[0])

def searchPkmnByName(mysql_cur, pokemon_name):
    mysql_cur.execute(f"SELECT * FROM Pokemon WHERE pokemon_name = '{pokemon_name}'")
    result = mysql_cur.fetchone()
    return str(result[0])

def searchPkmnByDex(mysql_cur, pokemon_id):
    mysql_cur.execute(f"SELECT * FROM Pokemon WHERE pokemon_id = {pokemon_id}")
    result = mysql_cur.fetchone()
    return str(result[0])

def searchPkmnByType(mysql_cur, type_id):
    mysql_cur.execute(f"SELECT * FROM Pokemon WHERE pokemon_typeone = {type_id} OR pokemon_typetwo = {type_id}")
    result = mysql_cur.fetchone()
    return str(result[0])

def viewAllTypes(mysql_cur):
    mysql_cur.execute(f"SELECT * FROM Type")
    result = mysql_cur.fetchone()
    return str(result[0])

def searchTypeByID(mysql_cur, type_id):
    mysql_cur.execute(f"SELECT type_name FROM Type WHERE type_id = {type_id}")
    result = mysql_cur.fetchone()
    return str(result[0])

def viewAllAbilities(mysql_cur):
    mysql_cur.execute(f"SELECT * FROM Abilities")
    result = mysql_cur.fetchone()
    return str(result[0])

def searchAbilityByID(mysql_cur, abilities_id):
    mysql_cur.execute(f"SELECT abilities_name FROM Abilities WHERE abilities_id = {abilities_id}")
    result = mysql_cur.fetchone()
    return str(result[0])

#SQL CREATE FUNCTIONS: NEED TO ADD ABILITY AND MOVES TO POKEMON CREATION
def createPokemon(mysql_cur, pokemon_name, pokemon_typeone, pokemon_typetwo, pokemon_ability):
    mysql_cur.execute(f"INSERT INTO Pokemon VALUES ('{pokemon_name}', {pokemon_typeone}, '{pokemon_typetwo}', '{pokemon_ability}')")
    #mysql_cur.execute(f"INSERT INTO PokemonAbilities VALUES ()")

def createType(mysql_cur, type_name):
    mysql_cur.execute(f"INSERT INTO Type VALUES ('{type_name}')")

def createAbility(mysql_cur, abilities_name):
    mysql_cur.execute(f"INSERT INTO Abilities VALUES ('{abilities_name}')")

# SQL UPDATE FUNCTIONS
def updatePkmnName(mysql_cur, old_pokemon_name, new_pokemon_name):
    mysql_cur.execute(f"UPDATE Pokemon SET pokemon_name = {new_pokemon_name} WHERE pokemon_name = '{old_pokemon_name}'")

def updatePkmnTypeOne(mysql_cur, pokemon_name, new_pokemon_typeone):
    mysql_cur.execute(f"UPDATE Pokemon SET pokemon_typeone = {new_pokemon_typeone} WHERE pokemon_name = '{pokemon_name}'")

def updatePkmnTypeTwo(mysql_cur, pokemon_name, new_pokemon_typetwo):
    mysql_cur.execute(f"UPDATE Pokemon SET pokemon_typetwo = {new_pokemon_typetwo} WHERE pokemon_name = '{pokemon_name}'")

def updatePkmnAbility(mysql_cur, pokemon_ability, new_pokemon_ability):
    mysql_cur.execute(f"UPDATE Pokemon SET pokemon_ability = {new_pokemon_ability} WHERE pokemon_ability = '{pokemon_ability}'")

def updateTypeName(mysql_cur, old_type_name, new_type_name):
    mysql_cur.execute(f"UPDATE Abilities SET type_name = {new_type_name} WHERE type_name = '{old_type_name}'")

def updateAbilityName(mysql_cur, old_abilities_name, new_abilities_name):
    mysql_cur.execute(f"UPDATE Abilities SET abilities_name = {new_abilities_name} WHERE abilities_name = '{old_abilities_name}'")

#SQL DELETE FUNCTIONS: NEED TO ACCOUNT FOR HOW THESE DELETES IMPACT THE FOREIGN KEYS
def deletePkmnByID(mysql_cur, pokemon_id):
    mysql_cur.execute(f"DELETE * FROM Pokemon WHERE pokemon_id = '{pokemon_id}'")

def deletePkmnByName(mysql_cur, pokemon_name):
    mysql_cur.execute(f"DELETE * FROM Pokemon WHERE pokemon_name = '{pokemon_name}'")

def deleteTypeByID(mysql_cur, type_id):
    mysql_cur.execute(f"DELETE * FROM Type WHERE type_id = '{type_id}'")

def deleteTypeByName(mysql_cur, type_name):
    mysql_cur.execute(f"DELETE * FROM Type WHERE type_name = '{type_name}'")

def deleteAbilityByID(mysql_cur, abilities_id):
    mysql_cur.execute(f"DELETE * FROM Abilities WHERE abilities_id = '{abilities_id}'")

def deleteAbilityByName(mysql_cur, abilities_name):
    mysql_cur.execute(f"DELETE * FROM Abilities WHERE abilities_name = '{abilities_name}'")

# CRUD FUNCTIONS

def readData():     #COULD USE AGGREGATE FUNCTIONS FOR MORE SPECIFIC SEARCH RESULTS (ie, search for pokemon by type, etc)
    readingData = True
    while (readingData):
        print("\nWhat data would you like to view?")
        print("\n1. Pokémon")
        print("2. Types")
        print("3. Abilities")
        print("4. Return to previous menu")

        inputSelection = input("\nPlease select an option: ")

        if (inputSelection == '1'):
            print("\nWhat would you like to view?")
            print("\n1. All Pokemon")
            print("2. All Pokemon of a certain Type")
            print("3. A specific Pokemon")
            print("4. Return to previous menu")
            inputSelection = input("\nPlease select an option: ")

            if (inputSelection == '1'):
                print("Showing the entire dex..\n\n")
                print(viewAllPokemon(mysql_cur))
            elif (inputSelection == '2'):
                typeID = int(input("Please enter the Type ID you would like to search by: "))
                print(searchPkmnByType(mysql_cur, typeID))
            elif (inputSelection == '3'):
                print("\nWould you like to search by Name or Pokédex Number?")
                print("\n1. Name")
                print("2. Pokédex Number")
                while (True):
                    inputSelection = int(input("\nPlease select an option: "))
                    if (inputSelection == 1):
                        pokeName = input("\nPlease enter the Pokémon's Name: ")
                        print(seachPkmnByName(mysql_cur, pokeName))
                        break
                    elif (inputSelection == 2):
                        dexNum = int(input("\nPlease enter the Pokédex Number: "))
                        print(serchPkmnByDex(mysql_cur, dexNum))
                        break
                    else:
                        print("\nERROR. Invalid input.")
            elif (inputSelection == '4'):
                print("Returning to previous menu..\n")
            else:
                print("Invalid input given.")

        elif (inputSelection == '2'):
            print("Showing all types..\n\n")
            print(viewAllTypes(mysql_cur))
        elif (inputSelection == '3'):
            print("Showing all abilities..\n\n")
            print(viewAllAbilities(mysql_cur))
        elif (inputSelection == '4'):
            print("Returning to previous menu..\n")
            readingData = False
        else:
            print("\nERROR. Invalid input.")

def addNewData():
    addingData = True
    while (addingData):
        print("\nWhat data would you like to add?")
        print("\n1. New Pokémon")
        print("2. New Type")
        print("3. New Abilities")
        print("4. Return to previous menu")
        inputSelection = input("\nPlease select an option: ")

        if (inputSelection == '1'):
            count = 0
            while (count < 5):
                exitCreatingPokemon = input("\nType 'y' to cancel: ")
                if (exitCreatingPokemon == 'y' or exitCreatingPokemon == 'Y'):
                    break
                elif (count == 0):
                    pokeName = input("\nEnter the name of the new Pokemon: ")
                    count += 1
                elif (count == 1):
                    pokeTypeOne = input("\nEnter the Type ID for the Pokemon: ")
                    count += 1
                elif (count == 2):
                    pokeTypeTwo = input("\nEnter the second Type ID for the pokemon (If it does not have one, leave the input empty): ")
                    count += 1
                elif (count == 3):
                    pokeAbility = input("\nEnter the Ability ID for the Pokemon: ")
                    count += 1
                elif (count == 4):
                    createPokemon(mysql_cur, pokeName, pokeTypeOne, pokeTypeTwo, pokeAbility)
                    count += 1
                else:
                    print("ERROR. Invalid input.")
        elif (inputSelection == '2'):
            count = 0
            while (count < 2):
                exitCreatingType = input("\nWould you like to cancel? (y/n)")
                if (exitCreatingType == 'y' or exitCreatingType == 'Y'):
                    break
                elif (count == 0):
                    typeName = input("\nEnter the name of the new Type: ")
                    count += 1
                elif (count == 1):
                    createType(mysql_cur, typeName)
                    count += 1
                else:
                    print("ERROR. Invalid input.")
        elif (inputSelection == '3'):
            count = 0
            while (count < 2):
                exitCreatingAbility = input("\nWould you like to cancel? (y/n)")
                if (exitCreatingAbility == 'y' or exitCreatingAbility == 'Y'):
                    break
                elif (count == 0):
                    abilityName = input("\nEnter the name of the new ability: ")
                    count += 1
                elif (count == 1):
                    createAbility(mysql_cur, abilityName)
                    count += 1
                else:
                    print("ERROR. Invalid input.")
        elif (inputSelection == '4'):
            print("Returning to previous menu..\n")
            addingData = False
        else:
            print("ERROR. Invalid input.")

def updateData():
    updatingData = True
    while (updatingData):
        print("\nWhat data would you like to update?")
        print("\n1. Pokemon")
        print("2. Types")
        print("3. Abilities")
        print("4. Return to previous menu")

        inputSelection = input("\nPlease select an option: ")

        if (inputSelection == '1'):
            print("First Option Selected")
            print("\nWhat would you like to update?")
            print("\n1. Name")
            print("2. First Type")
            print("3. Second Type")
            print("4. Ability")
            print("5. Return to previous menu")

            while (True):
                inputSelection = input("\nPlease select an option: ")

                if (inputSelection == '1'):
                    currPokeName = input("\nPlease enter the Pokemon's current name that you would like to change: ")
                    oldPokeName = input("\nPlease enter the Pokemon's new name: ")
                    updatePkmnName(mysql_cur, currPokeName, newPokeName)
                    break
                elif (inputSelection == '2'):
                    pokeName = input("\nPlease enter the name of the Pokemon whose type you would like to update: ")
                    newTypeOne = int(input("\nPlease enter the new Type ID: "))
                    updatePkmnTypeOne(mysql_cur, pokeName, newTypeOne)
                    break
                elif (inputSelection == '3'):
                    pokeName = input("\nPlease enter the name of the Pokemon whose type you would like to update: ")
                    newTypeTwo = input("\nPlease enter the new Type ID: ")
                    updatePkmnTypeTwo(mysql_cur, pokeName, newTypeTwo)
                    break
                elif (inputSelection == '4'):
                    currPokeAbility = input("\nPlease enter the Pokemon's current Ability that you would like to change: ")
                    oldPokeAbility = input("\nPlease enter the Pokemon's new Ability: ")
                    updatePkmnAbility(mysql_cur, currPokeAbility, newPokeAbility)
                    break
                elif (inputSelection == '5'):
                    print("Returning to previous menu..\n")
                    break
                else:
                    print("\nThe input given was invalid.")
        elif (inputSelection == '2'):
            print("\nWhat would you like to update?")
            print("\n1. Name")
            print("2. Return to previous menu")
            while (True):
                inputSelection = input("\nPlease select an option: ")

                if (inputSelection == '1'):
                    currTypeName = input("\nPlease enter the name of the ability you would like to update: ")
                    newTypeName = input("\nPlease enter the new name: ")
                    updateAbilitiesName(mysql_cur, currTypeName, newTypeName)
                    break
                elif (inputSelection == '2'):
                    print("Returning to previous menu..\n")
                    break
                else:
                    print("The input was invalid.")
        elif (inputSelection == '3'):
            print("\nWhat would you like to update?")
            print("\n1. Name")
            print("2. Return to previous menu")
            while (True):
                inputSelection = input("\nPlease select an option: ")

                if (inputSelection == '1'):
                    currAbilitiesName = input("\nPlease enter the name of the ability you would like to update: ")
                    newAbilitiesName = input("\nPlease enter the new name: ")
                    updateAbilitiesName(mysql_cur, currAbilitiesName, newAbilitiesName)
                    break
                elif (inputSelection == '2'):
                    print("Returning to previous menu..\n")
                    break
                else:
                    print("ERROR. Invalid input.")
        elif (inputSelection == 4):
            print("Returning to previous menu..\n")
            updatingData = False
        else:
            print("\nERROR. Invalid input.")

def deleteData():
    deletingData = True
    while (deletingData):
        print("\nWhat data would you like to delete?")
        print("\n1. Pokémon")
        print("2. Types")
        print("3. Abilities")
        print("4. Return to previous menu")

        inputSelection = input("\nPlease select an option: ")

        if (inputSelection == '1'):
            print("\nWould you like to delete by Name or Pokédex Number(ID)?")
            print("1. \nName")
            print("2. Pokédex Number(ID)")
            while (True):
                inputSelection = input("\nPlease select an option: ")
                if (inputSelection == '1'):
                    pokeName = input("\nPlease enter the Pokemon's Name: ")
                    deletePkmnByName(mysql_cur, pokeName)
                    break
                elif (inputSelection == '2'):
                    dexNum = input("\nPlease enter the Pokedex Number(ID): ")
                    print(f"You have deleted '{getPokemonName(mysql_cur, dexNum)}' from the database.")
                    deletePkmnByID(mysql_cur, dexNum)
                    break
                else:
                    print("\nERROR. Invalid input.")
        elif (inputSelection == '2'):
            print("\nWould you like to delete by Name or Type ID?")
            print("\n1. Name")
            print("2. Type ID")
            while (True):
                inputSelection = input("\nPlease select an option: ")
                if (inputSelection == '1'):
                    typeName = input("\nPlease enter the Type's Name: ")
                    deleteTypeByName(mysql_cur, typeName)
                    break
                elif (inputSelection == '2'):
                    typeID = int(input("\nPlease enter the Type ID: "))
                    print(f"You have deleted '{searchTypeByID(mysql_cur, typeID)}' from the database.")
                    deleteTypeByID(mysql_cur, typeID)
                    break
                else:
                    print("\nERROR. Invalid input.")
        elif (inputSelection == '3'):
            print("Third Option Selected")
            print("\nWould you like to delete by Name or ID Number?")
            print("\n1. Name")
            print("2. ID Number")
            while (True):
                inputSelection = input("\nPlease select an option: ")
                if (inputSelection == '1'):
                    print("First Option Selected")
                    abilityName = input("\nPlease enter the Ability's Name: ")
                    deleteAbilityByName(mysql_cur, abilityName)
                    break
                elif (inputSelection == '2'):
                    print("Second Option Selected")
                    abilityID = input("\nPlease enter the Ability's ID: ")
                    print(f"You have deleted '{searchAbilityByID(mysql_cur, abilityID)}' from the database.")
                    deleteAbilityByID(mysql_cur, abilityID)
                    break
                else:
                    print("\nERROR. Invalid input.")
        elif (inputSelection == '4'):
            print("Returning to previous menu..\n")
            deletingData = False
        else:
            print("\nERROR. Invalid input.")

# MAIN FUNCTION
def main():
    #mysql_conn = create_mysql_connection(db_user='root', db_password='rMxtwa024OfAi7iF', host_name='35.226.194.71', db_name='banking_app')
    mysql_conn = create_mysql_connection(db_user='root', db_password='password', host_name='104.197.101.227', db_name='PokemonDB')
    mysql_cur = mysql_conn.cursor()
    isRunning = True

    print("\nWelcome to The Pokémon Database!")
    print("- - - - -")

    while (isRunning == True):

        print("\n1. Search for a Pokémon")
        print("2. Add a new Pokémon")
        print("3. Update an existing data entry")
        print("4. Delete an existing data entry")
        print("5. Exit")

        inputSelection = input("\nEnter an option: ")

        if (inputSelection == '1'):
            readData()                              #LIMITED IMPLEMENTATION WITHOUT ERROR HANDLING
        elif (inputSelection == '2'):
            addNewData()                            #IMPLEMENTED WITHOUT ERROR HANDLING
        elif (inputSelection == '3'):
            updateData()                            #IMPLEMENTED WITHOUT ERROR HANDLING
        elif (inputSelection == '4'):
            deleteData()                            #IMPLEMENTED WITHOUT ERROR HANDLING
        elif (inputSelection == '5'):
            print("\nThank you for using The Pokémon Database! Now exiting...\n")
            isRunning = False
        else:
            print("\nERROR. Invalid input.")

if __name__ == "__main__":
    main()
