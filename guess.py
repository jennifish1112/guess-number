print('Hello, what is your name?')
my_name = input('My name is ')
print('Okey, ' + my_name + ', I am thinking of a number between 0 and 100, want to take a guess? ')

import random
num = random.randint(0, 100)
count = 1
while True:
    print('Guess ', count)
    guess = int(input('Your guess:'))
    if(guess == num):
        print('That is right, lucky you!')
        break
    elif(guess < num):
        print('Too low!')
    else:
        print('Too high!')
    count+=1
