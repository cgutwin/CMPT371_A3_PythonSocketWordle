import socket

HOST = '127.0.0.1' 
PORT = 3000


def start_client():

    player_name = input("Please enter your name: ")
    
    # Initializes a socket, AF_INET -> IPV4, SOCK_STREAM -> TCP Protocol
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    client.sendall(f"JOIN:{player_name}\n".encode("utf-8"))
    print(f"{player_name} Connected. Waiting for next Opponent")

    while True:
        # Reads up to 1024 bytes of data that is sent from the server
        # Converts the received bytes into a string using UTF-8 encoding
        data = client.recv(1024).decode("utf-8")

        client.close()
        



def main() -> None:
    print("client")

    guess = input("Guess a word: ").upper()
    if guess == "CAT":
        print("your guess was: " + guess)
    else:
        print("wrong")


if __name__ == "__main__":
    start_client()
    #main()
