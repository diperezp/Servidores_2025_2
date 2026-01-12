#importamos la libreria de socket
import socket

#informacion del servidor
HOST = "127.0.0.1"
PUERTO=23000
#Instanciamos un objeto de tipo socket para el servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PUERTO)) #enlazamos el socket con la direccion y puerto
    server_socket.listen() #ponemos el socket en modo escucha
    conn, addr = server_socket.accept() #aceptamos conexiones entrantes
    with conn:
        print("Conexion establecida con: ", addr)
        while True:
            data= conn.recv(1024) #recibimos datos del cliente
            if not data:
                break
            conn.sendall(data) #enviamos los datos recibidos de vuelta al cliente

