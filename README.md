# CMPT371 Assignment 3 — Multiplayer Wordle

_Chris Gutwin and Matthew Tortolano_

Play a game of Wordle with others! Pair up with another player and see who can solve the puzzle the fastest!

![Playing the Wordle in two terminal sessions with a server](header_preview.png)

## Installation Guide

Create a virtual environment and install dependencies:

```sh
python -m venv .venv
```

Activate the virtual environment:

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
# for development, do "pip install -r requirements-dev.txt"
```

## Running

To play games, first start the server in a terminal session:

```sh
python src/server.py
```

Then, start the client for each player (if on the same machine, in two separate terminal sessions):

```sh
python src/client.py
```

Enter your username, and you'll be placed in the waiting lobby until another player joins to make a pair. The game starts immediately!

## Limitations

- Clients connect to and play on the localhost machine.
- Closing the server can leave clients with an open connection to nowhere.
- Clients disconnecting may not leave the game session and it won't end.
  - Windows may not play nice with \<Control-C\> and the terminal session should be closed to quit.
- Can only play one game before needing to reconnect and join another lobby.

## Development

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
