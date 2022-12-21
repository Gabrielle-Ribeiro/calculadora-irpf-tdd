from IRPF.SimuladorIRPF import SimuladorIRPF
import pytest

class TestCadastroDepedente:

    PARAMETERS = [
        ([("Carlos Brown", "01/02/2004")], 189.59, 1),
        ([("Carlos Brown", "01/02/2004"), ("Tony Sterco", "05/07/2020")], 379.18, 2),
        ([("Carlos Brown", "01/02/2004"), ("Tony Sterco", "05/07/2020"), ("Jorel Filho", "07/06/2015")], 568.77, 3),
    ]

    @pytest.fixture
    def simulador_irpf(self):
        return SimuladorIRPF()

    @pytest.mark.parametrize("entrada, valor_esperado_deducoes, valor_esperado_dependentes", PARAMETERS)
    def test_cadastra_dependente(self, simulador_irpf, entrada, valor_esperado_deducoes, valor_esperado_dependentes):
        for nome, data_nascimento in entrada:
            simulador_irpf.cadastra_dependente(nome, data_nascimento)
        assert simulador_irpf.total_deducoes == valor_esperado_deducoes
        assert simulador_irpf.total_dependentes == valor_esperado_dependentes