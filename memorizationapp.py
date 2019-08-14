#-----------------------------NOTES:------------------------------------
# - terminal shortcut: Documents/Github/memorization-app
#-----------------------MAINE OBJECTIVES:-------------------------------
#  - Just do a simple demonstration that it will work to practice skills
#  - no need to include GUI
#  - Keep it simple for now!!!
#-----------------------------TODO:-------------------------------------
# 1) do research in OOB (object oriented programming)
#     - read the articles / watch videos 
# 2) look at similar projects online
# 3) read to learn to connect to a database:
#     - http://www.postgresqltutorial.com/postgresql-python/connect/

topic =[]

def main():
    print("What question would you like to save?")
    question = input().strip()
    print("What is the answer for the question?")
    answer = input().strip()

    SaveQuestion(question, answer)


def SaveQuestion(question, answer):
    
    new = [question,answer]
    topic.append(new) 
    print(topic)

    result = SaveAnotherQuestion(topic)
    print(result)

def SaveAnotherQuestion(topic):
    print("Would you like to add another question?")
    response = input().strip()
    if (response == "yes" or "y"):
        print("What question would you like to save?")
        question = input().strip()
        print("What is the answer for the question?")
        answer = input().strip()

        SaveQuestion(question, answer)
        
    elif (response == "no" or "n"): # ERROR: not working for this case!!! 
        return print(topic)
    else:
        return print("Enter yes or no")     

     
if __name__ == '__main__':
    main()