import socket
print()
# Kreiraj socket objekat za TCP/IP komunikaciju
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binduj server na sve interfejse (IP 0.0.0.0) i port 12345
server_socket.bind(('0.0.0.0', 12345))

# Postavi server da sluša dolazne konekcije
server_socket.listen(5)  # Maksimalno 5 konekcija u redu

print("Server čeka na konekcije...")

# Prihvatanje konekcije
conn, addr = server_socket.accept()
print(f"Povezan sa {addr}")

# Prima poruke od klijenta
while True:
    data = conn.recv(1024).decode()
    if not data:
        print("cek sec")
    print(f"Primljena poruka: {data}")

# Zatvori konekciju kada nema više podataka
conn.close()
