from IRPF.SimuladorIRPF import SimuladorIRPF
import pytest


class TestCalculoFaixa2:

    PARAMETERS = [
        (("Salario", 1903.98), 0, 0),
        (("Salario", 2500), 596.02, 44.7015),
        (("Salario", 10000), 922.67, 69.2003),
    ]

    @pytest.fixture
    def simulador_irpf(self):
        return SimuladorIRPF()

    @pytest.mark.parametrize("entrada, valor_esperado_base, valor_esperado_imposto", PARAMETERS)
    def test_calculo_faixa_2(self, simulador_irpf, entrada, valor_esperado_base, valor_esperado_imposto):
        simulador_irpf.cadastra_rendimento(entrada[0], entrada[1])

        assert simulador_irpf.calcula_base_faixa_2() == pytest.approx(valor_esperado_base, 0.1)
        assert simulador_irpf.calcula_imposto_faixa_2() == pytest.approx(valor_esperado_imposto, 0.1)
