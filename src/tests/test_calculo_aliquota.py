from IRPF.SimuladorIRPF import SimuladorIRPF
import pytest

class TestCalculoAliquota:

    def test_calcula_aliquota(self):
        simulador_irpf = SimuladorIRPF()
        simulador_irpf.cadastra_rendimento("Salario", 1800)

        assert simulador_irpf.calcula_total_imposto() == 0
        assert simulador_irpf.calcula_total_aliquota() == 0

    def test_calcula_outra_aliquota(self):
        simulador_irpf = SimuladorIRPF()
        simulador_irpf.cadastra_rendimento("Salario", 3000)

        assert simulador_irpf.calcula_total_imposto() == pytest.approx(95.20, 0.1)
        assert simulador_irpf.calcula_total_aliquota() == pytest.approx(3.17, 0.1)