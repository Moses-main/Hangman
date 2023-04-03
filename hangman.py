import random
import tkinter as tk
from words import another_word
import string


global usr_text


'''This function validates the list of words
chosen to play the game'''


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while "-" in word or " " in word:
        word = random.choice(words)

    return (word.upper())

    '''The Engine for the Game
    This class handles the definition and
    initialization of functions responsible
    for the different output that appears
    at the GUI according to the users input
    on the fly'''


class hang:

    def show(self):
        GUI = hang()

        usr_text = GUI.Guess.get('1.0', 'end').strip()
        # '''Restoring the state of the textbox to show the answer'''
        # ans.config(state='normal')

        GUI.ans.delete('1.0', 'end')
        GUI.ans.insert('1.0', game.clue(usr_text))
        GUI.Guess.delete('1.0', 'end')
        # ans.config(state='disabled')

    '''The GUI for the game
    The below code cover the 
    Graphical User Interface 
    for the game and is designed 
    minimalistically just for
    testing purposes'''

    words = get_valid_word(another_word)
    word_letters = set(words)  # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    root = tk.Tk()

    root.geometry('1200x500')
    root.config(bg='teal')
    root.title('Hangman Game')

    # padding the section
    pad = tk.Label(height=5, bg='teal')
    pad.pack()

    # first label
    lab1 = tk.Label()
    lab1.config(bg='white', height=2, width=100,
                text='Enter Your Guess Letter Here', )
    lab1.pack()

    # padding the section
    pad = tk.Label(height=2, bg='teal')
    pad.pack()

    # user input section
    Guess = tk.Text()
    Guess.config(bg='white', height=2, width=88)
    Guess.pack()

    # padding the section
    pad = tk.Label(height=8, bg='teal')
    pad.pack()

    # The answer section of the app
    ans = tk.Text()
    ans.config(bg='teal', fg='white', height=2, width=80, padx=5, pady=1)
    ans.pack()

    # padding the section
    pad = tk.Label(height=8, bg='teal')
    pad.pack()

    # The submit button for the app
    submit = tk.Button()
    submit.config(text="SUBMIT", bg='orange', fg='white',
                  width=20, height=2, command=show)
    submit.pack()

    # padding the section
    pad = tk.Label(height=2, bg='teal')
    pad.pack()

    # # padding the section
    # pad = tk.Label(height=8, bg='teal')
    # pad.pack()

    def __init__(self):
        self.words = get_valid_word(another_word)
        self.word_letters = set(self.words)  # letters in word
        self.alphabet = set(string.ascii_uppercase)
        self.used_letters = set()  # what the user has guessed

        while len(self.word_letters) > 0:
            # letters used
            # ' '.join( ['a', 'b', 'c',]) --> 'a b c'
            self.message = 'You have used these letters:'' '.join(
                self.used_letters)
            print(self.message)

            # what the current word is (i.e W - O R D)
            word_list = [
                letter if letter in self.used_letters else '-' for letter in self.words]
            print('Current word: ', ' '.join(word_list))

            # getting user input
            user_letter = input("Guess a letter: \n").upper()

            if user_letter in self.alphabet - self.used_letters:  # if valid character in alphabet
                # add to the used_letter set
                self.used_letters.add(user_letter)
                if user_letter in self.word_letters:  # removes letter when in the guessed word
                    self.word_letters.remove(user_letter)
            elif user_letter in self.used_letters:
                message = 'You have already used that character. Please try again'
            else:
                err = 'Invalid character. Please try again'
    # print('Congrats')

    def clue(self, user_letter):
        self.user_letter = user_letter
        return user_letter

    def message(self, message):
        self.message = message
        return message

    def Unknown(self, err):
        self.err = err
        return err


game = hang()

'''This function is responsible for the assignment and display 
of the result, i.e words that are correctly guessed by the user
and those that he have used so far'''


'''FUNCTION SECTION
Activate here if you're done with
the class region.
'''

# def hangman():
#     words = get_valid_word(another_word)
#     word_letters = set(words)  # letters in word
#     alphabet = set(string.ascii_uppercase)
#     used_letters = set()  # what the user has guessed

#     while len(word_letters) > 0:
#         # letters used
#         # ' '.join( ['a', 'b', 'c',]) --> 'a b c'
#         print('You have used these letters:', ' '.join(used_letters))

#         # what the current word is (i.e W - O R D)
#         word_list = [
#             letter if letter in used_letters else '-' for letter in words]
#         print('Current word: ', ' '.join(word_list))

#         # getting user input
#         user_letter = input("Guess a letter: \n").upper()

#         if user_letter in alphabet - used_letters:  # if valid character in alphabet
#             used_letters.add(user_letter)  # add to the used_letter set
#             if user_letter in word_letters:  # removes letter when in the guessed word
#                 word_letters.remove(user_letter)
#         elif user_letter in used_letters:
#             print('You have already used that character. Please try again')
#         else:
#             print('Invalid character. Please try again')
#     print('Congrats')


# hangman()
# print(get_valid_word(another_word))
# global game


tk.mainloop(0)
game = hang()
