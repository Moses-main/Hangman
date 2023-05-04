import tkinter as tk
import hangman


# class GameControl:

def start_game():

    player_name = User_name.get()
    if player_name == "" or player_name == None:
        player_name = 'player'

    root.destroy()

    new_window = tk.Tk()
    new_window.geometry('600x500')
    new_window.config(bg='teal')
    new_window.title('Hangman Game')

    game_label = tk.Label(
        text=f"Welcome {player_name} to the Game Section ", font='Arial 25')
    game_label.config(padx=10, pady=15, bg='teal', fg='white')
    game_label.pack()

    game_desc = tk.Label(
        text="To play game, enter an alphabet inside the box below to guess ", font='10', bg='teal', fg='white')
    game_desc.pack(pady=200)


def pause_button():
    print('You just tapped the pause_button')


def quit_button():
    root.destroy()


root = tk.Tk()
root.geometry('600x500')
root.config(bg='teal')
root.title('Hangman Game')

game_name = tk.Label(text="Hang Man Game")
game_name.config(font="arial 44", bg="teal", fg='white')
game_name.pack(pady=50)

input_label = tk.Label(text="Enter Your Name Below")
input_label.config(bg='teal', fg='white', font='bold 15')
input_label.pack(pady=30)

User_name = tk.Entry()
User_name.config(font='timesnewroman', width=35,)
User_name.pack(padx=5, pady=10)

next_button = tk.Button(text="Pause", width=10, command=pause_button)
next_button.place(x=400, y=340)

quit_button = tk.Button(text="Quit", width=10, command=quit_button)
quit_button.place(x=140, y=340)

start_button = tk.Button(text='Start Game', width=10, command=start_game)
start_button.place(x=260, y=340)


tk.mainloop()


# if __name__ == "__main__":
#     print('This is the game')

'''
Tkinter Widgets
Tkinter provides various controls, such as buttons, labels and text boxes used in a GUI application. These controls are commonly called widgets.

There are currently 15 types of widgets in Tkinter. We present these widgets as well as a brief description in the following table −

Sr.No.	Operator & Description
1	Button
The Button widget is used to display buttons in your application.

2	Canvas
The Canvas widget is used to draw shapes, such as lines, ovals, polygons and rectangles, in your application.

3	Checkbutton
The Checkbutton widget is used to display a number of options as checkboxes. The user can select multiple options at a time.

4	Entry
The Entry widget is used to display a single-line text field for accepting values from a user.

5	Frame
The Frame widget is used as a container widget to organize other widgets.

6	Label
The Label widget is used to provide a single-line caption for other widgets. It can also contain images.

7	Listbox
The Listbox widget is used to provide a list of options to a user.

8	Menubutton
The Menubutton widget is used to display menus in your application.

9	Menu
The Menu widget is used to provide various commands to a user. These commands are contained inside Menubutton.

10	Message
The Message widget is used to display multiline text fields for accepting values from a user.

11	Radiobutton
The Radiobutton widget is used to display a number of options as radio buttons. The user can select only one option at a time.

12	Scale
The Scale widget is used to provide a slider widget.

13	Scrollbar
The Scrollbar widget is used to add scrolling capability to various widgets, such as list boxes.

14	Text
The Text widget is used to display text in multiple lines.

15	Toplevel
The Toplevel widget is used to provide a separate window container.

16	Spinbox
The Spinbox widget is a variant of the standard Tkinter Entry widget, which can be used to select from a fixed number of values.

17	PanedWindow
A PanedWindow is a container widget that may contain any number of panes, arranged horizontally or vertically.

18	LabelFrame
A labelframe is a simple container widget. Its primary purpose is to act as a spacer or container for complex window layouts.

19	tkMessageBox
This module is used to display message boxes in your applications.

Let us study these widgets in detail −

Standard attributes
Let us take a look at how some of their common attributes.such as sizes, colors and fonts are specified.

Dimensions

Colors

Fonts

Anchors

Relief styles

Bitmaps

Cursors

Let us study them briefly −

Geometry Management
All Tkinter widgets have access to specific geometry management methods, which have the purpose of organizing widgets throughout the parent widget area. Tkinter exposes the following geometry manager classes: pack, grid, and place.

The pack() Method − This geometry manager organizes widgets in blocks before placing them in the parent widget.

The grid() Method − This geometry manager organizes widgets in a table-like structure in the parent widget.

The place() Method − This geometry manager organizes widgets by placing them in a specific position in the parent widget.'''
