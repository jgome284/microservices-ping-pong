# producer.py
import socket
import cowsay
import random

DESTINATION_HOST = 'consumer'
DESTINATION_PORT = 12345

# pick random character
char = random.choice(cowsay.char_names)
        
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((DESTINATION_HOST, DESTINATION_PORT))
        user_input = input("\nIt's your turn to serve! 🏓\n\n")
        data_to_send = cowsay.get_output_string(char, user_input).encode()
        s.sendall(data_to_send)
        print(f"\nProducer sent: \n{data_to_send.decode()}\n")

        # Receive data from the consumer
        data_received = s.recv(1024).decode()
        print(f"\nProducer received: \n{data_received}\n")
    except (BrokenPipeError, ConnectionResetError, ConnectionRefusedError):
        print("\nConnection failed 💔\n")