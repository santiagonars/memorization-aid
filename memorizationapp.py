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
# - Add menu functionality
# - Add function to view questions & answers (transversing and random)
# - Add timer to do perform practice sessions
# - Add option to delete a question&answer
# - Add function to create separate text file by area of knowledge
# - Add option to edit a question&answer
# - Add parameter that allows one to archive a question
# - Improve functionality to save another variable
# - Improve global variables functionality
# - Improve capability to write new data to .txt file

cards =[]

def main():
    #TODO: menu()
    print("Would you like to add a question?")
    response = input().strip()
    if response == "yes":
        SaveQuestion()
    else:
        pass     
    '''print("What question would you like to save?")
    question = input().strip()
    print("What is the answer for the question?")
    answer = input().strip()

    SaveQuestion(question, answer)
    '''

def LoadFile(cards):
    with open("topicname.txt", "r") as dfile:
        #for line in iter(dfile.readline, ''):
        for line in dfile:
            temp = eval(line)
            cards.append(temp)
        print(cards) 

def SaveQuestion():
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
        SaveAnotherQuestion()
    else:
        pass

def SaveAnotherQuestion():
    SaveQuestion()
    
"""     print("Would you like to add another question?")
    response = input().strip()
    if (response == "yes" or "y"):
        print("What question would you like to save?")
        question = input().strip()
        print("What is the answer for the question?")
        answer = input().strip()

        SaveQuestion(question, answer)
        
    elif (response == "no" or "n"): #ERROR! not working
        return print(cards)
    else:
        return print("Enter yes or no")   """
    

if __name__ == '__main__':
    LoadFile(cards)
    main()