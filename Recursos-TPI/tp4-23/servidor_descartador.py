import socket

IP = '0.0.0.0' #escuchar en todas las interfaces ethX
PORT = 9000

# SOCK_STREAM indica TCP
# AF_INET indica IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((IP, PORT))
sock.listen(1) # 1:cantidad maxima de conexiones en espera de aceptación

print(f"--- Servidor TCP DISCARD escuchando en el puerto {PORT} ---")

#loop principal, en espera de clientes
while True:
    print("Esperando conexión...")
    conn, addr = sock.accept() 
    #se bloquea hasta que un cliente se conecta (y se completa el Handshake)
    #conn: nuevo socket para comunicarse con el cliente
    #addr: tupla con IP y puerto del cliente
    #sock continua escuchando conexiones
    print(f"Conexión establecida desde: {addr}")
    
    try: #manejo de errores simple
        while True:
            data = conn.recv(1024) #lee hasta 1024 bytes
            if not data: # lee b"" si el cliente cerró su escritura (FIN)
                break 
            print(f"Recibido (y descartado): {len(data)} bytes") 
    except Exception as e:
        print(f"Error: {e}")
    finally: #se asegura de siempre cerrar la conexión
        conn.close()
        print(f"Conexión cerrada con {addr}")