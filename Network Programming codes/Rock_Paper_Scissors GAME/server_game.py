

import random
import socket
import tkinter as tk

# Define constants for the IP address and port number
IP = '127.0.0.1'
PORT = 12345


window = tk.Tk()
window.title("Rock, Paper, Scissors")



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
    


# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific IP address and port number
server_socket.bind((IP, PORT))

# Listen for incoming connections
server_socket.listen()

print(f"Server is listening on {IP}:{PORT}")

while True:
    # Wait for a client to connect
    client_socket, client_address = server_socket.accept()
    print(f"Received connection from {client_address}")

    # Receive the player's choicefrom the client
    player_choice = client_socket.recv(1024).decode()
    print(f"Received player choice: {player_choice}")

    # Determine the winner
    result = play_game(player_choice)

    # Send the result back to the client
    client_socket.send(result.encode())

    # Close the connection
    client_socket.close()