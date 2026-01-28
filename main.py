#------------------
#Libraries
#------------------
import requests

#------------------
#Global Variables
#------------------
password = ""

URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"
#------------------
#Subroutines
#------------------
def getUserInput():
    userInput = input("Enter a password you would like to check: ")

    return userInput

def extractWords(pPassword):
    word = ""
    tempList = []

    pPassword = list(pPassword)

    for i, character in enumerate(pPassword):
        if character.isalpha():
            word += character

        if not(character.isalpha()) and (word != ""): #Check if the word has ended then appends to list.
            tempList.append(word)
            word = ""

        # Check if it's the final character in the password
        if character.isalpha() and i == len(pPassword) - 1:
            tempList.append(word)
            word = ""

    return tempList

def checkAPI(pList):
    print("\nFetching from API")

    totalWords, dictionaryWords = 0, 0

    for word in pList:
        response = requests.get(URL + word)

        if response.status_code != 200: #Code 200 represents a successful request
            print("Word is not in the dictionary / Other Error")
            totalWords += 1

        else:
            print("Word is in the dictionary")
            dictionaryWords += 1
            totalWords += 1

    return totalWords, dictionaryWords

def calculateStrength(pPassword, pList): #Uses criteria in README to evaluate strength
    score = 0

    upperCount = 0
    lowerCount = 0
    symbolCount = 0
    numCount = 0

    multiplier = 0

    #Loops through password checking each character, adds to a running total to see what criteria is met
    for character in pPassword:
        if character.isupper():
            upperCount += 1

        elif character.islower():
            lowerCount += 1

        elif not(character.isalnum()):
            symbolCount += 1

        elif character.isnumeric():
            numCount += 1

    #Gives points based on whether uppercase and lowercase is used
    if upperCount > 0 and lowerCount > 0:
        print("Both uppercase and lowercase used (+3)")
        score += 3

    elif upperCount > 0 or lowerCount > 0:
        print("Password is all uppercase or lowercase (+2)")
        score += 2

    else:
        print("No letters used (0)")

    #Gives points based on whether numbers and special characters are used
    if symbolCount > 0 and numCount > 0:
        print("Numbers and special characters used (+3)")
        score += 3

    elif symbolCount > 0 or numCount > 0:
        print("Only numbers used or only special characters used (+1)")
        score += 1

    else:
        print("No numbers or special characters used (0)")

    #Checks password length and gives points based off it
    if len(pPassword) >= 15:
        print("Password is very long (+4)")
        score += 4

    elif len(pPassword) >= 10:
        print("Password has a medium length (+2)")
        score += 2

    else:
        print("Password is short (0)")

    totalWords, dictionaryWords = checkAPI(pList)

    #Avoid division by zero (error)
    if totalWords > 0:
        multiplier = round(max(0.5, 1.0 - 0.5 * (dictionaryWords / totalWords)), 2)

    else:
        multiplier = 1.0

    #Checks how many of the total words used come from the dictionary which would make the password weaker
    if totalWords == 0:
        print("No words in your password\nScore will not be affected by a multiplier")

    elif totalWords == dictionaryWords:
        score *= 0.5
        print("\nDue to having 100% of your words in your password being in the dictionary\nScore is multiplied by 0.5")

    else:
        score *= multiplier
        print(f"\nDue to having {round((dictionaryWords / totalWords) * 100, 2)}% of words in your password being in the dictionary\nYour score is multiplied by {multiplier}")

    #Outputs score rounded to 2d.p
    print(f"score is {round(score, 2)}/10")

#------------------
# Main Program
#------------------
#Subroutine calls
password = getUserInput()
wordList = extractWords(password)
calculateStrength(password, wordList)