# here code for connect four game. created by me "islam atef nagy"
# lets goo
import random
import turtle as t  # for drawing gui

import numpy as np


# help(t)
def starting_draw():
    t.bgcolor('black')
    t.color('white')
    t.penup()
    t.setpos(-200, -25)
    t.pendown()
    t.write("CHOOSE X OR O ", font=('Arial', 50, 'bold'))
    t.penup()
    t.setpos(-160, -80)
    t.write("CONNECT FOUR ", font=('Arial', 50, 'bold'))
    t.pendown()


starting_draw()

# board=np.array([['1','2','3','4','5','6','7'],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]])
# print(board)
# this soo bad
board = np.zeros((7, 7),
                 dtype=str)  # i used zero becouse array will take (7,7) as a data in 1 list but zero take it as a dimension and all dat is zero.
# i used dtype string to make 0 == '' and becouse i operate with string not intger.
board[0] = ['A', 'B', 'C', 'D', 'E', 'F', 'G']  # to make user choose which the colum
board = np.where(board == '', ' ', board)
computer = 'O'  # player x computer so i need 2 varible for playr and computer


def choose_player_mark():
    global player
    global computer
    player = input("enter your mark X or O ").upper()  # to make user choose the mark
    if player == 'X':
        computer = 'O'
    elif player == 'O':
        computer = 'X'
    else:
        print("enter correct answer: ")
        choose_player_mark()


choose_player_mark()
easy = False
mediam = False
hard = False


def level_game():
    global easy
    global mediam
    global hard
    level = input("which level you want ? \n1-easy \t2-midiam\t")
    if level == '1':
        easy = True
    elif level == '2':
        mediam = True
    elif level == '3':
        hard = True
    else:
        print("enter correct answer")
        level_game()


level_game()


# print(board)         #replace it by gui
def reset_screan():
    t.bgcolor('white')
    t.color('black')
    t.clear()  # to clear the screen.
    t.penup()
    t.setpos(0, 0)  # to reset curser.
    t.pendown()
    t.speed(0)


reset_screan()


def board_draw():
    t.width(3)  # foe width of line.
    t.penup()  # for delete the lines which will draw
    t.setpos(0, -210)
    t.pendown()  # to make future lines draw
    t.forward(210)
    t.left(90)
    for i in range(3):  # for drawing squre
        t.forward(420)
        t.left(90)
    t.forward(210)


board_draw()


def row_draw():
    t.left(90)
    t.setpos(210, -210)

    for i in range(3):  # for drawing rows
        t.forward(60)
        t.left(90)
        t.forward(420)
        t.right(90)
        t.forward(60)
        t.right(90)
        t.forward(420)
        t.left(90)
    t.forward(60)


row_draw()


def col_draw():
    t.left(90)
    for i in range(3):  # for drawing columns
        t.forward(60)
        t.left(90)
        t.forward(420)
        t.left(-90)
        t.forward(60)
        t.right(90)
        t.forward(420)
        t.left(90)


col_draw()


def main_row():
    t.right(180)
    t.penup()
    t.setpos(-195, 150)
    t.pendown()

    letters = 'ABCDEFG'
    #  for loop for draw letters
    #  function enumerate for return the data from letters and it's index
    t.color('red')
    for i, l in enumerate(letters):
        t.penup()
        t.setpos(-195 + i * 60, 150)
        t.pendown()
        t.write(l, font=('Arial', 40, 'bold'))


main_row()
column_i = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
free_cells = {'A': 6, 'B': 6, 'C': 6, 'D': 6, 'E': 6, 'F': 6, 'G': 6}


def drawing_playing(col, mark, color):
    t.color(color)  # take the color for playing
    r = free_cells[col]  # help in position  selecting
    c = column_i[col]  # help in position  selecting
    t.penup()
    #  print(-190 + 57 * (6 - (6 - c)), -150 + 57 * (5 - r))   # this for test thw position.
    t.setpos(-189 + 57 * (6 - (6 - c)), -140 + 57 * (5 - r))  # for select the position.
    t.pendown()  # to delete the line
    t.write(mark, font=('Arial', 35, 'normal'))  # to writing
    free_cells[col] -= 1


col_index = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}

all_posibler = ''


