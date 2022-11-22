from random import choice
from words import words
from threading import Timer
import time

def generate_black_answer(w):
    an = ''
    for i in range(len(w)):
     an = an + '_ '
    return an

def print_hangman(max):
    if (max == 5):
        print('''
            +---+
            O   |
                |
                |
                ===''')
    elif (max == 4):
        print('''
            +---+
            O   |
            |   |
                |
            ===''')
    elif (max == 3):
        print('''
            +---+
             O   |
            /|   |
                 |
            ===''')
    elif (max == 2):
        print('''
            +---+
            O   |
           /|\  |
                |
            ===''')
    elif (max == 1):
        print('''
            +---+
            O   |
           /|\  |
           /    |
            ===''')
    elif max == 0:
        print('''
            +---+
            O   |
           /|\  |
           / \  |
                ===''')
        
print("\nWelcome to Hangman game by Gifaril Mae Nisperos\n")
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
time.sleep(2)
print("\nThe game is about to start!\nLet's play Hangman!")
time.sleep(3)


maxTry = 6
word = choice(words)
answer = generate_black_answer(word)

timeUp = False

stillGueesing = True
gameIsOnGoing = True
temp= ''



while gameIsOnGoing:
    timeout = 30
    t = Timer(timeout, print)
    t.start()
    while stillGueesing:
        print(f"\nThe word is {answer}")
        if maxTry == 0 or not t.is_alive():
            if (not t.is_alive()):
                print("\nTIME IS UP!!")
            else:
               print_hangman(maxTry) 
            t.cancel()
            print(f"Game over!!" "\n" "The Answer is:", word)
            inp = input("do you want still to play?")
            if (inp.lower() == 'yes'):
                maxTry = 6
                word = choice(words)
                answer = generate_black_answer(word)
                t = Timer(timeout, print)
                t.start()
                print(f"The word length is {len(word)}")
                continue
            else:
                stillGueesing = False    
                gameIsOnGoing = False
                break
        print(f"You have {maxTry} tries left")

        prompt = "You have %d seconds to choose the correct answer...\n" % timeout
        inp = input(prompt)

        if inp.lower() in word.lower():
            temp = temp + inp.lower()
            answer = ''
            for i in word:
                if (i.lower() in temp.lower() or i.lower() == inp.lower()):
                    answer = answer +  f'{i} '
                else:
                    answer = answer + '_ '
            if (answer.replace(' ', '') == word):
                print(f"Congratz the word is {word}.")
                t.cancel()
                inp = input("do you want still to play?")
                if (inp.lower() == 'yes'):
                    maxTry = 6
                    word = choice(words)
                    answer = generate_black_answer(word)
                    print(f"The word length is {len(word)}")
                    continue
                else: 
                    stillGueesing = False    
                    gameIsOnGoing = False
                    break
            continue

        if (t.is_alive() and inp != None):
            if inp == word:
                print("You won!!")
                inp = input("do you want still to play?")
                stillGueesing = False
            print("Opps! your guesses are wrong please try again.")
        else:
            print("Opps! you ran out of time, please try again.")
        maxTry = maxTry - 1
        print_hangman(maxTry)         



    
    

# while '-' in word or '' in word:
#     word = random.choice(words)
 



