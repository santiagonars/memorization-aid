#-----------------------------NOTES:------------------------------------
# - terminal shortcut: Documents/Github/memorization-app
# - 
#-----------------------MAINE OBJECTIVES:-------------------------------
#  - Just do a simple demonstration that it will work to practice skills
#  - no need to include GUI yet
#  - Keep it simple for now!!!
#-----------------------------TODO:-------------------------------------
# 1) look at similar projects to online to spark ideas - (DONE)
# 2) Implement extracting questions & answeres from .txt file to use as a database - (DONE)
# 3) Implement saving questions & answers in the .txt file
# 4) Implement global variables functionality

cards =[]

def main():
    cards =[]
    LoadFile(cards)

    '''with open("topicname.txt", "r") as dfile:
        #for line in iter(dfile.readline, ''):
        for line in dfile:
            temp = eval(line)
            cards.append(temp)
            print(cards)
    '''        

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
'''
def SaveQuestion(question, answer):
    
    new = [question,answer]
    cards.append(new) 
    print(cards)

    result = SaveAnotherQuestion(cards)
    print(result)

def SaveAnotherQuestion(cards):
    print("Would you like to add another question?")
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
        return print("Enter yes or no")     
'''
     
if __name__ == '__main__':
    main()