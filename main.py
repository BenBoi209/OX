#TIC - TAC - TOE made by saran,benon,darsh,jewel:

#Made for IT exhibition at holy grace academy mala


from tkinter import*

root = Tk()
root.title('Tic-Tac-Toe')
root.geometry("650x450")


reset_button = Button(root, text="Restart",command=root.quit, bg="light blue")
button_quit = Button(root, text="Play",command=root.quit, bg="light blue")
mylabel1 = Label(root, text="Welcome to python TIC-TAC-TOE",bg="light blue",font="Helvetica 15 bold")
mylabel2 = Label(root, text="Tic-tac-toe, noughts and crosses, or Xs and Os is a paper-and-pencil game for two",bg="light blue",font="Helvetica 12 bold")
mylabel3 = Label(root, text="players who take turns marking the spaces in a three-by-three grid with X or O.",bg="light blue",font="Helvetica 12 bold")
mylabel4 = Label(root, text="The player who succeeds in placing three of their marks in a horizontal,",bg="light blue",font="Helvetica 12 bold")
mylabel5 = Label(root, text="vertical, or diagonal row is the winner.",bg="light blue",font="Helvetica 12 bold")
mylabel6 = Label(root, text="",bg="light blue",font="Helvetica 15 bold")
mylabel7 = Label(root, text="",bg="light blue",font="Helvetica 15 bold")
mylabel8 = Label(root, text="",bg="light blue",font="Helvetica 15 bold")
mylabel9 = Label(root, text="",bg="light blue",font="Helvetica 15 bold")
mylabel10 = Label(root, text="",bg="light blue",font="Helvetica 15 bold")
mylabel11 = Label(root, text="",bg="light blue",font="Helvetica 15 bold")
mylabel12 = Label(root, text="",bg="light blue",font="Helvetica 15 bold")
mylabel13 = Label(root, text="made by: Saran,Benon,Darsh,Jewel :)",bg="light blue",font="Helvetica 15 bold")
mylabel14 = Label(root, text="",bg="light blue",font="Helvetica 15 bold")

mylabel1.grid(row=0, column=0)
mylabel2.grid(row=3, column=0)
mylabel3.grid(row=4, column=0)
mylabel4.grid(row=5, column=0)
mylabel5.grid(row=6, column=0)
mylabel6.grid(row=7, column=0)
mylabel7.grid(row=8, column=0)
mylabel8.grid(row=9, column=0)
mylabel9.grid(row=10, column=0)
mylabel10.grid(row=11, column=0)
mylabel11.grid(row=12, column=0)
mylabel12.grid(row=13, column=0)
mylabel13.grid(row=14, column=0)
button_quit.grid(row=15, column=0)

root.configure(bg='light blue')



root.mainloop()


from tkinter import *
import random

from tkinter import *
import random

root.geometry("650x450")


def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + "'s turn"))

            elif check_winner() is True:
                label.config(text=(players[0] + " wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + "'s turn"))

            elif check_winner() is True:
                label.config(text=(players[1] + " wins by scoring 1 point"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")


def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="light green")
            buttons[row][1].config(bg="light green")
            buttons[row][2].config(bg="light green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="light green")
            buttons[1][column].config(bg="light green")
            buttons[2][column].config(bg="light green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="light green")
        buttons[1][1].config(bg="light green")
        buttons[2][2].config(bg="light green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="light green")
        buttons[1][1].config(bg="light green")
        buttons[2][0].config(bg="light green")
        return True

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False


def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


def new_game():
    global player

    player = random.choice(players)

    label.config(text=player + "'s turn :)")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="light blue")


window = Tk()
window.title("Tic-Tac-Toe")
players = ["X", "O"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]



label = Label(text=player + "'s turn :)", bg="light blue", font=('consolas', 25))
label.grid(row=8, column=0)

reset = Button(text="Restart", font=('consolas',20), bg='light blue', command=new_game)
reset.grid(row=13, column=0)

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", bg="light blue", font=('consolas', 45), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)


window.configure(bg='light blue')




window.mainloop()
