##############################################################################
# Exercise 1: Importing modules
##############################################################################
from random import randint
from os import remove, rename

##############################################################################
# Exercise 2: Getting the user's score
##############################################################################
# Define function
def getUserPoint(userName):

    # Code to run if the file is present
    try:           
        inputFile = open('userScores.txt', 'r')
        for line in inputFile:
            content = line.split(',')
            if content[0] == userName:
                inputFile.close()
                return content[1]
        inputFile.close()
        return "-1"
    
    # Code to run if the file is not present
    except IOError:
        print("File not found")
        createFile = open('userScores.txt', 'w')
        createFile.close()
        return "-1"

##############################################################################
# Exercise 3: Updating the user's score
##############################################################################
# Define function
def updateUserPoints(newUser, userName, score):
    if newUser == True:
        # Append user name and score to userScores.txt
        inputFile = open('userScores.txt', 'a')
        print('%s, %s' % (userName, score), file = inputFile)
        inputFile.close()
    elif newUser == False:
    # Update the user's score in the file by creating a temporary file
        tempFile = open('userScores.tmp', 'w')
        inputFile = open('userScores.txt', 'r')
        content = []
        userNameList = []
        userScoreList = []
        i = 0
        # Loop through the old file and get all the names and scores
        for line in inputFile:
            content = line.split(',')
            userNameList.append(str(content[0]))
            userScoreList.append(int(content[1]))
            # Update the score if necessary
            if (userNameList[i] == userName): # and (userScoreList[i] != score):
                userScoreList[i] = score
            # Copy across to the temp file                             
            print('%s, %s' % (userNameList[i], userScoreList[i]), file = tempFile, end='\n')
            i = i+1
        inputFile.close()
        tempFile.close()
        remove("userScores.txt")
        rename("userScores.tmp", "userScores.txt")
# End of function

##############################################################################
# Exercise 4: Generating the questions
##############################################################################
# Define function
def genQuestion():
    # Initialise two lists and one dictionary
    operandList = [0] * 5
    operatorList = [''] * 4
    operatorDict = {1:"+", 2:"-", 3:"*", 4:"**"}
    
    # Randomly generate our operands (random integers between 1 and 9)
    operandList[:] = [randint(1, 9) for i in operandList]
    # Randomly generate our operators, with the restriction that we cannot have 
    # consecutive "**" operators
    for i in range(len(operatorList)):
        # If it's the first operator, no restrictions on what ooerator we can have
        if i == 0:
            operatorList[i] = operatorDict[randint(1, 4)]
        # If the previous operator was "**", can't have it again, so can only have
        # the first three items in the dictionary
        elif operatorList[i-1] == "**":
            operatorList[i] = operatorDict[randint(1, 3)]
        # If previous operator wasn't "**", no restrictions on what ooerator we can have
        else:
            operatorList[i] = operatorDict[randint(1, 4)]
    
    # Concatenate values from the two lists into a string (the question)
    questionString = str(operandList[0])
    for i in range(1, len(operatorList)+1):
        questionString = questionString + str(operatorList[i-1])+ str(operandList[i])
    # Evaluate the string to get the answer
    result = eval(questionString)
    
    # Interact with the user
    # Replace "**" with "^" because most people don't know what "**" means
    questionString = questionString.replace("**","^")
    print(questionString)
    
    # Ask the user to enter the correct answer
    userResult = input("Enter the correct answer: ")
    
    while True:
        try:
            userResult = int(userResult)
            if userResult == result:
                print("Correct")
                return 1
            else: 
                print("Incorrect. The answer is ", result)
                return 0
        except Exception as e:
            print("Please enter an integer.")
            userResult = input("Enter the correct answer: ")
