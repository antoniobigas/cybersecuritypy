import itertools

string = input('String a Ser Permutada: ')

#metodo permutacao dos caracteres no wordlist.
resultado = itertools.permutations('string', len(string)) #len(string) percorre utiliza a quantidade de caracter inserida no input e usa como parametro
#dos caracteres acima, ele gera todas possibilidades de combinacao
for i in resultado:
    print(''.join(i))
#join junta o caracter um na posicao com o proximo, e assim ocorre o loop de estabelecido em resultado

