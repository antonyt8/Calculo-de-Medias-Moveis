from fila import *

class Deque:

    def __init__(self):
        self._deque = FilaArray()

    def add_last(self, elemento):
        self._deque.enqueue(elemento)

    def delete_first(self):
        return self._deque.dequeue()

    def first(self):
        return self._deque.peek_first()

    def __len__(self):
        return len(self._deque)

    def add_first(self, elemento):
        fila_aux = FilaArray()
        fila_aux.enqueue(elemento)
        fila_aux._tamanho += 1
        while not self._deque.is_empty():
            fila_aux.enqueue(self._deque.dequeue())
        self._deque = fila_aux

    def delete_last(self):
        fila_aux = FilaArray()
        while not self._deque.is_empty():
            if len(self._deque) == 1:
                return self._deque.dequeue()
            fila_aux.enqueue(self._deque.dequeue())
        ultimo_elemento = fila_aux.dequeue()
        while not fila_aux.is_empty():
            self._deque.enqueue(fila_aux.dequeue())
        return ultimo_elemento

    def last(self):
        return self._deque.peek_last()

    def is_empty(self):
        return self._deque.is_empty()


deque = Deque()

deque.add_first(1)
deque.add_last(2)
deque.add_first(3)

print(deque.first())  
print(deque.last())  

deque.delete_first()
deque.delete_last()

print(deque.is_empty())  

print(len(deque))  