
import socket
import tkinter as tk
import random
from PIL import Image, ImageTk
import tkinter.font as tkFont


window = tk.Tk()
window.title("Rock, Paper, Scissors")
frame = tk.Frame(window)
frame.pack()


P = Image.open("4 paper.jpg")
R = Image.open("4 rock.jpg")
S = Image.open("4 secc.jpg")
RE= Image.open("4 re_play.jpg")
width, height = RE.size
if width > 100 or height > 100:
    ratio = min(100.0 / width, 100.0 / height)
    width = int(width * ratio)
    height = int(height * ratio)
    RE = RE.resize((width, height), Image.ANTIALIAS)
image_R = ImageTk.PhotoImage(R)
image_P = ImageTk.PhotoImage(P)
image_S = ImageTk.PhotoImage(S)
image_RE= ImageTk.PhotoImage(RE)

def play_game(player_choice):
    # Convert player's choice to integer
    player_choice = int(player_choice)

    # Computer chooses randomly
    computer_choice = random.randint(1, 3)

    # Determine winner
    if player_choice == computer_choice:
        result_label.configure(text="It's a tie!")
    elif player_choice == 1 and computer_choice == 3 or \
         player_choice == 2 and computer_choice == 1 or \
         player_choice == 3 and computer_choice == 2:
        result_label.configure(text="You win!")
    else:
        result_label.configure(text="Computer wins!")

    # Print computer's choice
    if computer_choice == 1:
        computer_choice_label.configure(text="Computer chose Rock")
    elif computer_choice == 2:
        computer_choice_label.configure(text="Computer chose Paper")
    else:
        computer_choice_label.configure(text="Computer chose Scissors")

    # Disable game buttons
    rock_button.config(state=tk.DISABLED)
    paper_button.config(state=tk.DISABLED)
    scissors_button.config(state=tk.DISABLED)

    # Enable play again button
    play_again_button.config(state=tk.NORMAL)
    
    
def reset_game():
    # Clear result and computer choice labels
    result_label.configure(text="")
    computer_choice_label.configure(text="")

    # Enable game buttons
    rock_button.config(state=tk.NORMAL)
    paper_button.config(state=tk.NORMAL)
    scissors_button.config(state=tk.NORMAL)

    # Disable play again button
    play_again_button.config(state=tk.DISABLED)

# Define the GUI elements

player_choice_label = tk.Label(frame, text="Choose your weapon:", font = tkFont.Font(size=20))
player_choice_label.grid(row=0, column=1)

rock_button = tk.Button(frame, image= image_R, command=lambda: play_game(1))
rock_button.grid(row=1, column=0)

paper_button = tk.Button(frame, image= image_P, command=lambda: play_game(2))
paper_button.grid(row=1, column=1)

scissors_button = tk.Button(frame, image= image_S,  command=lambda: play_game(3))
scissors_button.grid(row=1, column=2)

result_label = tk.Label(frame, text="", font = tkFont.Font(size=20))
result_label.grid(row=2, column=0, columnspan=3)

computer_choice_label = tk.Label(frame, text="",font = tkFont.Font(size=20))
computer_choice_label.grid(row=3, column=0, columnspan=3)

play_again_button = tk.Button(frame, image= image_RE, command=reset_game, state=tk.DISABLED)
play_again_button.grid(row=4, column=1)
# Define constants for the IP address and port number
IP = '127.0.0.1'
PORT = 12345

# Get the player's choice
player_choice = input("Choose your weapon (1=Rock, 2=Paper, 3=Scissors): ")

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((IP, PORT))

# Send the player's choice to the server
client_socket.send(player_choice.encode())

# Receive the result from the server
result = client_socket.recv(1024).decode()

# Print the result
print(result)

# Close the connection
client_socket.close()

# Start the GUI event loop
window.mainloop()