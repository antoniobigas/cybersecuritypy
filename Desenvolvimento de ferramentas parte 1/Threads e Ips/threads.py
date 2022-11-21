import time
import threading
import queue

#trabalhando com threads

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto+=velocidade
        time.sleep(0.5)
        print('Piloto: {}  Km: {}'.format(piloto, trajeto))


t_carro1 = threading.Thread(target=carro, args=[1, 'Bruno'])
t_carro2 = threading.Thread(target=carro, args=[2, 'Python'])

t_carro1.start()
t_carro2.start()


