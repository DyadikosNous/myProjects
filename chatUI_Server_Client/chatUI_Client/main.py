import socket
import threading
import tkinter as tk
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8080
Username = ""
class ChatClient:
    def __init__(self, master):
        self.master = master
        master.title("Chat Client")
        self.messages_label = tk.Label(master, text="", font=("Arial", 12),
                                       justify="left")
        self.messages_label.pack(padx=10, pady=10)
        self.message_entry = tk.Entry(master, font=("Arial", 12))
        self.message_entry.pack(padx=10, pady=10, side=tk.LEFT)
        self.message_entry.bind("<Return>", self.send_message)
        self.send_button = tk.Button(master, text="Send", font=("Arial", 12),
                                     command=self.send_message)
        self.send_button.pack(padx=10, pady=10, side=tk.LEFT)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((SERVER_HOST, SERVER_PORT))
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()
    def send_message(self, event=None):
        message = self.message_entry.get()
        self.socket.send(f"{Username}: {message}".encode())
        self.message_entry.delete(0, tk.END)
    def receive_messages(self):
        while True:
            message = self.socket.recv(1024).decode()
            self.messages_label.configure(text=self.messages_label.cget("text")
                                               + message + "\n")
if __name__ == '__main__':
    root = tk.Tk()
    client = ChatClient(root)
    root.mainloop()