import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as erro:
        print("a conexão falhou")
        print("Erro: {}".format(erro))
        sys.exit()

    print("Socket criado com sucesso")

    HostAlvo = input("Digite Host ou Ip a ser conectado: ")
    PortaAlvo = input("Digita a porta a ser conectada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente TCP conectado com sucesso no Host: " + HostAlvo + "e na Porta: "+ PortaAlvo)
        s.shutdown(2)
    except socket.error as erro:
        print("A conexão falhou, não foi possível conectar no Host: " + HostAlvo + "e porta: " + PortaAlvo)
        print("Erro: {}".format(erro))
        sys.exit()

if __name__ == "__main__":
    main()
