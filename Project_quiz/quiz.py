import time
import random

print("\nWelcome to Code Foundation Quiz by Gifaril\n")
name = input("Enter your name: ")
print("\nHello " + name + "! Good Luck!")
time.sleep(2)
print("\nThe quiz is about to start!\nGet Ready!")
time.sleep(3)

quizes = [
    {"question": "\nPython in Software is? \n A.Snake\n B.Programming Language", "answer": "B"},
    {"question": "\nHow do you print on Python? \n A.console.log()\n B.print()", "answer": "B"},
    {"question": "\nWhat is the difference of Float and int? \n A.Int is a number without a decimal point. A float is a floating-point number\n B.none", "answer": "A"},
    {"question": "\nA loop is a sequence of instructions that is continually repeated until a certain condition is reached. \n A.True\n B.False", "answer": "A"},
]

quizes2 = [
    {"question": "\nSoftware is defined as ________ \n A.Set of programs, documentation & configuration of data\n B.Set of programs\n C.Documentation and configuration of data", "answer": "A"},
    {"question": "\nWhat is Software Engineering? \n A.Designing a software\n B.Testing a software\n C.Application of engineering principles to the design a software", "answer": "C"},
    {"question": "\nWho developed Python? \n A.Watts S. Humphrey\n B.Guido Van Rossum\n C.Boris Beizer", "answer": "B"},
    {"question": "\nThis Statements changes the execution from its normal sequence. \n A.Control Statements\n B.Break\n C.Pass", "answer": "A"},
]

quizes3 = [
    {"question": "\nWho is the father of Software Engineering", "answer": "Watts S. Humphrey"},
    {"question": "\nCASE stands for?", "answer": "Computer-Aided Software Engineering"},
    {"question": "\nWhat is the full form of the “COCOMO” model?", "answer": "Constructive Cost Estimation Mode"},
    {"question": "\nFAST stands for?", "answer": "Facilitated Application Specification Technique"},
]

class Quiz:
    def __init__(self, name, easy, med, hard):
        self.name = name
        self.easy = easy
        self.med= med
        self.hard= hard
    
    def ask(self, value):
        quiz = []
        score = 0
        if (value == 1):
            quiz = self.easy
        if (value == 2):
            quiz = self.med
        if (value == 3):
            self.hard
        random.shuffle(quiz)
        for i in quiz:
            time.sleep(2)
            print(i["question"])
            inp = input('>>')
            if (i["answer"].lower() == inp):
                score = score + 1
        if (score < 3):
            return False
        print('Congratz you Pass!')
        return True
        
    
    def main(self):
        gameIsGoing = True
        while gameIsGoing:
            if (self.ask(1) == False):
                print("\nYou are now allowed to go further, You want to try again?")
                inp = input('Yes, No >>')
                if inp.lower() == 'yes':
                    print(f"\n'Lets get ready again {self.name}")
                    continue
                else:
                    gameIsGoing = False
                    break
            time.sleep(2)
            print('You are now at stage 2')
            if (self.ask(2) == False):
                print("\nYou are now allowed to go further, You want to try again?")
                inp = input('Yes, No >>')
                if inp.lower() == 'yes':
                    print(f"\n'Lets get ready again {self.name}")
                    continue
                else:
                    gameIsGoing = False
                    break
            time.sleep(2)
            print('You are now at stage 3')
            if (self.ask(3) == False):
                print("\nYou are now allowed to go further, You want to try again?")
                inp = input('Yes, No >>')
                if inp.lower() == 'yes':
                    print(f"\n'Lets get ready again {self.name}")
                    continue
                else:
                    gameIsGoing = False
                    break
            else:
                print(f'You Pass all Level {self.name}')
                print("\nYou want to try again?")
                inp = input('Yes, No >>')
                if inp.lower() == 'yes':
                    print(f"\n'Lets get ready again {self.name}")
                    continue
                else:
                    gameIsGoing = False
                    break
q = Quiz(name, quizes, quizes2, quizes3)
q.main()
    
  


