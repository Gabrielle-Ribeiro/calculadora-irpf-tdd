from IRPF.SimuladorIRPF import SimuladorIRPF
import pytest


class TestCadastroPensaoAlimenticia:

    PARAMETERS = [
        ([300], 300, 300),
        ([250, 250], 500, 500),
        ([200, 200, 200], 600, 600),
    ]

    @pytest.fixture
    def simulador_irpf(self):
        return SimuladorIRPF()

    @pytest.mark.parametrize("entrada, valor_esperado_pensao, valor_esperado_deducoes", PARAMETERS)
    def test_cadastra_um_novo_rendimento(self, simulador_irpf, entrada, valor_esperado_pensao, valor_esperado_deducoes):
        for valor in entrada:
            simulador_irpf.cadastra_pensao_alimenticia(valor)

        assert simulador_irpf.total_pensao_alimenticia == valor_esperado_pensao
        assert simulador_irpf.total_deducoes == valor_esperado_deducoes


