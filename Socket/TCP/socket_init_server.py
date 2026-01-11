#importamos la libreria de socket
import socket

#informacion del servidor
HOST = "127.0.0.1"
PUERTO=23000
#Instanciamos un objeto de tipo socket para el servidor
server_scket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # AF_INET-->IPV4, STREAM-->TCP
server_scket.bind((HOST, PUERTO)) #enlazamos el socket con la direccion y puerto

server_scket.listen(1) #el servidor queda a la espera de conexiones
print("El servidor esta escuchando en el puerto: ", PUERTO)

conn,addr = server_scket.accept() #aceptamos la conexion de un cliente
print("Conexion establecida con: ", addr)

data=conn.recv(1024) #recibimos datos del cliente
print("Datos recibidos del cliente: ", data.decode())

conn.sendall(b"Hola desde el servidor") #enviamos datos al cliente
conn.close() #cerramos la conexion
