from IRPF.SimuladorIRPF import SimuladorIRPF
import pytest

class TestCadastroDeducoes:

    def test_cadastra_uma_nova_deducao(self):
        simulador_irpf = SimuladorIRPF()
        simulador_irpf.cadastra_deducao("Previdencia privada", 200)

        assert simulador_irpf.total_deducoes == 200