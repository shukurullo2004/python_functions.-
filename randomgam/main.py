import random
number = random.randint(1,100)
attemps =0

while True:
    guess = int(input('try to find guess number: '))
    attemps += 1
    if guess > number:
        print('it is too high')
    elif guess < number:
        print('it is too low')
    else:
        print(f'congrulation, you have found it with {attemps}')
