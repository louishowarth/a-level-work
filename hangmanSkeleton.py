from random import choice
from string import ascii_lowercase


class Hangman():
    def __init__(self):
        self.word = self.get_word()
        self.letter_row = '*' * len(self.word)
        self.letters_guessed = []
        self.guesses_left = 10
        
    def get_letter_row(self):
        return self.letter_row

    def get_guesses_left():
        return guesses_left

    def get_word(self):
##        read_words=open('words.txt','r')
##        lines=read_words.read().splitlines()
##        random_word=choice(lines)
##        read_words.close()
##        return random_word
        return "apple"
        
    
    def guess_letter(self,letter):
        try:
            if type(letter) != str or len(letter) != 1 or letter not in ascii_lowercase:
                raise TypeError
            if letter in self.letters_guessed:
                raise ValueError    
            elif letter in self.word:
                letter_row_list=list(self.letter_row)
                for count in range (len(self.word)):
                    if letter==self.word[count]:
                        letter_row_list[count]=letter
                self.letter_row=''.join(letter_row_list)
            else:
                self.guesses_left=self.guesses_left-1
        except TypeError:
            print("Value given is not a letter")
        except ValueError:
            print("Letter has already been guessed")
        return self.letter_row
        
    def check_win(self):
        if self.letter_row == self.word:
            return True
        else:
            return False
        

if __name__ == "__main__":
    
    this_game = Hangman()
    
    while not this_game.check_win():
        print(this_game.get_letter_row())
        user_guess = input("Guess a letter:\t")
        this_game.guess_letter(user_guess)
        this_game.letters_guessed.append(user_guess)
        print("Guesses Left:\t", this_game.guesses_left)
        this_game.check_win()

        if this_game.guesses_left == 0:
            print("The word was",this_game.word)
            break
        
        if this_game.check_win() == True:
            print("Congratulations, you guessed that the word was", this_game.word)



         


