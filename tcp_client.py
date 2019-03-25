import socket
import threading

target_host="0.0.0.0"
target_port=9999

#Criar o cliente socket
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connectar o cliente
client.bind((target_host,target_port))
client.listen(5)

print("[*] Escutar em {0}:{1}".format(target_host,target_port))

def handle_client(client):
    request=client.recv(1024)
    print("[*] Recebido: {0}".format(request))

    client.send("Hello world")
    client.close()

while True:
    client, addr = client.accept()
    #accept_connection = ()
    print("[*] Accept connection em {0}:{1}".format(addr[0],addr[1]))
    #print(“Accept connection em {0}:{1}”.format(addr[0], addr[1]))
    # Coloca a thread de cliente em ação para tratar
    # os dados de   entrada
    client_handler = threading.Thread(target=handle_client, args=(client, ))
    client_handler.start()
