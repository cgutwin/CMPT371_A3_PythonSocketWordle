# CMPT371 Assignment 3
Chris Gutwin and Matthew Tortolano

## Setup
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
pip install -r requirements-dev.txt
```

## Running
Start the server:
```sh
python src/server.py
```
Start the client:
```sh
python src/client.py
```

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
