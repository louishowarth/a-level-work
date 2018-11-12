from tkinter import *
from tkinter import messagebox
from hangmanSkeleton import Hangman

class interface():
    def __init__(self):
        self.game=Hangman() #create instance of Hangman
        self.button_state=["active"]*26 #set button states
        self.word=self.game.letter_row #get word to show
        self.draw_input()
        
    def draw_man(self): #draws hangman after each guess
        self.lives=self.game.guesses_left #get lives left
        if self.lives<1:
            w.create_line(125,60,120,65)
            messagebox.showinfo("game over!","out of lives")
        elif self.lives<2:
            w.create_line(125,60,130,65)
        elif self.lives<3:
            w.create_line(120,50,130,50)
        elif self.lives<4:
            w.create_line(125,45,125,60)
        elif self.lives<5:
            w.create_oval(120, 35, 130, 45)
        elif self.lives<6:
            w.create_line(125,25,125,35)
        elif self.lives<7:
            w.create_line(75,45,95,25)
        elif self.lives<8:
            w.create_line(75,25,125,25)
        elif self.lives<9:
            w.create_line(75,75,75,25)
        elif self.lives<10:
            w.create_line(100, 75, 50, 75)
        self.draw_input()
        canvas.mainloop()
        
    def draw_input(self): #creates updated input window
        word_display=Label(text=self.game.letter_row)
        word_display.grid(row=0,column=3)
        for i in range(len(self.button_state)):
            if i > 20:
                x=i+1
            else:
                x=i
            button = Button(window1, text=chr(65+i), state=self.button_state[i], command=lambda letter=i: self.input_guess(letter), width=10, height=6)
            button.grid(row=int(x/7)+1, column=x%7)
        window1.mainloop()

    def input_guess(self,letter): #processes guess
        self.button_state[letter]="disabled"
        letter=(chr(97+letter))
        self.word=self.game.guess_letter(letter)
        if self.game.check_win() == True:
            messagebox.showinfo("You Won!","Congratulations, you guessed that the word was "+ self.game.word)
            word_display=Label(text=self.game.letter_row)
            window1.mainloop()
        else:
            self.draw_man()

if __name__=="__main__":
    window1 = Tk()
    canvas = Tk()
    w = Canvas(canvas, width=200, height=100)
    w.pack()
    interface()
