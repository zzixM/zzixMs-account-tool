import random
import json

# Python Account Tool made by zzixM
# instagram handle: @zzixm_
# github handle: https://github.com/zzixM
# encryption for passwords might be added in the future
# time when the encryption functions will be added isnt decided yet.

def passwordGen():
    uppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercaseLetters = uppercaseLetters.lower()
    didgits = "0123456789"
    specialChrs =  "!?_#@:;\\/*."

    upper, lower, nums, special = True, True, True, True

    all = ""
    if upper:
        all += uppercaseLetters
    if lower:
        all += lowercaseLetters
    if nums:
        all += didgits
    if special:
        all += specialChrs

    validLength = False
    while validLength == False:
        length = input(str("How long do you want the passwords to be? "))

        try:
            length = int(length)

            if length > 3 and length < 25:
                validLength = True
            else:
                print("Please keep the length between 4 and 24. \n")
    
        except TypeError as e:
            print("Please enter an number between 4 and 24\n")
    
        except ValueError as e:
            print("Please enter an number between 4 and 24\n")
    

    validAmount = False
    while validAmount == False:
        amount = input(str("How many passwords do you want? "))

        try:
            amount = int(amount)

            if amount > 1 and amount < 21:
                validAmount = True
            else:
                print("please keep the amount between 2 and 20\n")
    
        except TypeError as e:
            print("Please enter an number between 2 and 20\n")
    
        except ValueError as e:
            print("Please enter an number between 2 and 20\n")
    
    print(f"\nGenerating passwords of length \"{length}\".")
    print(f"\nGenerating \"{amount}\" passwords.\n")

    choicNum = 0  
    passwords = {
        
    }
    passwords["passwords"] = []

    for x in range(amount):
        password = "".join(random.sample(all, length))
        print(f"Password {choicNum} = {password}")
        choicNum = choicNum + 1 

        passwords["passwords"].append({choicNum : password})

    validUserChoice = False
    while validUserChoice == False:
        userChoice = input(str("\nWARNING: Do you want to save the generated passwords to a file?\nNote: the passwords will be saved in plain text. "))
        userChoice.lower()

        if userChoice == "yes":
            savePasswords(passwords)
            validUserChoice = True
    
        elif userChoice == "no":
            startMenu()
            validUserChoice = True
    
        else:
            print("\nplease answer yes or no.\n")


def getPasswords():

    print("\nYour Passwords Are:\n")
    
    with open('passwords.json', 'r') as readFile:
        usersPasswords = json.load(readFile)
        print(usersPasswords)
        readFile.close()
    
    startMenu()

def savePasswords(passwords):

    validUserChoice = False
    while validUserChoice == False:
        userChoice = input(str("\nWARNING: You are about to save the generated passwords to a file. Are you sure?\nNote: the passwords will be saved in plain text. "))
        userChoice.lower()

        if userChoice == "yes":
            validUserChoice = True
    
        elif userChoice == "no":
            startMenu()
            validUserChoice = True
    
        else:
            print("\nplease answer yes or no.\n")
    
    with open ('passwords.json', 'w') as saveFile:
        json.dump(passwords, saveFile, indent = 4)
        print("Passwords saved")
        saveFile.close()
    
    startMenu()

def usernameGen():
    uppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercaseLetters = uppercaseLetters.lower()
    didgits = "0123456789"
    specialChrs =  " "

    upper, lower, nums, special = True, True, True, False

    all = ""
    if upper:
        all += uppercaseLetters
    if lower:
        all += lowercaseLetters
    if nums:
        all += didgits
    if special:
        all += specialChrs

    validLength = False
    while validLength == False:
        length = input(str("How long do you want the usernames to be? "))

        try:
            length = int(length)

            if length > 3 and length < 12:
                validLength = True
            else:
                print("Please keep the length between 4 and 11. \n")
    
        except TypeError as e:
            print("Please enter an number between 4 and 11\n")
    
        except ValueError as e:
            print("Please enter an number between 4 and 11\n")
    

    validAmount = False
    while validAmount == False:
        amount = input(str("How many usernames do you want? "))

        try:
            amount = int(amount)

            if amount > 1 and amount < 21:
                validAmount = True
            else:
                print("please keep the amount between 2 and 20\n")
            
        #except Exception as e:
            #print("")
    
        except TypeError as e:
            print("Please enter an number between 2 and 20\n")
    
        except ValueError as e:
            print("Please enter an number between 2 and 20\n")
    
    print(f"\nGenerating Usernames of length \"{length}\".")
    print(f"\nGenerating \"{amount}\" usernames.\n")

    choicNum = 0  
    usernames = {
        
    }
    usernames["Usernames"] = []

    for x in range(amount):
        usename = "".join(random.sample(all, length))
        print(f"Usename {choicNum} = {usename}")
        choicNum = choicNum + 1 

        usernames["Usernames"].append({choicNum : usename})

    validUserChoice = False
    while validUserChoice == False:
        userChoice = input(str("\nWARNING: Do you want to save the generated usernames to a file?\nNote: the usernames will be saved in plain text. "))
        userChoice.lower()

        if userChoice == "yes":
            saveUsernames(usernames)
            validUserChoice = True
    
        elif userChoice == "no":
            startMenu()
            validUserChoice = True
    
        else:
            print("\nplease answer yes or no.\n")

def saveUsernames(usernames):

    validUserChoice = False
    while validUserChoice == False:
        userChoice = input(str("\nWARNING: You are about to save the generated usenames to a file. Are you sure? "))
        userChoice.lower()

        if userChoice == "yes":
            validUserChoice = True
    
        elif userChoice == "no":
            startMenu()
            validUserChoice = True
    
        else:
            print("\nplease answer yes or no.\n")
    
    with open ('usernames.json', 'w') as saveFile:
        json.dump(usernames, saveFile, indent = 4)
        print("Usernames Saved")
        saveFile.close()
    
    startMenu()

def getUsernames():

    print("\nYour Usernames Are:\n")
    
    with open('usernames.json', 'r') as readFile:
        usersUsernames = json.load(readFile)
        print(usersUsernames, "\n")
        readFile.close()
    
    startMenu()

def credits():
    print("\nPython Account Tool made by zzixM")
    print("Instagram handle: @zzixm_")
    print("Github handle: https://github.com/zzixM")
    startMenu()

def startMenu():
    
    print("")
    print("Welcome to zzixMs account tool!\n")
    userChoice = input(str("Would you like to: \n1. Generate a Passwords \n2. Read Your Passwords\n3. Make Usernames\n4. Read Your Usernames\n5. Credits\n6. Exit\n> "))

    if userChoice == "1":
        passwordGen()
    
    elif userChoice == "2":
        getPasswords()

    elif userChoice == "3":
        usernameGen()

    elif userChoice == "4":
        getUsernames()

    elif userChoice == "5":
        credits()

    elif userChoice == "6":
        exit()
    
    else:
        startMenu()

if __name__ == "__main__":
    startMenu()