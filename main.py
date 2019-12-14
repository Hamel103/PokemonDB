import pymysql
from datetime import datetime

def create_mysql_connection(db_user, db_password, host_name, db_name):
    conn = None
    try:
        conn = pymysql.connect(user=db_user, password=db_password, host=host_name, db=db_name)
    except:
        print("Connection failed..")
    return conn

# SQL SELECT FUNCTIONS: DONT KNOW IF THESE FOUR WILL WORK PROPERLY; THEY MAY ONLY RETURN A SINGLE ATTRIBUTE INSTEAD OF ALL
def viewAllPokemon(mysql_cur):
    counter = 0
    mysql_cur.execute("SELECT * FROM Pokedex")
    result = mysql_cur.fetchall()
    for pkmn in result:
        print(f"Dex Number: {result[counter][0]}\nName: {result[counter][1]}\nType(s): {result[counter][2]}/{result[counter][3]}\n")
        counter += 1

def viewAllPkmnByType(mysql_cur, type_name):
    counter = 0
    mysql_cur.execute(f"SELECT * FROM Pokedex WHERE type_one = {type_name} OR type_two = {type_name}")
    result = mysql_cur.fetchall()
    for pkmn in result:
        print(f"Dex Number: {result[counter][0]}\nName: {result[counter][1]}\nType(s): {result[counter][2]}/{result[counter][3]}\n")
        counter += 1

def searchPkmnByDex(mysql_cur, dex_num):
    mysql_cur.execute(f"SELECT * FROM Pokedex WHERE dex_num = {dex_num}")
    result = mysql_cur.fetchone()
    mysql_cur.execute(f"SELECT * FROM Pokemon WHERE name = '{result[0][1]}'")
    result2 = mysql_cur.fetchone()
    return f"Dex Number: {result[0][0]}\nName: {result[0][1]}\nType(s): {result[0][2]}/{result[0][3]}\nAbility: {result[0][3]}\nCan Mega Evolve: {result2[0][1]}\nHas Gigantimax Form: {result2[0][2]}\n"

def searchPkmnByName(mysql_cur, pokemon_name):
    mysql_cur.execute(f"SELECT * FROM Pokedex WHERE pokemon_name = '{pokemon_name}'")
    result = mysql_cur.fetchone()
    mysql_cur.execute(f"SELECT * FROM Pokemon WHERE pokemon_name = '{pokemon_name}'")
    result2 = mysql_cur.fetchone()
    return f"Dex Number: {result[0][0]}\nName: {result[0][1]}\nType(s): {result[0][2]}/{result[0][3]}\nAbility: {result[0][3]}\nCan Mega Evolve: {result2[0][1]}\nHas Gigantimax Form: {result2[0][2]}\n"

def viewAllTypes(mysql_cur):
    counter = 0
    mysql_cur.execute(f"SELECT * FROM Types")
    result = mysql_cur.fetchall()
    for type in result:
        print(f"Type: {result[counter][0]}\nEffective Against: {result[counter][1]}\nWeak Against: {result[counter][2]}\n")
        counter += 1

def viewAllAbilities(mysql_cur):
    counter = 0
    mysql_cur.execute(f"SELECT * FROM Abilities")
    result = mysql_cur.fetchall()
    for type in result:
        print(f"Ability: {result[counter][0]}\nDescription: {result[counter][1]}\n")
        counter += 1

#SQL CREATE FUNCTIONS: NEED TO ADD ABILITY AND MOVES TO POKEMON CREATION
def createPokemon(mysql_cur, pokemon_name, has_mega, has_gmax, pokemon_typeone, pokemon_typetwo, pokemon_ability):
    mysql_cur.execute(f"INSERT INTO Pokemon VALUES ('{pokemon_name}', '{has_mega}', '{has_gmax}')")
    mysql_cur.execute(f"INSERT INTO Pokedex VALUES('{pokemon_name}', {pokemon_typeone}, '{pokemon_typetwo}', '{pokemon_ability}')")

def createType(mysql_cur, type_name, advantages, disadvantages):
    mysql_cur.execute(f"INSERT INTO Types VALUES ('{type_name}', '{advantages}', '{disadvantages}')")

def createAbility(mysql_cur, ability_name, description):
    mysql_cur.execute(f"INSERT INTO Abilities VALUES ('{ability_name}', '{description}')")

