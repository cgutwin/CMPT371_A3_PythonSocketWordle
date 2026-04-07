# CMPT371 Assignment 3 — Multiplayer Wordle

![Playing the Wordle in two terminal sessions with a server](header_preview.png)

**Course:** CMPT 371 — Data Communications & Networking

**Instructor:** Mirza Zaeem Baig

**Semester:** Spring 2026

## Group Members

| Name              | Student ID | Email                    |
| :---------------- | :--------- | :----------------------- |
| Chris Gutwin      | 301400079  | cgutwin@sfu.ca           |
| Matthew Tortolano | 301505019  | matthew_tortolano@sfu.ca |

## Project Overview & Description

This Co-op project is a multiplayer Wordle game built using Python's Socket API over TCP. It allows a maximum
of two players to connect to the server, pairs them up with another player and see who can solve the puzzle the
fastest in real time! The server deals with all the game logic, while the client side handles all the user
input and UI.

## System Limitations & Edge Cases

Listed below are Limitations from our project and edge cases that solutions have been provided for:

- Localhost Connectivity:
  - Limitation: This project only allows to bind to port 127.0.0.1 (localhost). This was the design choice
    for this project, but doesnt allow for multiplayer games across different networks.
- Single Game Per Connection:
  - Limitation: After the game finishes, the client closes the socket connection with the server. To play again
    the clients would have to reastablish another connection with the server.
- Handling Unsolved Games and Null Solve Times:
  - Solution: When a player runs out of guesses without solving the word, their solve time remains None.
    This would crash the game because it would try to print None. We fixed this by assigning a default value of inf when the client ran out of guesses. Then we would check if their solve_time was an actual value or inf to check win conditions.
  - Limitation: Using inf worked but caused a lot of checks we had to do on the client side to check if solve_time was a value from completing the game or inf from running out of guesses.

<!-- - Clients connect to and play on the localhost machine.
- Closing the server can leave clients with an open connection to nowhere.
- Clients disconnecting may not leave the game session and it won't end.
  - Windows may not play nice with \<Control-C\> and the terminal session should be closed to quit.
- Can only play one game before needing to reconnect and join another lobby. -->

## Video Demo

## Prerequisites (Fresh Environment)

## Step-by-Step Run Guide

## Technical Protocol Details

## Academic Integrity & References

- Code Origin:
  - The socket boilerplate was referenced from the video series "Python Network Programming - TCP/IP Socket Programming" and the python socket library documentation. The game desing, logic and handling was all developed by the group.
- GenAI Usage:
  - Claude Code helped with planning before implementation.
  - CoPilot was used to help with the User Inteface.
  - CoPilot was used when stuck when dealing with the Colorama library.
- Reference:
  - [Python String split()](https://www.geeksforgeeks.org/python/python-string-split/)
  - [Python socket programming - exception handling](https://stackoverflow.com/questions/38544493/python-socket-programming-exception-handling/38545213#38545213)
  - [Print Colorful Text in Python](https://www.youtube.com/watch?v=P3AdKGHmtto)
  - [Stop pyzmq receiver by KeyboardInterrupt](https://stackoverflow.com/questions/17174001/stop-pyzmq-receiver-by-keyboardinterrupt/26392777#26392777)
  - [socket — Low-level networking interface](https://docs.python.org/3/library/socket.html#socket.socket.makefile)

# All stuff below merge with appropiate heading above

## Installation Guide

This project used Python 3.14.

Clone the repository to a place of your choosing:

```sh
git clone https://github.com/cgutwin/cmpt371-project.git dir
cd dir
```

Create a virtual environment and install dependencies:

```sh
python -m venv .venv
```

Activate the virtual environment depending on your terminal and operating system:

```sh
source .venv/Scripts/activate       # bash/zsh (Windows)
source .venv/bin/activate           # bash/zsh (Mac/Linux)
source .venv/Scripts/activate.fish  # fish (Windows)
source .venv/bin/activate.fish      # fish (Mac/Linux)
.\.venv\Scripts\Activate.ps1        # PowerShell (Windows)
```

Install dependencies:

```sh
pip install -r requirements.txt
```

## Running

### Start the Server

Open a terminal session in the project folder. The server will bind to `127.0.0.1` on port `3000`.

```sh
python src/server.py
```

### Connect Player One

In a new terminal window/session, run the client script. Enter your username, and you'll be placed in the waiting lobby until another player joins to make a pair.

```sh
python src/client.py
```

### Connect Player Two

In another new terminal session, run the client script again. Enter your username and you will be paired with Player One. The match, and timer, begins immediately!

```sh
python src/client.py
```

### Gameplay

- The server will randomly choose a word to guess.
- You will be prompted to enter a guess word.
- Each player can make guesses simultaneously.
- If the guess isn't a guessable word, or is too short, you will be informed and told to make another guess.
- The server will validate your guess based on the randomly chosen word, and return back a colour encoding for your guess.
- When one player guesses the word, they will wait for the other to either guess, or run out of guesses, before revealing the winner and time.

## Technical Protocol Details

- **Message Format:** `COMMAND message` (for example: `GUESS crane` may return `GUESS_RESULT GGXYX`)
- **Joining a Game:** `JOIN username` will join the game lobby. If another player hasn't joined, the server sends back `WAITING`. When another player joins, the server manages the game session and sends back `GAME_START` to each client in the game.
- **Gameplay:** Clients are responsible for submitting words with `GUESS <word>`, and the server is responsbible for checking if the guess matches the chosen word, sending back the colour encoding `GUESS_RESULT GGXYX`. When a player solves and the other runs out of guesses, or both run out of guesses, `GAME_OVER` is sent with results of the game to each client.

## References

- Socket boilerplate was taken from the Python documentation on sockets, available at https://docs.python.org/3/library/socket.html#example.

## Development

Create a virtual environment with `python -m venv .venv` as above, activate, and run `pip install -r requirements-dev.txt -r requirements.txt`.

### Available Tools

Run tests:

```sh
python -m pytest
```

Run linter:

```sh
python -m ruff check src tests
```

Run type checker:

```sh
python -m mypy src
```

Format code:

```sh
python -m ruff format src tests
```
