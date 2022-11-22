import random
import time


z1 = False
z2 = False
z3 = False

hp = 100
z1_damage = 30
z2_damage =50
z3_damage = 100
z1_hp = 60
z2_hp =80
z3_hp = 120

gameIsGoing = True

yourDamage = 20

name = input("\nwhat is you name soldier?")
time.sleep(1)
print(f"\nYou are task {name} to deliver the vaccine to cure the zombie apocalypse.\nYou have to beat every zombie you face\nby answering this questions.")


quizes = [
    {"question": "\nFind the value of 3 + 2 • (8 – 3)", "answer": "13"},
    {"question": "\nI am an odd number. Take away one letter and I become even. What number am I?", "answer": "7"},
    {"question": "\nWhat is the difference of Float and int? \n A.Int is a number without a decimal point. A float is a floating-point number\n B.none", "answer": "A"},
    {"question": "\nA loop is a sequence of instructions that is continually repeated until a certain condition is reached \n A.True\n B.False", "answer": "A"},
    {"question": "\nIs used to execute both the true part and the false part of a given condition.", "answer": "If/Else Statemen"},
    {"question": "\nThis statement in python is used to terminate a loop.", "answer": "If/Else Statemen"},
    {"question": "\nIs a named location used to store the data in the memory?", "answer": "Variables"},
    {"question": "\nWhat is the correct extension of the Python file??", "answer": ".py"},
    {"question": "\nWhat will be the value of the following Python expression \n 4 + 3 % 5?", "answer": "7"},
    {"question": "\nWhat character is used to give single-line comments in Python?", "answer": "#"},
]

quizes2 = [
    {"question": "\nSoftware is defined as ________ \n A.Set of programs, documentation & configuration of data\n B.Set of programs\n C.Documentation and configuration of data", "answer": "A"},
    {"question": "\nWhat is Software Engineering? \n A.Designing a software\n B.Testing a software\n C.Application of engineering principles to the design a software", "answer": "C"},
    {"question": "\nWho developed Python? \n A.Watts S. Humphrey\n B.Guido Van Rossum\n C.Boris Beizer", "answer": "B"},
    {"question": "\nThis Statements changes the execution from its normal sequence. \n A.Control Statements\n B.Break\n C.Pass", "answer": "A"},
    {"question": "\nWhich of the following is not a core data type in Python programming?\n A.Tuples\n B.Lists\n C.Class", "answer": "C"},
    {"question": "\nWhich of the following functions is a built-in function in python? \n A.factorial()\n B.print()\n C.sqrt()", "answer": "B"},
    {"question": "\nWhich of the following is used to define a block of code in Python language? \n A.Indentation\n B.Key\n C.Brackets", "answer": "A"},
    {"question": "\nWhich of the following is the truncation division operator in Python? \n A.|\n B.//\n C./", "answer": "B"},
    {"question": "\nWhat are the two main types of functions in Python?  \n A.System function\n B.Custom function\n C.Built-in function & User defined function", "answer": "C"},
    {"question": "\nWhich of the following is a Python tuple? \n A.{1, 2, 3}\n B.[1, 2, 3]\n C.(1, 2, 3)", "answer": "D"},
]

quizes3 = [
    {"question": "\nWho is the father of Software Engineering", "answer": "Watts S. Humphrey"},
    {"question": "\nCASE stands for?", "answer": "Computer-Aided Software Engineering"},
    {"question": "\nWhat is the full form of the “COCOMO” model?", "answer": "Constructive Cost Estimation Mode"},
    {"question": "\nFAST stands for?", "answer": "Facilitated Application Specification Technique"},
    {"question": "\nPython was developed on what year?", "answer": "1991"},
    {"question": "\nPython supports the creation of anonymous functions at runtime, using a construct called __________", "answer": "lambda"},
    {"question": "\nWhat arithmetic operators cannot be used with strings in Python?", "answer": "-"},
    {"question": "\nWhat is output of print(math.pow(3, 2))?", "answer": "9.0"},
    {"question": "\nThis is a loop inside other loop", "answer": "Nested loop"},
    {"question": "\nIs a null operation, which is used when the statement is required syntactically", "answer": "Pass"},
    
]

while gameIsGoing:
    random.shuffle(quizes)
    print("\nOw one zombie found you. You need to beat him in oder to move forward.")
    for i in quizes:
        time.sleep(2)
        print(i["question"])
        inp = input('>>')
        if (i["answer"].lower() == inp):
            z1_hp = z1_hp - yourDamage
            if (z1_hp < 1):
                print("\nYou beat the zombie you can now move forward to the train station")
                break
        else:
            hp = hp - z1_damage
            if (hp<1):
                print("\nYou are dead!")
                break
    if (hp < 1):
        inp = input("\nDo you want to try again? >> ")
        if (inp == 'yes'):
            hp = 100
            z1_damage = 30
            z2_damage =50
            z3_damage = 100
            z1_hp = 60
            z2_hp =80
            z3_hp = 120
            gameIsGoing = True
            yourDamage = 20
            continue
        else:
            break
    else:
        random.shuffle(quizes2)
        time.sleep(2)
        print("\nOw one zombie found you. You need to beat him in oder to move forward")
        for i in quizes2:
            time.sleep(3)
            print(i["question"])
            inp = input('>>')
            if (i["answer"].lower() == inp):
                z2_hp = z2_hp - yourDamage
                if (z2_hp < 1):
                    print("\nYou beat the zombie you can now move forward to the train")
                    break
            else:
                hp = hp - z2_damage
                if (hp<1):
                    print("\nYou are dead!")
                    break
        if (hp < 1):
            inp = input("\nDo you want to try again? >> ")
            if (inp == 'yes'):
                hp = 100
                z1_damage = 30
                z2_damage =50
                z3_damage = 100
                z1_hp = 60
                z2_hp =80
                z3_hp = 120
                gameIsGoing = True
                yourDamage = 20
                continue
            else:
                break
        else:
            random.shuffle(quizes3)
            time.sleep(2)
            print("\nOw the final zombie is guarding the train beat it!")
            for i in quizes3:
                time.sleep(3)
                print(i["question"])
                inp = input('>>')
                if (i["answer"].lower() == inp):
                    z3_hp = z3_hp - yourDamage
                    if (z3_hp < 1):
                        print("\nYou beat the zombie you have sucessfully delivered the vaccine!")
                        break
                else:
                    hp = hp - z3_damage
                    if (hp<1):
                        print("\nOh No! You are died!")
                        break
            if (hp < 1):
                inp = input("\nDo you want to try again? >> ")
                if (inp == 'yes'):
                    hp = 100
                    z1_damage = 30
                    z2_damage =50
                    z3_damage = 100
                    z1_hp = 60
                    z2_hp =80
                    z3_hp = 120
                    gameIsGoing = True
                    yourDamage = 20
                    continue
                else:
                    break