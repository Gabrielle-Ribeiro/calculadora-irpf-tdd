class SimuladorIRPF:
    def __init__(self, ):
        self.rendimentos = []
        self._total_rendimentos = 0

    def cadastra_rendimento(self, descricao, valor):
        self.rendimentos.append((descricao, valor))
        self._total_rendimentos += valor

    @property
    def total_rendimentos(self):
        return self._total_rendimentos
