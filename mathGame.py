
##############################################################################
# Exercise 5: Writing the main program
##############################################################################

# Import the myPythonFunctions module
from myPythonFunctions import getUserPoint, updateUserPoints, genQuestion
# Prompt for user name
userName = input("What is your user name: ")
# Get the score associated with that name
userScore = getUserPoint(userName)
# getUserPoint returns a -1 if the user is not found
if userScore == "-1":
    newUser = True
else:
    newUser = False
if newUser == True:
    userScore = 0 # Set a new user's score to zero    
# Step 1    
userChoice = 0
# Step 2
while userChoice != "-1":
    # Step 3
    userScore = userScore + genQuestion()
    # Step 4
    userChoice = input("Enter 0 to continue or -1 to quit: ")
    
# Update user score if the user quits
updateUserPoints(newUser, userName, userScore)