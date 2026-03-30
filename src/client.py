import socket

HOST = '127.0.0.1' 
PORT = 3000

def client_guess(client):
    while True:
        client_input = input("Please enter a 5 letter word: ")
        if len(client_input) != 5:
            print("Error: Word must be exactly 5 letters ")
        elif (not client_input.isalpha()):
            print("Error: Word must only contain letters")
        else:
            break
    client.sendall(f"GUESS {client_input}\n".encode("utf-8"))

def start_client():

    player_name = input("Please enter your name: ")
    
    # Initializes a socket, AF_INET -> IPV4, SOCK_STREAM -> TCP Protocol
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Reference: https://stackoverflow.com/questions/38544493/python-socket-programming-exception-handling/38545213#38545213
    try:
        client.connect((HOST, PORT))

        client.sendall(f"JOIN {player_name}\n".encode("utf-8"))
        print(f"{player_name} connected. Waiting for opponent")

        while True:
            # Reads up to 1024 bytes of data that is sent from the server
            # Converts the received bytes into a string using UTF-8 encoding
            message = client.recv(1024).decode("utf-8").strip()
            
            # https://www.geeksforgeeks.org/python/python-string-split/
            parts = message.split()
            command = parts[0]
            # If server sends more than 1 argument, succeeding arguments are stored in a list 
            args = parts[1:] 

            if command == "GAME_START":
                print(f"Game started! Your opponent is {args[0]}")
                
                # TODO: Have function to print gameboard

                # Function to receive input from user first argument should be command 
                client_guess(client)
            
            if command == "INVALID_GUESS":
                print(f"Invalid Guess {args[0]}")
                # Asks client to send another guess due to invalid input
                client_guess(client)

    except ConnectionRefusedError:
        # Server is not running or unreachable
        print("Could not connect to server. Make sure that it is running!")

    except socket.error as e:
        # Any other socket errors that occurs 
        print(f"Network error: {e}")

    finally:    
        client.close()
        



def main() -> None:
    print("client")


if __name__ == "__main__":
    start_client()
    #main()
