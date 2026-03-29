import socket
import threading
from typing import cast

HOST = ""
PORT = 50000


def send(conn: socket.socket, message: str) -> None:
    conn.sendall((message + "\n").encode())


def parse_message(line: str) -> tuple[str, list[str]] | None:
    parts = line.strip().split()
    if not parts:
        return None
    return parts[0].upper(), parts[1:]


def handle_client(conn: socket.socket, addr: tuple[str, int]) -> None:
    with conn:
        print(f"Connected from {addr}")
        reader = conn.makefile("r")
        for line in reader:
            msg = parse_message(line)
            if msg is None:
                continue
            command, args = msg
            print(f"[{addr}] {command} {args}")

def main() -> None:
    # Create a new TCP (SOCK_STREAM) IPv4 (AF_INET) socket.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # REUSEADDR allows the kernel to reuse a local socket without waiting
        # for its timeout state to expire.
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(5)

        print(f"Listening on port {PORT}")

        # Accept clients in a loop and spawn a thread for them: this will be
        # used later because clients will each run their guesses in real-time.
        while True:
            # Casting to create explicit types for passing.
            # The addr for AF_INET is tuple[str, int] and varies for different
            # protocols.
            result = cast(tuple[socket.socket, tuple[str, int]], s.accept())
            conn, addr = result
            threading.Thread(
                target=handle_client, args=(conn, addr), daemon=True
            ).start()


if __name__ == "__main__":
    main()
