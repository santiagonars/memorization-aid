#---------Main objective:----------
#  - Just do a simple demonstration that it will work to practice skills
#  - no need to include GUI
#  - Keep it simple for now!!!

#--------------To do:-------------
# 1) do research in OOB (object oriented programming) for python / read the articles - watch videos
#      - read the articles / watch videos 
# 2) look at similar projects online
# 3) read to learn to connect to database: http://www.postgresqltutorial.com/postgresql-python/connect/

topic =[]

def SaveQuestion(question, answer):
    
    new = [question,answer]
    topic.append(new)  # ERROR HERE: need to make it so that it keeps the data 
    print(topic)

    print("Would you like to add another question?")
    response = input().strip()
    SaveAnotherQuestion(response, topic)
    
def SaveAnotherQuestion(response, topic):
    if response == 'y' or 'yes':
        print("What question would you like to save?")
        question = input().strip()
        print("What is the answer for the question?")
        answer = input().strip()

        SaveQuestion(question, answer)
    elif response == 'n' or 'no':
        print(topic)
    else:
        print("Enter yes or no")


if __name__ == '__main__':

    print("What question would you like to save?")
    question = input().strip()

    print("What is the answer for the question?")
    answer = input().strip()

    SaveQuestion(question, answer)

