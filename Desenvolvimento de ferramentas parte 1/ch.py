import hashlib
#comparador de Hash's

#variaveis recebem os arquivos
arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

# do hash lib, recebe novo. 'ripemd160' um algoritmo de hash 160 bits
hash1 = hashlib.new('ripemd160')

hash1.update(open(arquivo1,'rb').read())
#'rb' é um metodo de leitura binário


hash2 = hashlib.new('ripemd160')

hash2.update(open(arquivo2,'rb').read())

#comparar os arquivos

if hash1.digest() != hash2.digest():
#digest eh um resumo passado pelo metodo update != diferente
    print(f'O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}')
    print('O hash do arquivo a.txt é: ', hash1.hexdigest()) #hashdigest resume em hexadicimal e mostra o hash armazenado
    print('O hash do arquivo b.txt é: ', hash2.hexdigest())
else:
    print(f'O Arquivo: {arquivo1} é igual ao arquivo: {arquivo2}')
    print('O hash do arquivo a.txt é: ', hash1.hexdigest()) #hashdigest resume em hexadicimal e mostra o hash armazenado
    print('O hash do arquivo b.txt é: ', hash2.hexdigest())


