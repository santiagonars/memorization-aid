#---------------------------NOTES:------------------------------------
# - NOTE: sonsole-menu library (https://pypi.org/project/console-menu/)
# - 
#---------------------------BACKLOG:------------------------------------
# - TODO: Add a pause to to require user to press any key before go back to menu for many of the functions (DONE)
# - TODO: Add timer to practice sessions
# - TODO: Add comments throughout code
# - TODO: Add project info in README file in github
# - TODO: Add option to delete a list
# - TODO: loadFile() - option when id response not in list
# - (MAYBE)TODO: Add option to edit a question&answer
# - (MAYBE)TODO: Add parameter that allows one to archive a question
# - (MAYBE)TODO: Improve global variables functionality
# - (MAYBE)TODO: Improve capability to write new data to .txt file

import random
import glob


global cards, tname
cards = list()
tname = list()

def main():
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
        loadFile()
        practiceSession()
    elif response == '2':
        loadFile()
        saveQuestion()
    elif response == '3':
        createNewTopicList()
    elif response == '4':
        loadFile()
        deleteQuestion()
    elif response == '5':
        loadFile()
        viewQuestionList()
    elif response == '6':
        exit
    else:
        print('>>> Only type a number from the available options and press enter!')
        menuResponse()


def loadFile():
    # ALT: add a new parameter to the first list that accounts for topic name and index each time to work this those values
    topics = []
    tname.clear()
    cards.clear()
    width = 25
    for file in glob.glob("*.txt"):
        topics.append(file)
    print('ID - Topic file name')
    print('-'.center(width, '-'))
    for i, name in enumerate(topics, start=1):
        print(i,'-',name)
    print('-'.center(width, '-'))
    print('>>> Enter topic ID: (q to exit)')
    response = input().strip()
    if response == 'q':
        menu()
    else:
        for i,name in enumerate(topics, start=1):
            if i == int(response):
                tname.append(name)
                with open(name, "r") as dfile:
                    for line in dfile:
                        temp = eval(line) # eval(): value needs to be defined (file must be empty or in correct format)
                        cards.append(temp)
    # TODO: option when id response not in list


def randomQuestion():
    r = list(cards)
    random.shuffle(r)
    return r


def practiceSession():
    shuffList = randomQuestion()
    width = 50
    print('>>> *Press Return to see answer and continue'.ljust(width,'-'))
    print('>>> *Enter any character to skip'.ljust(width,'-'))
    print('>>> *Enter q to quit'.ljust(width,'-'))
    print('-'.center(width,'-'))
    for i in shuffList:
        ques = i[0]
        ans = i[1]
        print('QUESTION: ', ques)
        response = input().strip()
        if response == '':
            print('ANSWER: ', ans)
            print('-'.center(width,'-'))
            if i[0] == shuffList[len(shuffList)-1][0]:
                print('Congrats! You have reached the end of the list!\n')
                input(">>> Press Enter to continue...")
        elif response == 'q':
            break
        else:
            print('-'.center(width,'-'))
            if i[0] == shuffList[len(shuffList)-1][0]:
                print('Congrats! You have reached the end of the list!\n')
                input(">>> Press Enter to continue...")
            next
    menu()


def saveFile():
    # print('tname before saving file: ', tname)
    n = tname[0]
    with open(n, "w") as dfile:
        for line in cards:
            # TODO: add function so it doesnt rewrite entire file
            dfile.write("%s\n" % line)


def saveQuestion():
    print("Type the QUESTION: ")
    question = input().strip()
    print("Type the ANSWER: ")
    answer = input().strip()
    new = [question,answer]
    cards.append(new) 

    saveFile()
    # TODO: Add argument so code below doesn't execute for the delete function
    print("Would you like save another question?")
    response = input().strip()
    if response == "yes" or response == "y":
        saveQuestion()
    else:
        menu()


def createNewTopicList():
    topics = list()
    print('>>> Select a TOPIC name for the new list:')
    response = str(input().strip())
    name = response + '_topic.txt'
    # statement that compares name to any of the names in existing lists of topic name
    for file in glob.glob("*.txt"):
        topics.append(file)
    if (name in topics):
        print('Name already used! Please enter another name.\n')
        createNewTopicList()
    else:
        with open(name, 'w') as nfile:
            nfile.write('')
        print('\n',name,' has been created!\n')
        input(">>> Press Enter to continue...")
        menu()


def deleteQuestion():
    print('ID - QUESTION : ANSWER')
    print('-'.center(25, '-'))
    for i,line in enumerate(cards, start=1):
        print(i, "-",line[0],':',line[1])
    print('-'.center(25, '-'))
    print('>>> Enter ID to delete OR q to quit:')
    response = input().strip()
    if response == 'q':
        menu()
    else:
        for i,line in enumerate(cards, start=1):
            if i == int(response):
                cards.remove(line)
                saveFile()
                print(line, ' has been removed from the list!\n')
                input(">>> Press Enter to continue...")
                menu()
            # TODO: option when id response not in list.   


def viewQuestionList():
    print('ID - QUESTION : ANSWER')
    print('-'.center(25, '-'))
    for i,line in enumerate(cards, start=1):
        print(i, "-",line[0],':',line[1])
    print('-'.center(25, '-'))
    print("Would you like view another list?")
    response = input().strip()
    if response == 'yes' or response == 'y':
        loadFile()
        viewQuestionList()
    else:
        menu()          


if __name__ == '__main__':  
    main()