def playing_for_player():
    global all_posible
    column = ' '
    while column != 'A' and column != 'B' and column != 'C' and column != 'D' and column != 'E' and column != 'F' and column != 'G':
        column = input("choose your position: ").upper()
    all_posible = column
    column_index = col_index[column]  # the playing column
    all_cells = board[1:, column_index]  # to extract the collum which player will play in it.
    position = (all_cells == ' ').sum()
    if position == 0:
        # print("choose correct position:")
        playing_for_player()
        return
    # the result of comparison is array of true and false and i will do sum function at this array.
    board[position][column_index] = player
    # print(board)
    drawing_playing(column, player, 'red')


# here code for computer playing v player:
index_col = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G'}


def playing_for_computer_hard():
    column_index = col_index[all_posible]
    x = column_index - 1
    y = column_index + 1
    index = random.randint(x, y)
    #while index > 6 or index < 1:
       # index = random.randint(x , y)
    if index > 6 or index < 1:
        #  nummber of playing the percentag is 1/3
           playing_for_computer()
           return
    all_cells = board[1:, index]
    pos = (all_cells == ' ').sum()
    c=0
    while pos == 0:
         c+=1
         index = random.randint(x,y )
         # while index > 6 or index < 1:
         #    index = random.randint(x, y)
         all_cells = board[1:, index]
         pos = (all_cells == ' ').sum()
         # the result of comparison is array of true and false and i will do sum function at this array.
         if c == 9:
            playing_for_computer()
            return
    board[pos][index] = computer
    drawing_playing(index_col[index], computer, 'green')


def playing_for_computer():
    column_index = random.randint(0, 6)
    all_cells = board[1:, column_index]  # to extract the collum which player will play in it.
    position = (all_cells == ' ').sum()
    # if position == 0:            # why here have drob when code run recuirsion!!!!!!!!
    #     playing_for_computer()
    while position == 0:
        column_index = random.randint(0, 6)
        all_cells = board[1:, column_index]
        position = (all_cells == ' ').sum()
        # the result of comparison is array of true and false and i will do sum function at this array.
    board[position][column_index] = computer
    # print(board)
    drawing_playing(index_col[column_index], computer, 'green')


player_score_tot = 0  # final score
comp_score_tot = 0  # final score
reversed_arr = np.flip(board[1:], axis=0)  # i reversed the array by this function in numpy to git diagonal from right.


# def hard():
#
#     for i in range(7):
#         count = 0
#         for g in range(1,7):
#             if board[i][g]==' ':
#                 continue
#             elif board[i][g]== player:
#                 count+=1
#             elif board[i][g]!= player and count>=2:
#                 return i
#             else:
#                 break
#


