import random, string

#criar um gerador de senha!

tamanho = int(input("Digite o tamanho de senha que você deseja gerar: "))
chars = string.ascii_letters + string.digits + '!@#&%*$-+=,.;:\/|)(}{[]'
#ascii_uppercase (so letra maiuscula, lowercase quando quiser minúscula)


rnd = random.SystemRandom() #os.urandom gera numero aleatorios a partir de fonte fornecidas pelo S.O

print(''.join(rnd.choice(chars)for i in range(tamanho)))
