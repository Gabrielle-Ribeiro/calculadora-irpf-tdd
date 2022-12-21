from IRPF.SimuladorIRPF import SimuladorIRPF
import pytest


class TestCalculoFaixa5:

    PARAMETERS = [
        (("Salario", 4000), 0, 0),
        (("Salario", 7000), 2335.32, 642.2130),
        (("Salario", 10000), 5335.32, 1467.2130),
    ]

    @pytest.fixture
    def simulador_irpf(self):
        return SimuladorIRPF()

    @pytest.mark.parametrize("entrada, valor_esperado_base, valor_esperado_imposto", PARAMETERS)
    def test_calculo_faixa_4(self, simulador_irpf, entrada, valor_esperado_base, valor_esperado_imposto):
        simulador_irpf.cadastra_rendimento(entrada[0], entrada[1])

        assert simulador_irpf.calcula_base_faixa_5() == pytest.approx(valor_esperado_base, 0.1)
        assert simulador_irpf.calcula_imposto_faixa_5() == pytest.approx(valor_esperado_imposto, 0.1)