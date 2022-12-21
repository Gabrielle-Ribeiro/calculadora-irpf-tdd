from IRPF.SimuladorIRPF import SimuladorIRPF
import pytest

class TestCadastroPrevidenciaOficial:

    PARAMETERS = [
        ([("Previdencia oficial", 400)], 400),
        ([("Previdencia oficial", 300), ("Previdencia oficial 2", 200)], 500),
        ([("Previdencia oficial", 300), ("Previdencia oficial 2", 200), ("Previdencia oficial 3", 100)], 600),
    ]

    @pytest.fixture
    def simulador_irpf(self):
        return SimuladorIRPF()

    @pytest.mark.parametrize("entrada, valor_esperado", PARAMETERS)
    def test_cadastra_uma_nova_previdencia_oficial(self, simulador_irpf, entrada, valor_esperado):
        for descricao, valor in entrada:
            simulador_irpf.cadastra_previdencia_oficial(descricao, valor)

        assert simulador_irpf.total_deducoes == valor_esperado