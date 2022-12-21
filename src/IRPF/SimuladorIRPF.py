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

    def calcula_base_de_calculo(self):
        return self._total_rendimentos - self._total_deducoes

    def calcula_base_faixa_1(self):
        base_calculo = self.calcula_base_de_calculo()

        if base_calculo <= 1903.98:
            return base_calculo
        return 1903.98

    def calcula_imposto_faixa_1(self):
        return 0

    def calcula_base_faixa_2(self):
        base_calculo = self.calcula_base_de_calculo()

        if base_calculo > (1903.98 + 922.67):
            return 922.67
        elif base_calculo > 1903.98:
            return base_calculo - 1903.98
        return 0

    def calcula_imposto_faixa_2(self):
        return 0.075 * self.calcula_base_faixa_2()

    def calcula_base_faixa_3(self):
        base_calculo = self.calcula_base_de_calculo()

        if base_calculo > (1903.98 + 922.67 + 924.40):
            return 924.40
        elif base_calculo > (1903.98 + 922.67):
            return base_calculo - (1903.98 + 922.67)
        return 0

    def calcula_imposto_faixa_3(self):
        return 0.15 * self.calcula_base_faixa_3()
    
    def calcula_base_faixa_4(self):
        base_calculo = self.calcula_base_de_calculo()

        if base_calculo > (1903.98 + 922.67 + 924.40 + 913.63):
            return 913.63
        elif base_calculo > (1903.98 + 922.67 + 924.40):
            return base_calculo - (1903.98 + 922.67 + 924.40)
        return 0

    def calcula_imposto_faixa_4(self):
        return 0.225 * self.calcula_base_faixa_4()

    def calcula_base_faixa_5(self):
        base_calculo = self.calcula_base_de_calculo()

        if base_calculo > (1903.98 + 922.67 + 924.40 + 913.63):
            return base_calculo - (1903.98 + 922.67 + 924.40 + 913.63)
        return 0

    def calcula_imposto_faixa_5(self):
        return 0.275 * self.calcula_base_faixa_5()

    def calcula_total_imposto(self):
        return (self.calcula_imposto_faixa_1() + 
                self.calcula_imposto_faixa_2() +  
                self.calcula_imposto_faixa_3() +
                self.calcula_imposto_faixa_4() +
                self.calcula_imposto_faixa_5())
    
    def calcula_total_aliquota(self):
        return (self.calcula_total_imposto() * 100 ) / self.calcula_base_de_calculo()