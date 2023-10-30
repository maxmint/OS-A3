import socket
import threading
import argparse

# Global variables
PORT = None
PATTERN = None
shared_list = []  # List to store received data nodes
lock = threading.Lock()  # Lock for thread safety
book_count = 0  # Counter for received books

# Function to handle a client connection
def handle_client(client_socket):
    global book_count
    book_lines = []  # List to store lines of the current book
    book_next = None  # Pointer to the next node in the current book
    pattern_count = 0  # Counter for pattern occurrences

    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break

        with lock:
            node = {
                'data': data,
                'is_book_line': False,
                'book_next': None,
            }

            if PATTERN in data:
                pattern_count += 1
                node['contains_pattern'] = True
                node['pattern_occurrences'] = pattern_count
                print(f"Pattern '{PATTERN}' found in line {pattern_count}")

            if book_next is not None:
                book_next['book_next'] = node

            shared_list.append(node)
            book_lines.append(node)

            book_next = node

            print(f"Added node: {data}")

    with lock:
        book_count += 1
        for node in book_lines:
            node['is_book_line'] = True
            node['sequence'] = book_count

        print(f"Received Book {book_count}")

        with open(f"book_{book_count:02d}.txt", 'w') as file:
            for node in book_lines:
                file.write(node['data'] + '\n')

        print(f"Pattern '{PATTERN}' occurred {pattern_count} times in this book.")

    client_socket.close()

# Function to print the entire book
def print_book():
    with lock:
        book_lines = [node for node in shared_list if node['is_book_line']]
        book_lines.sort(key=lambda x: x['sequence'])
        book_text = '\n'.join([node['data'] for node in book_lines])
        print(book_text)

# Function to start the server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', PORT))
    server.listen(5)

    print(f"Server listening on port {PORT}...")

    while True:
        client_socket, _ = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

# Function to parse command line arguments
def parse_args():
    global PORT, PATTERN
    parser = argparse.ArgumentParser(description='Multi-threaded network server')
    parser.add_argument('-l', dest='port', type=int, required=True, help='Listen port')
    parser.add_argument('-p', dest='pattern', type=str, required=True, help='Search pattern')
    args = parser.parse_args()
    PORT = args.port
    PATTERN = args.pattern

if __name__ == "__main__":
    parse_args()
    start_server()
