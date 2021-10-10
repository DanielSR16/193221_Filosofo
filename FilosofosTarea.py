import time
from threading import Thread, Lock

mutex = Lock()

tenedores = [1,1,1,1,1]
tenedorFilosofo = []
def toma_cubiertos(name):
    print("Filosofo", name,"Tomo los 2 tenedores")
    tenedorFilosofo.append(tenedores.pop())
    tenedorFilosofo.append(tenedores.pop())


def comer(name):
     if len(tenedorFilosofo)==2:
        print("Filosofo", name, "esta comiendo")   
        time.sleep(1) 
        tenedores.append(tenedorFilosofo.pop())
        tenedores.append(tenedorFilosofo.pop())

def filosofo(name):
    while True:
        time.sleep(1)
        mutex.acquire()
        if len(tenedores) == 5:
            toma_cubiertos(name)
        try:
            comer(name)
        finally:
            print("Filosofo", name,"termino de comer")         
            mutex.release()
            break




for i in range(5):
    fil = Thread(target=filosofo, args=(str(i+1)))
    fil.start()