# SQL UPDATE FUNCTIONS
def updatePkmnName(mysql_cur, old_pokemon_name, new_pokemon_name):
    mysql_cur.execute(f"UPDATE Pokemon SET name = {new_pokemon_name} WHERE name = '{old_pokemon_name}'")

def updatePkmnTypeOne(mysql_cur, pokemon_name, new_pokemon_typeone):
    mysql_cur.execute(f"UPDATE Pokedex SET type_one = {new_pokemon_typeone} WHERE name = '{pokemon_name}'")

def updatePkmnTypeTwo(mysql_cur, pokemon_name, new_pokemon_typetwo):
    mysql_cur.execute(f"UPDATE Pokedex SET type_two = {new_pokemon_typetwo} WHERE name = '{pokemon_name}'")

def updatePkmnAbility(mysql_cur, pokemon_ability, new_pokemon_ability):
    mysql_cur.execute(f"UPDATE Pokedex SET ability_name = {new_pokemon_ability} WHERE name = '{pokemon_ability}'")

def updateTypeName(mysql_cur, old_type_name, new_type_name):
    mysql_cur.execute(f"UPDATE Types SET type_name = {new_type_name} WHERE type_name = '{old_type_name}'")

def updateAbilityName(mysql_cur, old_abilities_name, new_abilities_name):
    mysql_cur.execute(f"UPDATE Abilities SET ability_name = {new_abilities_name} WHERE ability_name = '{old_abilities_name}'")

#SQL DELETE FUNCTIONS: NEED TO ACCOUNT FOR HOW THESE DELETES IMPACT THE FOREIGN KEYS
def deletePkmnByID(mysql_cur, pokemon_id):
    mysql_cur.execute(f"DELETE * FROM Pokedex WHERE dex_num = '{pokemon_id}'")

def deletePkmnByName(mysql_cur, pokemon_name):
    mysql_cur.execute(f"DELETE * FROM Pokemon WHERE name = '{pokemon_name}'")

def deleteTypeByName(mysql_cur, type_name):
    mysql_cur.execute(f"DELETE * FROM Types WHERE type_name = '{type_name}'")

def deleteAbilityByID(mysql_cur, ability_name):
    mysql_cur.execute(f"DELETE * FROM Abilities WHERE ability_name = '{ability_name}'")



# CRUD FUNCTIONS
def readData(mysql_cur):
    readingData = True
    while (readingData):
        print("\nThe following data is viewable:")
        print("\n1. Pokémon")
        print("2. Types")
        print("3. Abilities")
        print("4. Return to previous menu")
        inputSelection = input("\nEnter the option number of the data you wish to view: ")

        if (inputSelection == '1'):
            print("\nThe following options are available:")
            print("\n1. View all Pokémon")
            print("2. View all Pokémon of a specificed type")
            print("3. View a specific Pokémon")
            print("4. Return to previous menu")
            inputSelection = input("\nEnter the option number you wish to view: ")

            if (inputSelection == '1'):
                print("Showing the entire dex..\n\n")
                viewAllPokemon(mysql_cur)
            elif (inputSelection == '2'):
                typeName = input("Enter the name of the type you wish to view: ")
                try:
                    viewAllPkmnByType(mysql_cur, typeName.upper())
                except:
                    print("ERROR. Invalid Type input.")
            elif (inputSelection == '3'):
                print("\nThe following options are available:")
                print("\n1. Name")
                print("2. Pokédex Number")
                print("3. Return to previous menu")
                inputSelection = input("\nPlease select an option: ")
                if (inputSelection == '1'):
                    pkmnName = input("\nEnter the name of the Pokémon you wish to view: ")
                    try:
                        print(searchPkmnByName(mysql_cur, pkmnName.upper()))
                    except:
                        print("ERROR. Invalid Pokémon name.")
                elif (inputSelection == '2'):
                    dexNum = input("\nEnter the Pokédex Number of the Pokémon you wish to view: ")
                    try:
                        print(searchPkmnByDex(mysql_cur, dexNum))
                    except:
                        print("ERROR. Invalid Pokédex Number.")
                elif (inputSelection == '3'):
                    print("Returning to previous menu..\n")
                else:
                    print("\nERROR. Invalid input.")
            elif (inputSelection == '4'):
                print("Returning to previous menu..\n")
            else:
                print("ERROR. Invalid input.")

        elif (inputSelection == '2'):
            print("Showing all types..\n\n")
            viewAllTypes(mysql_cur)

        elif (inputSelection == '3'):
            print("Showing all abilities..\n\n")
            viewAllAbilities(mysql_cur)

        elif (inputSelection == '4'):
            print("Returning to previous menu..\n")
            readingData = False
        else:
            print("\nERROR. Invalid input.")

