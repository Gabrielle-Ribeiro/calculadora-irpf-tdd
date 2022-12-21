from IRPF.SimuladorIRPF import SimuladorIRPF
import pytest


class TestCalculoFaixa1:

    PARAMETERS = [
        (("Salario", 1200), 1200, 0),
        (("Salario", 1903.98), 1903.98, 0),
        (("Salario", 20000), 1903.98, 0),
    ]

    @pytest.fixture
    def simulador_irpf(self):
        return SimuladorIRPF()

    @pytest.mark.parametrize("entrada, valor_esperado_base, valor_esperado_imposto", PARAMETERS)
    def test_calculo_faixa_1(self, simulador_irpf, entrada, valor_esperado_base, valor_esperado_imposto):
        simulador_irpf.cadastra_rendimento(entrada[0], entrada[1])

        assert simulador_irpf.calcula_base_faixa_1() == valor_esperado_base
        assert simulador_irpf.calcula_imposto_faixa_1() == valor_esperado_imposto
