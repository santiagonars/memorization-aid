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
# - Improve menu with sonsole-menu library (https://pypi.org/project/console-menu/)

global cards
cards =[]

def main():
    loadFile()
    menu()


def menu():
    width = 60
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
    width = 60
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
        print('Only type a number from one of the available options and press enter')
        menuResponse()


def loadFile():
    with open("topicname.txt", "r") as dfile:
        #for line in iter(dfile.readline, ''):
        for line in dfile:
            temp = eval(line)
            cards.append(temp)
        # print(cards) 


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
        menu()


def saveAnotherQuestion():
    saveQuestion()


def viewQuestionList():
    print(cards)
    #print('which topic list would you like to view?')


def addNewTopicList():
    pass


def deleteQuestion():
    pass


if __name__ == '__main__':  
    main()