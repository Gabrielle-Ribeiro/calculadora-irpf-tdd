class SimuladorIRPF:
    def __init__(self, ):
        self.rendimentos = []
        self._total_rendimentos = 0
        self.deducoes = []
        self._total_deducoes = 0
        self.previdencias_oficiais = []

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

    def cadastra_deducao(self, descricao, valor):
        if not descricao:
            raise Exception("DescricaoEmBrancoException")
        if valor is None or valor < 0:
            raise Exception("ValorRendimentoInvalidoException")

        self.deducoes.append((descricao, valor))
        self._total_deducoes += valor

    @property
    def total_deducoes(self):
        return self._total_deducoes

    def cadastra_previdencia_oficial(self, descricao, valor):
        if not descricao:
            raise Exception("DescricaoEmBrancoException")
        
        self.previdencias_oficiais.append((descricao, valor))
        self._total_deducoes += valor