import socket

# Δημιουργία socket
s = socket.socket()

# Ορισμός "πόρτας" επικοινωνίας (port)
port = 8080
connStatus = "Σύνδεση σε εξέλιξη..."
i = 1

# Σύνδεση στον διακομιστή
while i < 4 and connStatus == "Σύνδεση σε εξέλιξη...":
    try:
        print(connStatus, i)
        s.connect(('localhost', port))
        connStatus = connResponse = s.recv(1024).decode()
        print(connResponse)

        # Αποστολή/Παραλαβή μηνυμάτων
        while True:
            # Αποστολή μηνύματος
            msg = input("Εσείς: ")
            s.send(msg.encode())
            # Λήψη μηνύματος
            data = s.recv(1024).decode()
            print("Διακομιστής: " + data)
    except:
        print("Αδυναμία Σύνδεσης")
        i += 1

# Διακοπή σύνδεσης
s.close()
