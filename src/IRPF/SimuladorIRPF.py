class SimuladorIRPF:
    def __init__(self, ):
        self.rendimentos = []
        self._total_rendimentos = 0
        self.deducoes = []
        self._total_deducoes = 0
        self.previdencias_oficiais = []
        self._total_pensao_alimenticia = 0
        self.pensoes_alimenticias = []
        self.dependentes = []
        self._total_dependentes = 0

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
        
        if valor is None or valor < 0:
            raise Exception("ValorDeducaoInvalidoException")
        
        self.previdencias_oficiais.append((descricao, valor))
        self._total_deducoes += valor

    def cadastra_pensao_alimenticia(self, valor):
        if valor is None or valor < 0:
            raise Exception("ValorPensaoAlimenticiaInvalidoException")
        self.pensoes_alimenticias.append(valor)
        self._total_pensao_alimenticia += valor
        self._total_deducoes += valor

    @property
    def total_pensao_alimenticia(self):
        return self._total_pensao_alimenticia

    def cadastra_dependente(self, nome, data_nascimento):
        if not nome:
            raise Exception("NomeEmBrancoException")

        self.dependentes.append((nome, data_nascimento))
        self._total_deducoes += 189.59
        self._total_dependentes += 1
    
    @property
    def total_dependentes(self):
        return self._total_dependentes
