from IRPF.SimuladorIRPF import SimuladorIRPF
import pytest


class TestCalculoFaixa1:

    def test_calculo_faixa_1(self):
        simulador_irpf = SimuladorIRPF()
        simulador_irpf.cadastra_rendimento("Salario", 1200)

        assert simulador_irpf.calcula_base_faixa_1() == 1200
        assert simulador_irpf.calcula_imposto_faixa_1() == 0

    def test_outro_calculo_faixa_1(self):
        simulador_irpf = SimuladorIRPF()
        simulador_irpf.cadastra_rendimento("Salario", 1903.98)

        assert simulador_irpf.calcula_base_faixa_1() == 1903.98
        assert simulador_irpf.calcula_imposto_faixa_1() == 0

    def test_terceiro_calculo_faixa_1(self):
        simulador_irpf = SimuladorIRPF()
        simulador_irpf.cadastra_rendimento("Salario", 20000)

        assert simulador_irpf.calcula_base_faixa_1() == 1903.98
        assert simulador_irpf.calcula_imposto_faixa_1() == 0
