import ipaddress

ip = '192.168.0.0/0'
#endereco = ipaddress.ip_address(ip)
#print(endereco + 2000)  # e possivel adicionar informaçao para imprimir o ip da sequencia ex quero saber o 2000 da sequencia
rede = ipaddress.ip_network(ip, strict=False) #descobrir de qual rede pertence.
#print(ip) para imprimir somente um ip, abaixo imprime toda lista.
for ip in rede:
    print(ip)

