from IRPF.SimuladorIRPF import SimuladorIRPF
import pytest

class TestCalculoAliquota:

    PARAMETERS = [
        (("Salario", 1800), 0, 0),
        (("Salario", 3000), 95.20, 3.17),
        (("Salario", 10000), 1880.64, 18.8),
    ]

    @pytest.fixture
    def simulador_irpf(self):
        return SimuladorIRPF()

    @pytest.mark.parametrize("entrada, valor_esperado_imposto, valor_esperado_aliquota", PARAMETERS)
    def test_calculo_aliquota(self, simulador_irpf, entrada, valor_esperado_imposto, valor_esperado_aliquota):
        simulador_irpf.cadastra_rendimento(entrada[0], entrada[1])

        assert simulador_irpf.calcula_total_imposto() == pytest.approx(valor_esperado_imposto, 0.1)
        assert simulador_irpf.calcula_total_aliquota() == pytest.approx(valor_esperado_aliquota, 0.1)