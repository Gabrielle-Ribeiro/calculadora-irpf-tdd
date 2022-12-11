from IRPF.SimuladorIRPF import SimuladorIRPF
import pytest

class TestCadastroRendimentos:

    PARAMETERS = [
        ([("Salário", 10000)], 10000),
        ([("Salário", 10000), ("Dividendos", 2000)], 12000),
        ([("Salário", 10000), ("Dividendos", 2000), ("Aluguel", 1800)], 13800),
    ]

    @pytest.fixture
    def simulador_irpf(self):
        return SimuladorIRPF()

    @pytest.mark.parametrize("entrada, valor_esperado", PARAMETERS)
    def test_cadastra_um_novo_rendimento(self, simulador_irpf, entrada, valor_esperado):
        for descricao, valor in entrada:
            simulador_irpf.cadastra_rendimento(descricao, valor)

        assert simulador_irpf.total_rendimentos == valor_esperado
