class SimuladorIRPF:
    def __init__(self, ):
        self.rendimentos = []
        self._total_rendimentos = 0

    def cadastra_rendimento(self, descricao, valor):
        if not descricao:
            raise Exception("DescricaoEmBrancoException")
        if valor is None or valor < 0:
            raise Exception("ValorRendimentoInvalidoException")

        self.rendimentos.append((descricao, valor))
        self._total_rendimentos += valor

    @property
    def total_rendimentos(self):
        return self._total_rendimentos
