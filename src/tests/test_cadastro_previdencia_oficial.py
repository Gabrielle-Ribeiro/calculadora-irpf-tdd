from IRPF.SimuladorIRPF import SimuladorIRPF
import pytest

class TestCadastroPrevidenciaOficial:

    def test_cadastra_uma_nova_previdencia_oficial(self):
        simulador_irpf = SimuladorIRPF()
        simulador_irpf.cadastra_previdencia_oficial("Previdencia oficial", 400)

        assert simulador_irpf.total_deducoes == 400

    def test_cadastra_duas_novas_previdencias_oficiais(self):
        simulador_irpf = SimuladorIRPF()
        simulador_irpf.cadastra_previdencia_oficial("Previdencia oficial", 300)
        simulador_irpf.cadastra_previdencia_oficial("Previdencia oficial 2", 200)

        assert simulador_irpf.total_deducoes == 500

    def test_cadastra_tres_novas_previdencias_oficiais(self):
        simulador_irpf = SimuladorIRPF()
        simulador_irpf.cadastra_previdencia_oficial("Previdencia oficial", 300)
        simulador_irpf.cadastra_previdencia_oficial("Previdencia oficial 2", 200)
        simulador_irpf.cadastra_previdencia_oficial("Previdencia oficial 3", 100)

        assert simulador_irpf.total_deducoes == 600