# def comp_turn_medium():  #meiam palying.
#     mark = computer
#     condition = (board[1:] == player).sum()  # count number of player turns
#     if condition >= 2:
#         # print('condition: ',condition)
#         # true if player played two or more turns
#         all_cells = board[1:]
#         for row in range(all_cells.shape[0]):
#             # iterate on the rows
#             where_to_play = []
#             idx_sec_cell = []
#             col_or_row = len(all_cells[row])  # 6 for column - 7 for rows
#             # (determine row or column)
#             counter = 0
#             for x in range(len(all_cells[row]) - 1):
#                 # create a window of length 2 with step = 1
#                 two_cells = all_cells[row][x: x + 2]
#                 # print('two cells',two_cells)
#                 if (two_cells == player).sum() == 2:
#                     idx_sec_cell.append(x + 1)
#                     counter += 1
#                     continue
#                 else:
#                     counter += 1
#                     continue
#             if counter == 6 and row != 5 and len(idx_sec_cell) == 0:
#                 # check: we scanned the row (counter),
#                 # check: we are not in the last row (row)
#                 # check: there are any two player_choice cells in the window?
#                 continue
#             if len(idx_sec_cell) >= 1:
#                 for index in idx_sec_cell:
#                     if index == 1 and all_cells[row][index + 1] == ' ' and col_or_row == 7:
#                         # in case of row and the two cells
#                         # are at the beginning and the next cell is empty
#                         where_to_play.append(index + 1)
#                     elif index == 1 and all_cells[row][index + 1] == player and all_cells[row][
#                         index + 2] == ' ' and col_or_row == 7:
#                         # in case of the third cell is player_choice, check the fourth cell
#                         # [index+2] can not be player_choice
#                         where_to_play.append(index + 2)
#
#                     ###################################################################
#                     if 2 <= index < col_or_row - 1 and col_or_row == 7:
#                         # the case of the 2 cells are in the middle
#                         if all_cells[row][index + 1] == ' ' and col_or_row == 7:
#                             # if the next cell is empty
#                             if 3 <= index < col_or_row - 1 and all_cells[row][index - 2] == ' ' and all_cells[row][
#                                 index - 3] == player:
#                                 # if the cell previous to the first x is empty and the cell before it is player_choice
#                                 where_to_play.append(index - 2)
#                             else:
#                                 where_to_play.append(index + 1)
#                         elif all_cells[row][index - 2] == ' ' and col_or_row == 7:
#                             # if the cell before the first x is empty
#                             where_to_play.append(index - 2)
#                         elif 2 <= index < col_or_row - 2 and all_cells[row][index + 2] == ' ' and col_or_row == 7:
#                             # if the fourth cell is empty
#                             where_to_play.append(index + 2)
#                             ####################################################################
#
#                     if index == col_or_row - 1 and all_cells[row][index - 2] == ' ' and col_or_row == 7:
#                         # if the two x are at the last two cells and the cell before the previous cell is empty
#                         where_to_play.append(index - 2)
#                     elif index == col_or_row - 1 and all_cells[row][index - 3] == ' ' and col_or_row == 7:
#                         where_to_play.append(index - 3)
#                 if len(where_to_play):
#                     if 0 <= row < 5 and all_cells[row + 1, where_to_play[-1]] != ' ':
#                         all_cells[row, where_to_play[-1]] = computer
#                         free_cells[index_col[where_to_play[-1]]] -= 1
#                         drawing_playing(index_col[where_to_play[-1]], mark, 'green')
#                         # print(board)
#                         # print(free_cells)
#                         return
#                     elif 0 <= row < 5 and all_cells[row + 1, where_to_play[-1]] == ' ':
#                         playing_for_computer()
#                         return
#                     else:
#                         all_cells[row, where_to_play[-1]] = computer
#                         free_cells[index_col[where_to_play[-1]]] -= 1
#                         drawing_playing(index_col[where_to_play[-1]], mark, 'green')
#                         # print(free_cells)
#                         # print(board)
#                         return
#                 else:
#                     # if all the previous conditions are false
#                     playing_for_computer()
#                     return
#             else:
#                 playing_for_computer()
#                 return
#     else:
#         playing_for_computer()
#         return
#
#
# ####################################################################


def score(col):
    x_score = 0  # to store the scor of player X
    o_score = 0  # to store the scor of player O
    for cell in col:
        if cell == 'X':
            x_score += 1
        else:
            if x_score % 4 != 0:
                x_score = x_score - (x_score % 4)
                # i want  if  scor make player win store it but  can not  make player win  all score delete it
                # this by {  x_score = x_score - (x_score % 4) }
        if cell == 'O':
            o_score += 1
        else:
            if o_score % 4 != 0:
                o_score = o_score - (o_score % 4)
    if player == 'X':
        player_score = x_score // 4  # to reset data
        comp_score = o_score // 4  # to reset data
    else:
        comp_score = x_score // 4  # to reset data
        player_score = o_score // 4  # to reset data
    return player_score, comp_score


def sendig_data_abd_cheack_if_win(p_or_c):
    player_score_tot = 0  # final score
    comp_score_tot = 0  # final score
    reversed_arr = np.flip(board[1:],
                           axis=0)  # i reversed the array by this function in numpy to git diagonal from right.
    for row in range(6):
        col = board[row + 1]  # to extract row and send it and increase 1 Becouse i do't need the first row
        player, comp = score(col)  # to take return data of score x and o
        player_score_tot += player  # edit final score for player
        comp_score_tot += comp  # edit final score for computer
        """               here check for diagonal  and send the diagonal to the same function {score}           """
        # in class array there is diagonal function take intger and return diagonal data in numpy there is flip function
        # it reverse the array take the array and the number which it reverse the array from it
        if row < 4:
            col = board[1:].diagonal(row)
            player, comp = score(col)  # to take return data of score x and o
            player_score_tot += player  # edit final score for player
            comp_score_tot += comp  # edit final score for computer

            col = reversed_arr[1:].diagonal(row)
            player, comp = score(col)  # to take return data of score x and o
            player_score_tot += player  # edit final score for player
            comp_score_tot += comp  # edit final score for computer
        else:
            # to do all diagonal. i need send to diagonal function { -2 -1 0 1 2 3 }.
            col = reversed_arr[1:].diagonal(row - 6)
            player, comp = score(col)  # to take return data of score x and o
            player_score_tot += player  # edit final score for player
            comp_score_tot += comp  # edit final score for computer

    for row in range(7):
        col = board[1:, row]  # to extract column and send it
        player, comp = score(col)  # to take return data of score x and o
        player_score_tot += player  # edit final score for player
        comp_score_tot += comp  # edit final score for computer
    if p_or_c == 'p':
        if player_score_tot >= 1:
            return True
        else:
            return False
    else:
        if comp_score_tot >= 1:
            return True
        else:
            return False


