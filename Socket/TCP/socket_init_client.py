import socket

#informacion del servidor
HOST = "127.0.0.1"
PUERTO=23000


#Intanciamos un objeto de tipo socket para el cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # AF_INET-->IPV4, STREAM-->TCP

client_socket.connect((HOST, PUERTO)) #conectamos el socket con la direccion y puerto del servidor

client_socket.sendall(b"Hola desde el cliente") #enviamos datos al servidor
data = client_socket.recv(1024) #recibimos datos del servidor

print("Datos recibidos del servidor: ", data.decode())
client_socket.close() #cerramos la conexion

