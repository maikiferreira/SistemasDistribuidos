import socket, subprocess

host = '10.3.2.62'
server_port = 5100      
      
# Criando a conexão

def verificaConexao():
	while (True):
		print('\nDigite suas mensagens')
		mensagem = input()
		saida = subprocess.getstatusoutput(mensagem)
		print(saida[1])

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	tcp.connect((host, server_port))

	print('\nDigite suas mensagens')

	mensagem = input()

	# Enviando a mensagem 
	while mensagem != '\x18':   
		tcp.send(str(mensagem).encode())
		mensagemRecebida = str(tcp.recv(1024).decode())
		if(mensagemRecebida != '\x18'):
			print(mensagemRecebida)
			mensagem = input()
		else:
			mensagem = mensagemRecebida

	else:
		verificaConexao()
	tcp.close()

except (socket.error, socket.gaierror, socket.herror, socket.timeout):
	verificaConexao()
