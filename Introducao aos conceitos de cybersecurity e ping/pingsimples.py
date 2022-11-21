import os 

print('#'*60)

#criar uma variavel que recebe um input do usuario com o ip

ip_ou_host = input('Digite o IP ou Host a ser verificado: ')

#chamando o metodo system da biblioteca os, e chamando o comando ping -n 6 vezes. numero de pacotes disparados
os.system('ping -n 6 {}'.format(ip_ou_host))

print('-'*60)


