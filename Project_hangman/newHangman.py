from threading import Timer

class HangMan:
    def __init__(self, name,list_of_words):
        self.name = name
        self.list_of_words = list_of_words
        self.word = ''
        self.temp_answer = ''
        self.attemp = 0
    
    def generate_word(self):
        self.word = self.list_of_words[0]
        self.list_of_words.pop(0)
        ans = ''
        for i in range(len(self.word)):
            ans = ans + '_ '
        print(f"You have 30 seconds to guese the correct answer...\n")
        print(f'Here is your word {self.name}')
        print(f'{ans}')
        self.temp_answer = ans
        self.attemp = 0
    
    def validate(self, value):
        if ( not value.lower() in self.word.lower()):
            return False
        temp_str = ''
        for i in self.word:
            if (i.lower() in self.temp_answer.lower() or i.lower() == value.lower()):
                temp_str = temp_str +  f'{i} '
            else:
                temp_str = temp_str + '_ '
        print(temp_str)
        self.temp_answer = temp_str
        return True

        
    
    def print_hangman(self):
        hangman = [
           '''
            +---+
            O   |
                |
                |
                ===''',
           '''
            +---+
            O   |
            |   |
                |
            ===''',
            '''
            +---+
             O   |
            /|   |
                 |
            ===''',
            '''
            +---+
            O   |
           /|\  |
                |
            ===''',
            '''
            +---+
            O   |
           /|\  |
           /    |
            ===''',
            '''
            +---+
            O   |
           /|\  |
           / \  |
            ==='''
        ]
        print(hangman[self.attemp -1])
        
    
    
    def play(self):
        max_try = 6
        time_out = 30
        self.generate_word()
        game_is_going= True
        t = Timer(time_out, print, ['Youre time is up!'])
        t.start()
        print(f'You have {max_try}')
        while game_is_going:
            if (self.attemp >= max_try or self.temp_answer.replace(' ', '').lower() == self.word.lower()):
                t.cancel()
                if (self.attemp > max_try):
                    print(f'Game over! You lose! the word is {self.word}')    
                    self.print_hangman()
                else:
                    print(f'You did a great Job {self.name}. the word is {self.word}')
                inp = input('You want to play again?: ')
                if (inp == 'yes' or inp == 'y'):
                    self.generate_word()
                    t = Timer(time_out, print)
                    t.start()
                else:
                    print('Thanks for playing!')
                    break
            print(f"You have {time_out} seconds to guese the correct answer...\n")
            ans = input(">>>: ")
            if ( not t.is_alive()):
                inp = input('You want to play again?: ')
                if (inp == 'yes' or inp == 'y'):
                    self.generate_word()
                    t = Timer(time_out, print)
                    t.start()
                else:
                    print('Thanks for playing!')
                    break
            if (self.validate(ans)):
                continue
            self.attemp = self.attemp + 1
            self.print_hangman()
list_of_words = []
with open('words.txt') as f:
    contents = f.readlines()
    for i in contents:
        list_of_words.append(i.strip())
                
name = input('Your name: ')
game1 = HangMan(name, list_of_words)
game1.play()
            
            

        