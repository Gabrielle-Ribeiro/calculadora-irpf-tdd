from IRPF.SimuladorIRPF import SimuladorIRPF
import pytest

class TestCalculoAliquota:

    def test_calcula_aliquota(self):
        simulador_irpf = SimuladorIRPF()
        simulador_irpf.cadastra_rendimento("Salario", 1800)

        assert simulador_irpf.calcula_total_imposto() == 0
        assert simulador_irpf.calcula_total_aliquota() == 0