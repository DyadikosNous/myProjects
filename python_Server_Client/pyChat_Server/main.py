import socket

# Προετοιμασία διακομιστή
HOST = 'localhost'
PORT = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

# Αναμονή σύνδεσης χρήστη
print('Αναμονή Σύνδεσης..')
conn, addr = s.accept()
print('Συνδέθηκε ο: ', addr)
conn.sendall("Επιτυχής σύνδεση στον διακομιστή!".encode())

# Αποστολή/Παραλαβή μηνυμάτων
while True:
    # Λήψη μηνύματος
    data = conn.recv(1024)
    if not data:
        break
    print(f'Χρήστης: {data.decode()}')

    # Αποστολή μηνύματος
    message = input('Εσείς: ')
    conn.sendall(message.encode())

# Καθαρισμός
print('Η Σύνδεση Τερματίστηκε!')
conn.close()
