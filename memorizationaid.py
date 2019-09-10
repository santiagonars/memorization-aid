#---------------------------NOTES:-------------------------------------
# - NOTE: sonsole-menu library (https://pypi.org/project/console-menu/)
# - 
#---------------------------BACKLOG:------------------------------------
# - TODO: Add timer to practice sessions
# - TODO: Add option to delete a list
# - (MAYBE)TODO: loadFile() - option when id response not in list 
# - (MAYBE)TODO: Add option to edit a question&answer
# - (MAYBE)TODO: Add parameter that allows one to archive a question
# - (MAYBE)TODO: Improve global variables functionality
# - (MAYBE)TODO: Improve capability to write new data to .txt file
#---------------------------BUGS:------------------------------------
# - BUG: 

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
    option = input().strip()
    print('-'.center(width, '-'))
    if option == '1':
        loadFile()
        practiceSession()
    elif option == '2':
        loadFile()
        saveQuestion()
    elif option == '3':
        createNewTopicList()
    elif option == '4':
        loadFile()
        deleteQuestion()
    elif option == '5':
        loadFile()
        viewQuestionList()
    elif option == '6':
        exit
    else:
        print('>>> Only type a number from the available options and press enter!')
        menuResponse()


def loadFile():
    topics = []
    tname.clear()
    cards.clear()
    width = 25
    # create a list with all text files in local directory
    for file in glob.glob("*.txt"):
        topics.append(file)
    print('ID - Topic file name')
    print('-'.center(width, '-'))
    # display names of lists of topics
    for i, name in enumerate(topics, start=1):
        print(i,'-',name)
    print('-'.center(width, '-'))
    # prompt user to select a topic list to work on
    print('>>> Enter topic ID: (q to exit)')
    response = input().strip()
    if response == 'q':
        menu()
    elif response == '':
        print('Please Enter a valid option!\n')
        loadFile()
    else:
        for i,name in enumerate(topics, start=1):
            if i == int(response):
                # add name of topic list been worked on
                tname.append(name)
                with open(name, "r") as dfile:
                    for line in dfile:
                        # eval(): value needs to be defined (file must be empty or in correct format)
                        temp = eval(line) 
                        cards.append(temp)
    # TODO: option when id response not in list


def randomQuestion():
    # shuffle lists in cards 
    r = list(cards)
    random.shuffle(r)
    return r


def practiceSession():
    shuffList = randomQuestion() #shuffled cards list
    width = 50
    print('>>> *Press Return to see answer and continue'.ljust(width,'-'))
    print('>>> *Enter any character to skip'.ljust(width,'-'))
    print('>>> *Enter q to quit'.ljust(width,'-'))
    print('-'.center(width,'-'))
    # iterate through shuffle nested list
    for i in shuffList:
        ques = i[0] # save question 
        ans = i[1] # save answer 
        print('QUESTION: ', ques)
        response = input().strip()
        # user presses return or enter key
        if response == '': 
            print('ANSWER: ', ans)
            print('-'.center(width,'-'))
            # reached end of list
            if i[0] == shuffList[len(shuffList)-1][0]:
                print('Congrats! You have reached the end of the list!\n')
                input(">>> Press Enter to continue...")
        # quit practice session
        elif response == 'q': 
            break
        # enter any character doesnt display answer to question
        else: 
            print('-'.center(width,'-'))
            # reached end of list
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
    
    saveFile() # stored cards list of question and answer in text file
    
    print("Would you like save another question?")
    response = input().strip()
    if response == "yes" or response == "y":
        saveQuestion()
    else:
        menu() 


def createNewTopicList():
    topics = list()
    # prompt user to type name of topic/area of knowledge to create list name
    print('>>> Select a TOPIC name for the new list:')
    response = str(input().strip())
    name = response + '_topic.txt'
    # get topic names already used 
    for file in glob.glob("*.txt"):
        topics.append(file)
    # statement that compares selected topic name to any of the names in existing lists of topic name
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
    # diplay tabled list of questions & corresponding answers of loaded topic list
    print('ID - QUESTION : ANSWER')
    print('-'.center(25, '-'))
    for i,line in enumerate(cards, start=1):
        print(i, "-",line[0],':',line[1])
    print('-'.center(25, '-'))
    # prompt user to select id of question & corresponding answer to delete
    print('>>> Enter ID to delete (q to quit):')
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
    # diplay tabled list of questions & corresponding answers of loaded topic list
    print('ID - QUESTION : ANSWER')
    print('-'.center(25, '-'))
    for i,line in enumerate(cards, start=1):
        print(i, "-",line[0],':',line[1])
    print('-'.center(25, '-'))
    # prompt user to view a new list
    print("Would you like view another list?")
    response = input().strip()
    if response == 'yes' or response == 'y':
        loadFile()
        viewQuestionList()
    else:
        menu()          


if __name__ == '__main__':  
    main()