from IRPF.SimuladorIRPF import SimuladorIRPF
import pytest

class TestCadastroDepedente:

    def test_cadastra_uma_nova_dependente(self):
        simulador_irpf = SimuladorIRPF()
        simulador_irpf.cadastra_dependente("Carlos Brown", "01/02/2004")

        assert simulador_irpf.total_deducoes == 189.59
        assert simulador_irpf._total_dependentes == 1

    def test_cadastra_dois_novos_dependentes(self):
        simulador_irpf = SimuladorIRPF()
        simulador_irpf.cadastra_dependente("Carlos Brown", "01/02/2004")
        simulador_irpf.cadastra_dependente("Tony Sterco", "05/07/2020")

        assert simulador_irpf.total_deducoes == 379.18
        assert simulador_irpf._total_dependentes == 2

    def test_cadastra_tres_novos_dependentes(self):
        simulador_irpf = SimuladorIRPF()
        simulador_irpf.cadastra_dependente("Carlos Brown", "01/02/2004")
        simulador_irpf.cadastra_dependente("Tony Sterco", "05/07/2020")
        simulador_irpf.cadastra_dependente("Jorel Filho", "07/06/2015")

        assert simulador_irpf.total_deducoes == 568.77
        assert simulador_irpf._total_dependentes == 3