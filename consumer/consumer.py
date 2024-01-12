# consumer.py
import socket
import cowsay
import random
import re

LOCAL_HOST = '0.0.0.0'
LOCAL_PORT = 12345

# pick random character
char = random.choice(cowsay.char_names)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((LOCAL_HOST, LOCAL_PORT))
    s.listen()

    print(f"\nConsumer is listening on port {LOCAL_PORT} (⊙_⊙👂)\n")

    conn, addr = s.accept()
    with conn:
        print(f"(￣y▽￣)╭ Ohohoho..... Connected to {addr}💕 \n")
        data = conn.recv(1024).decode()
        print(f"\nConsumer received: \n{data}\n")

        # Check if the received data has "Ping" (case insensitive)
        if re.search("Ping", data, re.I) is not None:
            response = cowsay.get_output_string(char, "Pong! 🏓").encode()
            conn.sendall(response)
            print(f"\nConsumer sent: \n{response.decode()}\n")
        else:
            response = cowsay.get_output_string(char, "no game 💔").encode()
            conn.sendall(response)
            print(f"\nConsumer sent: \n{response.decode()}\n")