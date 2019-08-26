#-----------------------------NOTES:------------------------------------
# - terminal shortcut: Documents/Github/memorization-app
# - 
#-----------------------MAIN OBJECTIVES:-------------------------------
#  - Just do a simple demonstration that it will work to practice skills
#  - no need to include GUI yet
#  - Keep it simple for now!!!
#---------------------------BACKLOG:TODO:------------------------------
# - look at similar projects to online to spark ideas - (DONE)
# - Implement extracting questions&answers from .txt file to use as a database - (DONE)
# - Implement saving questions & answers in the .txt file - (DONE)
# - Add menu functionality (DONE)
# - Add function to view questions (DONE)
# - Add function to create a random questions list (DONE)
# - Add function to perform a practice session
# - Add timer to practice sessions
# - Add option to delete a question&answer
# - Add function to create separate text file by area of knowledge
# - Add option to edit a question&answer
# - Add parameter that allows one to archive a question
# - Improve functionality to save another variable
# - Improve global variables functionality
# - Improve capability to write new data to .txt file
# - Improve menu with sonsole-menu library (https://pypi.org/project/console-menu/)
import random


global cards
cards =[]

def main():
    loadFile()
    menu()


def menu():
    width = 70
    for l in range(2):
        l = '-'.center(width,'-')
        print(l)
    print('Practice Memorization'.center(width, '-'))
    for l in range(2):
        l = '-'.center(width,'-')
        print(l)
    print('-----Select an Option:'.ljust(width, '-'))
    print('-'.center(width, '-'))
    print('-------(1) Start a practice session')
    print('-------(2) Add a new question')
    print('-------(3) Create a new topic list')
    print('-------(4) Delete questions')
    print('-------(5) View list of questions')
    print('-------(6) Exit')
    menuResponse()


def menuResponse():
    width = 70
    response = input().strip()
    print('-'.center(width, '-'))
    if response == '1':
        saveQuestion()
    elif response == '2':
        saveQuestion()
    elif response == '3':
        pass
    elif response == '4':
        pass
    elif response == '5':
        viewQuestionList()
    elif response == '6':
        exit
    else:
        print('!! Only type a number from the available options and press enter')
        menuResponse()


def loadFile():
    with open("topicname.txt", "r") as dfile:
        #for line in iter(dfile.readline, ''):
        for line in dfile:
            temp = eval(line)
            cards.append(temp)
        # print(cards) 


def randomQuestion():
    r = list(cards)
    random.shuffle(r)
    print("After Reshuffling list : ", r)


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
    if response == "yes" or response == "y":
        saveQuestion()
    else:
        menu()


def viewQuestionList():
    # TODO: Ask user what list to view 
    print('ID - QUESTION : ANSWER')
    print('-'.center(25, '-'))
    for i,line in enumerate(cards, start=1):
        print(i, "-",line[0],':',line[1])
    print('-'.center(25, '-'))

    print("Would you like view another list?")
    response = input().strip()
    if response == 'yes' or response == 'y':
        # TODO: Ask user what list to view 
        viewQuestionList()
    else:
        menu()


def addNewTopicList():
    pass


def deleteQuestion():
    pass


if __name__ == '__main__':  
    main()