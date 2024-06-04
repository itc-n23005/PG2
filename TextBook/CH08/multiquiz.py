import pyinputplus as pyip
import random, time

number_of_questions = 10
correct_answers = 0

for question_number in range(number_of_questions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    answer = num1 * num2
    prompt = f'#{question_number + 1}: {num1} * {num2} = '

    attempts = 0
    while attempts < 3:
        user_input = input(prompt)
        try:
          user_answer = int(user_input)
         except ValueError:
             print('Invalid input. please enter a number.')
             continue

        if user_answer == answer:
            print('Correct')
            correct_answer += 1
            time.sleep(1)
            break
        else:
            print('Incorrect')
            attempts += 1
            
            if attempts == 3:
                print('Out of tries')
                time.sleep(1)

        print(f'得点: {correct_answers} / {number_of_questions}')
