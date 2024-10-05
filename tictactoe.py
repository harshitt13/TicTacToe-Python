import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Tic Tac Toe")

# Create the game board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Create the buttons for each cell
buttons = []
for i in range(3):
     row = []
     for j in range(3):
          button = tk.Button(window, text=' ', width=10, height=5,
               command=lambda i=i, j=j: make_move(i, j))
          button.grid(row=i, column=j)
          row.append(button)
     buttons.append(row)

# Variable to keep track of the current player
current_player = 'X'

# Function to handle a move
def make_move(row, col):
     global current_player

     # Check if the cell is already occupied
     if board[row][col] != ' ':
          messagebox.showerror("Invalid Move", "This cell is already occupied!")
          return

     # Update the board and the button text
     board[row][col] = current_player
     buttons[row][col].config(text=current_player)

     # Check for a win
     if check_win(current_player):
          messagebox.showinfo("Game Over", f"Player {current_player} wins!")
          reset_game()
          return

     # Check for a draw
     if check_draw():
          messagebox.showinfo("Game Over", "It's a draw!")
          reset_game()
          return

     # Switch to the other player
     current_player = 'O' if current_player == 'X' else 'X'

# Function to check for a win
def check_win(player):
     # Check rows
     for row in board:
          if row.count(player) == 3:
               return True

     # Check columns
     for col in range(3):
          if [board[row][col] for row in range(3)].count(player) == 3:
               return True

     # Check diagonals
     if board[0][0] == board[1][1] == board[2][2] == player:
          return True
     if board[0][2] == board[1][1] == board[2][0] == player:
          return True

     return False

# Function to check for a draw
def check_draw():
     for row in board:
          if ' ' in row:
               return False
     return True

# Function to reset the game
def reset_game():
     global current_player

     # Clear the board
     for i in range(3):
          for j in range(3):
               board[i][j] = ' '
               buttons[i][j].config(text=' ')

     # Reset the current player
     current_player = 'X'

# Start the main loop
window.mainloop()