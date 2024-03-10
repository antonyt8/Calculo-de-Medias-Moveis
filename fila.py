class FilaArray:

    def __init__(self, capacidade=10):
        self._dados = [None] * capacidade
        self._tamanho = 0
        self._inicio = 0

    def __len__(self):
        return self._tamanho

    def is_empty(self):
        return self._tamanho == 0

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Fila vazia')
        result = self._dados[self._inicio]
        self._dados[self._inicio] = None
        self._inicio = (self._inicio + 1) % len(self._dados)
        self._tamanho -= 1
        return result

    def enqueue(self, elemento):
        if self._tamanho == len(self._dados):
            self._mudar_tamanho(2 * len(self._dados))
        disponivel = (self._inicio + self._tamanho) % len(self._dados)
        self._dados[disponivel] = elemento
        self._tamanho += 1

    def _mudar_tamanho(self, capacidade):
        antigos_dados = self._dados
        self._dados = [None] * capacidade
        for k in range(self._tamanho):
            self._dados[k] = antigos_dados[(self._inicio + k) % len(antigos_dados)]
        self._inicio = 0

    def peek_first(self):
        if self.is_empty():
            raise IndexError('Fila vazia')
        return self._dados[self._inicio]

    def peek_last(self):
        if self.is_empty():
            raise IndexError('Fila vazia')
        return self._dados[(self._inicio + self._tamanho - 1) % len(self._dados)]