def createData(mysql_conn, mysql_cur):
    addingData = True
    while (addingData):
        print("\nThe following data is creatable:")
        print("\n1. New Pokémon")
        print("2. New Type")
        print("3. New Ability")
        print("4. Return to previous menu")
        inputSelection = input("\nEnter the option number of the data you wish to create: ")

        if (inputSelection == '1'):
            name = input("\nEnter a name for the new Pokémon: ")
            boolInput = input("Can this Pokémon Mega Evolve? (y/n)")
            if (boolInput.upper() == 'Y'):
                mega = True
            else:
                mega = False
            boolInput = input("Can this Pokémon Gigantimax? (y/n)")
            if (boolInput.upper() == 'Y'):
                gmax = True
            else:
                gmax = False
            typeone = input("Enter a first type for the new Pokémon: ")
            typetwo = input("Enter a second type for the new Pokémon (If no second type, enter 'NONE'): ")
            ability = input("Enter an ability name for the new Pokémon: ")

            try:
                createPokemon(mysql_cur, name.upper(), mega, gmax, typeone.upper(), typetwo.upper(), ability.upper())
                mysql_conn.commit()
            except:
                print("\nERROR. Invalid input during Pokémon creation.")

        elif (inputSelection == '2'):
            name = input("Enter a name for the new Type: ")
            temp = input("Enter the type advantages for the new Type (FORMATTING EXAMPLE: BUG, GHOST, DARK): ")
            adv = temp.upper()
            temp = input("Enter the type disadvantages for the new Type (FORMATTING EXAMPLE: BUG, GHOST, DARK): ")
            disadv = temp.upper()

            try:
                createType(mysql_cur, name.upper(), adv, disadv)
                mysql_conn.commit()
            except:
                print("\nERROR. Invalid input during Type creation.")

        elif (inputSelection == '3'):
            name = input("Enter a name for the new Ability: ")
            desc = input("Enter a description for the new Ability (100 character MAX): ")

            try:
                createAbility(mysql_cur, name.upper(), desc)
                mysql_conn.commit()
            except:
                print("\nERROR. Invalid input during Ability creation.")

        elif (inputSelection == '4'):
            print("Returning to previous menu..\n")
            addingData = False
        else:
            print("ERROR. Invalid input.")

def updateData(mysql_conn, mysql_cur):
    updatingData = True
    while (updatingData):
        print("\nThe following data is updatable: ")
        print("\n1. Pokémon")
        print("2. Types")
        print("3. Abilities")
        print("4. Return to previous menu")

        inputSelection = input("\nEnter the option of the data you wish to update: ")
        if (inputSelection == '1'):
            print("\nEnter the option of the Pokémon data you wish to update: ")
            print("\n1. Name")
            print("2. First Type")
            print("3. Second Type")
            print("4. Ability")
            print("5. Return to previous menu")

            while (True):
                inputSelection = input("\nPlease select an option: ")
                if (inputSelection == '1'):
                    currPokeName = input("Please enter the Pokemon's current name that you would like to change: ")
                    oldPokeName = input("Please enter the Pokemon's new name: ")
                    try:
                        updatePkmnName(mysql_cur, currPokeName.upper(), newPokeName.upper())
                        mysql_conn.commit()
                    except:
                        print("ERROR. Invalid input.")
                    break
                elif (inputSelection == '2'):
                    pokeName = input("Please enter the name of the Pokemon whose type you would like to update: ")
                    newTypeOne = input("Please enter the name of the new Type: ")
                    try:
                        updatePkmnTypeOne(mysql_cur, pokeName.upper(), newTypeOne.upper())
                        mysql_conn.commit()
                    except:
                        print("ERROR. Invalid input.")
                    break
                elif (inputSelection == '3'):
                    pokeName = input("Please enter the name of the Pokemon whose type you would like to update: ")
                    newTypeTwo = input("Please enter the name of the new Type: ")
                    try:
                        updatePkmnTypeTwo(mysql_cur, pokeName.upper(), newTypeTwo.upper())
                        mysql_conn.commit()
                    except:
                        print("ERROR. Invalid input.")
                    break
                elif (inputSelection == '4'):
                    currPokeAbility = input("Please enter the Pokemon's current Ability that you would like to change: ")
                    oldPokeAbility = input("Please enter the Pokemon's new Ability: ")
                    try:
                        updatePkmnAbility(mysql_cur, currPokeAbility.upper(), newPokeAbility.upper())
                        mysql_conn.commit()
                    except:
                        print("ERROR. Invalid input.")
                    break
                elif (inputSelection == '5'):
                    print("Returning to previous menu..\n")
                    break
                else:
                    print("\nERROR. Invalid input.")

        elif (inputSelection == '2'):
            curTypeName = input("Enter the name of the Type to be updated: ")
            newTypeName = input(f"Enter a new name for the Type {curTypeName.upper()}: ")
            try:
                updateTypeName(mysql_cur, curTypeName.upper(), newTypeName.upper())
                mysql_conn.commit()
            except:
                print("ERROR. Invalid input.")

        elif (inputSelection == '3'):
            curAbilityName = input("Enter the name of the Ability to be updated: ")
            newAbilityName = input(f"Enter the new name for the Ability {curAbilityName.upper()}: ")
            try:
                updateAbilityName(mysql_cur, curAbilityName.upper(), newAbilityName.upper())
                mysql_conn.commit()
            except:
                print("ERROR. Invalid input.")

        elif (inputSelection == '4'):
            print("Returning to previous menu..\n")
            updatingData = False

        else:
            print("\nERROR. Invalid input.")

