'''
Quiz generator

'''

def Quiz():
    score = 0
    while True:

        print('Welcome to the Quiz Competition')
        que_1 = input("Que 0 : What is the Capital of France?\n").lower()
        if que_1 == 'paris':
            print("Correct !")
            score += 1
        else:
            print('Incorrect . The correct answer is Paris')
            print(f'Your Final score is {score} out of 3')
            break
            
        que_2 = input("Que 1 : What is the largest planet in our solar system?\n").lower()
        if que_2 == 'jupiter':
            print("Correct !")
            score += 1
        else:
            print('Incorrect . The correct answer is Jupiter')
            print(f'Your Final score is {score} out of 3')
            break
        que_3 = input('Who painted the Mona Lisa?\n').lower()
        if que_3 == 'leonardo da vinci':
            print("Correct !")
            score += 1
        else:
            print('Incorrect . The correct answer is Leonardo da Vinci')
            print(f'Your Final score is {score} out of 3')
            break
        print(f'Your Final score is {score} out of 3')
        break



# so the above code is bit simple and begineer friendly yet the long and time consuming as we can see everything is being used in a basic manner 


# the below code will be bit advanced 

# first we created the nested list with all the question along with their answers
question = [['What is the Capital of France?', 'Paris'],
            ['What is the largest planet of the solar system?', 'Jupiter'],
            ['Who painted the Mona Lisa painting?','Leonaldo da vinci']]

# we will use the for loop now

for que_numer, ques in enumerate(question):
    score = 0
    print(f'Question {que_numer} : {ques[0]}')
    user_input = input("Your Answer : ").lower()

    if user_input == ques[1].lower():
        print("Correct")
        score += 1
    else:
        print(f"Incorrect Answer. The correct Answer is {ques[1]}")
        print(f'Your score is {score} out of {len(question)}')
        break 

print(f'\nYour final score is {score} out of {len(question)}')


