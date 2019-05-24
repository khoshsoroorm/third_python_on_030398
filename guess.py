import random
secret = random.randint(1,10)
print('guess if you are a genius')

while True:

    guess = int(input('guess the secret number:'))
    if guess < secret:
        print('javab kochiktar ast \n try again')
    elif guess > secret:
        print(' javab bozogtar az male mas')
    elif guess == secret:
        print('very good \n you are a genius')
        break


