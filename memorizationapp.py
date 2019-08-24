#-----------------------------NOTES:------------------------------------
# - terminal shortcut: Documents/Github/memorization-app
# - 
#-----------------------MAIN OBJECTIVES:-------------------------------
#  - Just do a simple demonstration that it will work to practice skills
#  - no need to include GUI yet
#  - Keep it simple for now!!!
#---------------------------BACKLOG:TODO:------------------------------_
# - look at similar projects to online to spark ideas - (DONE)
# - Implement extracting questions&answers from .txt file to use as a database - (DONE)
# - Implement saving questions & answers in the .txt file - (DONE)
# - TODO: Add menu functionality 
# - Add function to view questions & answers (transversing and random)
# - Add timer to do perform practice sessions
# - Add option to delete a question&answer
# - Add function to create separate text file by area of knowledge
# - Add option to edit a question&answer
# - Add parameter that allows one to archive a question
# - Improve functionality to save another variable
# - Improve global variables functionality
# - Improve capability to write new data to .txt file

global cards
cards =[]

def main():
    #TODO: menu()
    print("Would you like to add a question?")
    response = input().strip()
    if response == "yes":
        saveQuestion()
    else:
        pass     


def menu():
    pass

def loadFile():
    with open("topicname.txt", "r") as dfile:
        #for line in iter(dfile.readline, ''):
        for line in dfile:
            temp = eval(line)
            cards.append(temp)
        print(cards) 


def saveQuestion():
    print("Type the 'Question': ")
    question = input().strip()
    print("Type the 'Answer': ")
    answer = input().strip()
    new = [question,answer]
    cards.append(new) 
    print(cards)

    with open("topicname.txt", "w") as dfile:
        for line in cards:
            # TODO: add function so it doesnt rewrite entire file
            dfile.write("%s\n" % line)
    
    print("Would you like save another question?")
    response = input().strip()
    if response == "yes":
        saveAnotherQuestion()
    else:
        pass


def saveAnotherQuestion():
    saveQuestion()
    

if __name__ == '__main__':
    loadFile()
    main()