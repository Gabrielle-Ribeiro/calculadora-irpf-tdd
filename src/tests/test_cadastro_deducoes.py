from IRPF.SimuladorIRPF import SimuladorIRPF
import pytest


class TestCadastroDeducoes:

    PARAMETERS = [
        ([("Previdencia privada", 200)], 200),
        ([("Previdencia privada", 200), ("Funpresp", 150)], 350),
        ([("Previdencia privada", 100), ("Funpresp", 100), ("Saude", 112)], 312),
    ]

    @pytest.fixture
    def simulador_irpf(self):
        return SimuladorIRPF()

    @pytest.mark.parametrize("entrada, valor_esperado", PARAMETERS)
    def test_cadastra_uma_nova_deducao(self, simulador_irpf, entrada, valor_esperado):
        for descricao, valor in entrada:
            simulador_irpf.cadastra_deducao(descricao, valor)

        assert simulador_irpf.total_deducoes == valor_esperado

