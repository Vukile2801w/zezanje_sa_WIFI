import socket

# Kreiraj socket objekat za TCP/IP komunikaciju
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Poveži se na server koristeći njegov javni IP i port
server_ip = "94.189.214.166"  # Zameniti sa stvarnim IP servera
server_port = 12345
client_socket.connect((server_ip, server_port))

# Šalji poruku serveru
message = "Pozdrav od klijenta!"
client_socket.send(message.encode())

# Zatvori konekciju nakon slanja poruke
client_socket.close()
