import socket

target_host="www.google.com"
target_port=80

#Criar o cliente socket
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connectar o cliente
client.connect((target_host,target_port))

#Enviar dados
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#Recebe dados

response=client.recv(4096)

print(response)
