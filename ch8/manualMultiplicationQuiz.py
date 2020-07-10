import random, time

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    # Pick two random numbers:
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
    startTime = time.time()
    counter = 0
    while True:
        answer = input(prompt)
        try:
            answer = int(answer)
        except:
            print('Enter a number!')
            continue
        else:
            if time.time() - startTime > 8:
                print('Out of time!')
                break
            if answer != (num1 * num2):
                print('Incorrect!')
                counter += 1
                if counter == 3:
                    print('Out of tries!')
                    break
            else:
                print('Correct!')
                correctAnswers += 1
                break
            time.sleep(1) # Brief pause to let user see the result

print('Score: %s / %s' % (correctAnswers, numberOfQuestions))