def deleteData(mysql_conn, mysql_cur):
    deletingData = True
    while (deletingData):
        print("\nThe following data is deletable?")
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
                    pokeName = input("\nPlease enter the Pokémon's Name: ")
                    try:
                        deletePkmnByName(mysql_cur, pokeName.upper())
                        mysql_conn.commit()
                        print(f"SUCCESS. Pokémon {pokeName} has been deleted.")
                    except:
                        print("ERROR. Invalid Pokémon name")
                    break
                elif (inputSelection == '2'):
                    dexNum = input("\nPlease enter the Pokedex Number(ID): ")
                    try:
                        deletePkmnByID(mysql_cur, dexNum)
                        mysql_conn.commit()
                        print(f"SUCCESS. Pokémon at Pokédex number {dexNum} has been deleted.")
                    except:
                        print("ERROR. Invalid Pokédex number.")
                    break
                else:
                    print("\nERROR. Invalid input.")

        elif (inputSelection == '2'):
            typeName = input("\nEnter the name of the Type to be deleted: ")
            try:
                deleteTypeByName(mysql_cur, typeName.upper())
                mysql_conn.commit()
                print(f"SUCCESS. Type {typeName.upper()} has been deleted.")
            except:
                print("ERROR. Invalid Type.")

        elif (inputSelection == '3'):
            abilityName = input("\nEnter the name of the Ability to be deleted: ")
            try:
                deleteAbilityByName(mysql_cur, abilityName.upper())
                mysql_conn.commit()
                print(f"SUCCESS. Ability {abilityName.upper()} has been deleted.")
            except:
                print("ERROR. Invalid Ability.")


# MAIN FUNCTION
def main():
    mysql_conn = create_mysql_connection(db_user='root', db_password='rMxtwa024OfAi7iF', host_name='35.226.194.71', db_name='PokemonDB')
    #mysql_conn = create_mysql_connection(db_user='root', db_password='password', host_name='104.197.101.227', db_name='PokemonDB')
    mysql_cur = mysql_conn.cursor()
    isRunning = True

    print("\nWelcome to The Pokémon Database!")
    print("- - - - -")

    while (isRunning == True):
        print("The following services are offered:")
        print("\n1. Search for Pokémon-related data")
        print("2. Add new Pokémon-related data")
        print("3. Update an existing data entry")
        print("4. Delete an existing data entry")
        print("5. Exit")

        inputSelection = input("\nEnter an option: ")

        if (inputSelection == '1'):
            readData(mysql_cur)
        elif (inputSelection == '2'):
            createData(mysql_conn, mysql_cur)
        elif (inputSelection == '3'):
            updateData(mysql_conn, mysql_cur)
        elif (inputSelection == '4'):
            deleteData(mysql_conn, mysql_cur)
        elif (inputSelection == '5'):
            print("\nThank you for using The Pokémon Database! Now exiting...\n")
            isRunning = False
        else:
            print("\nERROR. Invalid input.")

if __name__ == "__main__":
    main()
