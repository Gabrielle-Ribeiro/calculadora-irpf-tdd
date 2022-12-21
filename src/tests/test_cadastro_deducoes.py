from IRPF.SimuladorIRPF import SimuladorIRPF
import pytest


class TestCadastroDeducoes:

    def test_cadastra_uma_nova_deducao(self):
        simulador_irpf = SimuladorIRPF()
        simulador_irpf.cadastra_deducao("Previdencia privada", 200)

        assert simulador_irpf.total_deducoes == 200

    def test_cadastra_duas_novas_deducoes(self):
        simulador_irpf = SimuladorIRPF()
        simulador_irpf.cadastra_deducao("Previdencia privada", 200)
        simulador_irpf.cadastra_deducao("Funpresp", 150)

        assert simulador_irpf.total_deducoes == 350

    def test_cadastra_duas_novas_deducoes(self):
        simulador_irpf = SimuladorIRPF()
        simulador_irpf.cadastra_deducao("Previdencia privada", 100)
        simulador_irpf.cadastra_deducao("Funpresp", 100)
        simulador_irpf.cadastra_deducao("Saude", 112)

        assert simulador_irpf.total_deducoes == 312
