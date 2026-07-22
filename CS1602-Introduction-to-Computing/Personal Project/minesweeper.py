#This is a simple implementation of the Minesweeper game in Python.

#Import libraries
import random

#Backend logic
class Minesweeper:
    def __init__(self,n,m):
        '''
        **Initializing the game board and so on.**  
        *We use list to represent each position.*
        - '-1' means there exists a mine
        - 'n'  means it is surrounded by how many mines
        - 'T/F' means whether it is visible for the plaer
        '''
        self.size = n
        self.density = m
        board = [[[0,False] for i in range(n)] for j in range(n)]
        cells = [(i,j) for i in range(n) for j in range(n)]
        mines = random.sample(cells,m)
        row_position = [mines[k][0] for k in range(m)]
        col_position = [mines[k][1] for k in range(m)]
        for k in range(m):
            board[row_position[k]][col_position[k]][0] = -1
        def mines_counter(s,t):
            counter = 0
            for x in range(-1,2):
                for y in range(-1,2):
                    if 0 <= s + x < n and 0 <= t + y < n:
                        if board[s + x][t + y][0] == -1:
                            counter += 1
            return counter
        for s in range(n):
            for t in range(n):
                if board[s][t][0] == -1:
                    continue
                else:
                    board[s][t][0] = mines_counter(s,t)
        self.board = board
    
    def click(self,u,v):
        '''
        The first click is different from other clicks, we need to define it specially.
        '''
        if self.board[u][v][0] == -1:
            self.board[u][v][1] = True
            return 0
        if self.board[u][v][1] == True:
            return 1
        self.board[u][v][1] = True
        stack = [(u,v)]
        while len(stack) > 0:
            i, j = stack[0]
            stack.pop(0)
            for x in range(-1,2):
                for y in range(-1,2):
                    if 0 <= i + x < self.size and 0 <= j + y < self.size and self.board[i+x][j+y][0] == 0 and self.board[i+x][j+y][1] == False:
                        self.board[i+x][j+y][1] = True
                        stack.append((i+x,j+y))
                    elif 0 <= i + x < self.size and 0 <= j + y < self.size and self.board[i+x][j+y][0] > 0 and self.board[i+x][j+y][1] == False:
                        self.board[i+x][j+y][1] = True
        return 1
    
    def visualize(self):
        '''
        Visualize the current board.
        '''
        for i in range(self.size):
            row = ''
            for j in range(self.size):
                if self.board[i][j][1] == False:
                    row += '■ '
                else:
                    if self.board[i][j][0] == -1:
                        row += '* '
                    else:
                        row += str(self.board[i][j][0]) + ' '
            print(row)
    
    def check_win(self):
        '''
        Check whether the player wins the game.
        '''
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j][0] != -1 and self.board[i][j][1] == False:
                    return False
        return True

def main():
    n = int(input("Please input the size of the board: "))
    m = int(input("How many mines do you want to put in your board? "))
    if m >= n*n:
        print("Too many mines! Please try again.\n")
        return 1
    board = Minesweeper(n,m)
    board.visualize()
    while board.check_win() == False:
        s = int(input("Please input the row ordinate of the position you choose:"))
        if s < 1 or s >= n+1:
            print("Out of range! Please try again.\n")
            continue
        t = int(input("Please input the column ordinate of the position you choose:"))
        if t < 1 or t >= n+1:
            print("Out of range! Please try again.\n")
            continue
        s -= 1
        t -= 1
        index = board.click(s,t)
        if index == 0:
            print("Bomb! Game Over!")
            board.visualize()
            break
        else:
            board.visualize()
            checker = input("You lucky dog, let's continue")
                
    if board.check_win() == True:
        print("Congratulations: You win the game!\n")
    else:
        print("Oops, you failed! would you like to try again?\n")
    judger = input("Would you like another game? (y/n):")
    if judger == 'y':
        return 1
    else:
        print("Goodbye! See you next time.\n")
        return 0

if __name__ == "__main__":
    index = main()
    while index == 1:
        index = main()