player_win = False
computer_win = False
while player_win != True and computer_win != True:
    playing_for_player()
    if sendig_data_abd_cheack_if_win('p'):
        player_win = True
    if easy==True:
        playing_for_computer()
    else:
        playing_for_computer_hard()
   # playing_for_computer()
    if sendig_data_abd_cheack_if_win('c'):
        computer_win = True
print('####GAME OVER####')
if player_win:
    print("player win. ")
else:
    print("computer win:")
# Creating a turtle object(pen)
pen = t.Turtle()


# Defining a method to draw curve
def curve():
    for i in range(200):
        # Defining step by step curve motion
        pen.right(1)
        pen.forward(1)


# Defining method to draw a full heart
def heart():
    # Set the fill color to red
    pen.speed(-1)
    pen.penup()
    pen.setpos(-30, 0)
    pen.pendown()
    pen.fillcolor('red')

    # Start filling the color
    pen.begin_fill()

    # Draw the left line
    pen.left(140)
    pen.forward(113)

    # Draw the left curve
    curve()
    pen.left(120)

    # Draw the right curve
    curve()

    # Draw the right line
    pen.forward(112)

    # Ending the filling of the color
    pen.end_fill()


# Defining method to write text
def txt():
    # Move turtle to air
    pen.up()

    # Move turtle to a given position
    pen.setpos(-98, 95)

    # Move the turtle to the ground
    pen.down()

    # Set the text color to lightgreen
    pen.color('white')

    # Write the specified text in
    # specified font style and size
    pen.write("Player Win", font=("Verdana", 25, "bold"))


# Draw a heart
def draw_heart():
    heart()

    # Write text
    txt()

    # To hide turtle
    pen.ht()


def print_who_winer():
    t.clear()
    t.color('black')
    t.penup()
    t.setpos(-250, -150)
    t.pendown()
    # t.write("    GAME OVER", font=('Arial', 50, 'bold'))

    t.penup()
    t.setpos(-170, -75)
    t.pendown()
    if player_win:
        t.penup()
        t.setpos(-400, -250)
        t.pendown()
        t.color("brown")
        t.write("CONGRATULATINS ", font=('Arial', 80, 'bold'))
        draw_heart()  # for draw heart.
    else:
        t.clear()
        t.color('black')
        t.penup()
        t.setpos(-220, -100)
        t.pendown()
        t.write("    GAME OVER", font=('Arial', 50, 'bold'))
        t.penup()
        t.setpos(-250, -150)
        t.pendown()
        t.color("red")
        t.write("Computer Win ", font=('Arial', 50, 'bold'))
    t.color("white")
    t.done()


print_who_winer()




















# what the errrrrrrrrrrrror.

# if index > 6 or index < 1:
#     # before doing nummber of playing the percentag is 1/3
#     # but now the percentage of playing random from 0 to 6 if soo little
#     if index < 1:
#         if ((board[0] == ' ').sum() > 0) and ((board[1] == ' ').sum() > 0):
#             index = random.randint(0, 1)
#             print("case 1 and 2")
#         elif (board[0] == ' ').sum() > 0:
#             index = 0
#             print("case 1 ")
#             print((board[0] == ' ').sum())
#         elif (board[1] == ' ').sum() > 0:
#             index = 1
#             print("case 2")
#             print((board[1] == ' ').sum())
#         else:
#             playing_for_computer()
#             print("case 3")
#             return
#     elif index > 6:
#         if (board[6] == ' ').sum() > 0 and (board[5] == ' ').sum() > 0:
#             index = random.randint(5, 6)
#         elif (board[6] == ' ').sum() > 0:
#             index = 6
#         elif (board[5] == ' ').sum() > 0:
#             index = 5
#         else:
#             playing_for_computer()
#             return