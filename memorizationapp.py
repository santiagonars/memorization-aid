#----To do:----
# - 
# - 
# - 


def SaveQuestion(question, answer):

    topic = [[question,answer]]
    
    response = topic

    '''if question in topic and answer in topic:
        response = "Your answer has been saved"
    else:
        response = "Error. Unable to save question."'''
    return response


if __name__ == '__main__':
    print("What question would you like to save?")
    question = input().strip()
    print("What is the answer for the question?")
    answer = input().strip()

    saved = SaveQuestion(question, answer)
    print(saved)

