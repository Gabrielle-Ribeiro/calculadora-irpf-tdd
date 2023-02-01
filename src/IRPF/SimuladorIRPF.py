class SimuladorIRPF:
    TETO_FAIXA_1 = 1903.98
    TETO_FAIXA_2 = 922.67
    TETO_FAIXA_3 = 924.40
    TETO_FAIXA_4 = 913.63
    PORCETAGEM_FAIXA_2 = 0.075
    PORCETAGEM_FAIXA_3 = 0.15
    PORCETAGEM_FAIXA_4 = 0.225
    PORCETAGEM_FAIXA_5 = 0.275
    DEDUCAO_DE_DEPEDENTE = 189.59

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
        self._total_deducoes += self.DEDUCAO_DE_DEPEDENTE
        self._total_dependentes += 1

    @property
    def total_dependentes(self):
        return self._total_dependentes

    def calcula_base_de_calculo(self):
        return self._total_rendimentos - self._total_deducoes

    def calcula_base_faixa_1(self):
        base_calculo = self.calcula_base_de_calculo()
        return self.realiza_calculo_valor_faixa_1(base_calculo)

    def calcula_imposto_faixa_1(self):
        return 0

    def calcula_base_faixa_2(self):
        base_calculo = self.calcula_base_de_calculo()
        return self.realiza_calculo_valor_faixa_2(base_calculo)

    def calcula_imposto_faixa_2(self):
        return self.PORCETAGEM_FAIXA_2 * self.calcula_base_faixa_2()

    def calcula_base_faixa_3(self):
        base_calculo = self.calcula_base_de_calculo()
        return self.realiza_calculo_valor_faixa_3(base_calculo)

    def calcula_imposto_faixa_3(self):
        return self.PORCETAGEM_FAIXA_3 * self.calcula_base_faixa_3()

    def calcula_base_faixa_4(self):
        base_calculo = self.calcula_base_de_calculo()
        return self.realiza_calculo_valor_faixa_4(base_calculo)

    def calcula_imposto_faixa_4(self):
        return self.PORCETAGEM_FAIXA_4  * self.calcula_base_faixa_4()

    def calcula_base_faixa_5(self):
        base_calculo = self.calcula_base_de_calculo()
        return self.realiza_calculo_valor_faixa_5(base_calculo)

    def calcula_imposto_faixa_5(self):
        return self.PORCETAGEM_FAIXA_5 * self.calcula_base_faixa_5()

    def calcula_total_imposto(self):
        imposto = Imposto(self)
        return imposto.calcula_imposto()

    def calcula_total_aliquota(self):
        return (self.calcula_total_imposto() * 100) / self.calcula_base_de_calculo()

    def realiza_calculo_valor_faixa_1(self, base_calculo):
        if base_calculo <= self.TETO_FAIXA_1:
            return base_calculo
        return self.TETO_FAIXA_1

    def realiza_calculo_valor_faixa_2(self, base_calculo):
        if base_calculo > (self.TETO_FAIXA_1 + self.TETO_FAIXA_2):
            return self.TETO_FAIXA_2
        elif base_calculo > self.TETO_FAIXA_1:
            return base_calculo - self.TETO_FAIXA_1
        return 0

    def realiza_calculo_valor_faixa_3(self, base_calculo):
        if base_calculo > (self.TETO_FAIXA_1 + self.TETO_FAIXA_2 + self.TETO_FAIXA_3):
            return self.TETO_FAIXA_3
        elif base_calculo > (self.TETO_FAIXA_1 + self.TETO_FAIXA_2):
            return base_calculo - (self.TETO_FAIXA_1 + self.TETO_FAIXA_2)
        return 0

    def realiza_calculo_valor_faixa_4(self, base_calculo):
        if base_calculo > (self.TETO_FAIXA_1 + self.TETO_FAIXA_2 + self.TETO_FAIXA_3 + self.TETO_FAIXA_4):
            return self.TETO_FAIXA_4
        elif base_calculo > (self.TETO_FAIXA_1 + self.TETO_FAIXA_2 + self.TETO_FAIXA_3):
            return base_calculo - (self.TETO_FAIXA_1 + self.TETO_FAIXA_2 + self.TETO_FAIXA_3)
        return 0

    def realiza_calculo_valor_faixa_5(self, base_calculo):
        if base_calculo > (self.TETO_FAIXA_1 + self.TETO_FAIXA_2 + self.TETO_FAIXA_3 + self.TETO_FAIXA_4):
            return base_calculo - (self.TETO_FAIXA_1 + self.TETO_FAIXA_2 + self.TETO_FAIXA_3 + self.TETO_FAIXA_4)
        return 0


class Imposto:
    def __init__(self, simulador):
        self.imposto_faixa_1 = simulador.calcula_imposto_faixa_1()
        self.imposto_faixa_2 = simulador.calcula_imposto_faixa_2()
        self.imposto_faixa_3 = simulador.calcula_imposto_faixa_3()
        self.imposto_faixa_4 = simulador.calcula_imposto_faixa_4()
        self.imposto_faixa_5 = simulador.calcula_imposto_faixa_5()

    def calcula_imposto(self):
        return (self.imposto_faixa_1 +
                self.imposto_faixa_2 +
                self.imposto_faixa_3 +
                self.imposto_faixa_4 +
                self.imposto_faixa_5)
