from IRPF.SimuladorIRPF import SimuladorIRPF
import pytest


class TestCalculoFaixa3:

    PARAMETERS = [
        (("Salario", 1903.98), 0, 0),
        (("Salario", 2500), 0, 0),
        (("Salario", 3000), 173.35, 26.0025),
        (("Salario", 10000), 924.40, 138.66),
    ]

    @pytest.fixture
    def simulador_irpf(self):
        return SimuladorIRPF()

    @pytest.mark.parametrize("entrada, valor_esperado_base, valor_esperado_imposto", PARAMETERS)
    def test_calculo_faixa_3(self, simulador_irpf, entrada, valor_esperado_base, valor_esperado_imposto):
        simulador_irpf.cadastra_rendimento(entrada[0], entrada[1])

        assert simulador_irpf.calcula_base_faixa_3() == pytest.approx(valor_esperado_base, 0.1)
        assert simulador_irpf.calcula_imposto_faixa_3() == pytest.approx(valor_esperado_imposto, 0.1)
