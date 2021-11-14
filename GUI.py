import tkinter as tk
from tkinter.constants import DISABLED, NORMAL
from tresenraya import TicTacToe
from tkinter import messagebox

newGame = TicTacToe()
dict_players = {0: 'X', 1: 'O'}

def disable_buttons()-> None:
    for i in range(9):
        buttons[i].config(state=DISABLED)

def reset():
    for i in range(9):
        buttons[i]['text']=' '
        buttons[i].config(state=NORMAL)
        newGame.reset_game()


def click(b: tk.Button, game:TicTacToe =newGame) -> None:
    if game.checkMove([b.grid_info()['row'], b.grid_info()['column']]):
        b['text'] = dict_players[newGame.player]
        game.updateGame([b.grid_info()['row'], b.grid_info()['column']])
        finished, winner = game.checkGame()
        if (finished) & (winner != None):
            messagebox.showinfo(title="Game finished!", message="Player {} wins the game!".format(dict_players[winner]))
            disable_buttons()
        elif (finished) & (winner == None):
            messagebox.showinfo(title="Game finished!", message="Nobody won the game!")
            disable_buttons()
    else:
        messagebox.showerror(title="!!", message="!!!")

window = tk.Tk()

b_00 = tk.Button(window, command=lambda: click(b_00), height=4, width=5)
b_01 = tk.Button(window, command=lambda: click(b_01), height=4, width=5)
b_02 = tk.Button(window, command=lambda: click(b_02), height=4, width=5)
b_10 = tk.Button(window, command=lambda: click(b_10), height=4, width=5)
b_11 = tk.Button(window, command=lambda: click(b_11), height=4, width=5)
b_12 = tk.Button(window, command=lambda: click(b_12), height=4, width=5)
b_20 = tk.Button(window, command=lambda: click(b_20), height=4, width=5)
b_21 = tk.Button(window, command=lambda: click(b_21), height=4, width=5)
b_22 = tk.Button(window, command=lambda: click(b_22), height=4, width=5)
buttons = [b_00, b_01, b_02, b_10, b_11, b_12, b_20, b_21, b_22]

for i in range(9):
    buttons[i].grid(row=i//3, column=i%3)

my_menu = tk.Menu(window)
window.config(menu=my_menu)

options_menu = tk.Menu(my_menu)
my_menu.add_cascade(label='Options', menu=options_menu)
options_menu.add_command(labe='Reset game', command=reset)


window.mainloop()