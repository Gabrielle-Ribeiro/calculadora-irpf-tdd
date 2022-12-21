from IRPF.SimuladorIRPF import SimuladorIRPF
import pytest


class TestCalculoFaixa4:

    PARAMETERS = [
        (("Salario", 2500), 0, 0),
        (("Salario", 4000), 248.95, 56.0138),
        (("Salario", 10000), 913.63, 205.5667),
    ]

    @pytest.fixture
    def simulador_irpf(self):
        return SimuladorIRPF()

    @pytest.mark.parametrize("entrada, valor_esperado_base, valor_esperado_imposto", PARAMETERS)
    def test_calculo_faixa_4(self, simulador_irpf, entrada, valor_esperado_base, valor_esperado_imposto):
        simulador_irpf.cadastra_rendimento(entrada[0], entrada[1])

        assert simulador_irpf.calcula_base_faixa_4() == pytest.approx(valor_esperado_base, 0.1)
        assert simulador_irpf.calcula_imposto_faixa_4() == pytest.approx(valor_esperado_imposto, 0.1)
