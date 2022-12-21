from IRPF.SimuladorIRPF import SimuladorIRPF
import pytest


class TestCadastroPensaoAlimenticia:

    def test_cadastra_uma_pensao_alimenticia(self):
        simulador_irpf = SimuladorIRPF()
        simulador_irpf.cadastra_pensao_alimenticia(300)

        assert simulador_irpf.total_pensao_alimenticia == 300
        assert simulador_irpf.total_deducoes == 300

    def test_cadastra_duas_pensoes_alimenticias(self):
        simulador_irpf = SimuladorIRPF()
        simulador_irpf.cadastra_pensao_alimenticia(250)
        simulador_irpf.cadastra_pensao_alimenticia(250)

        assert simulador_irpf.total_pensao_alimenticia == 500
        assert simulador_irpf.total_deducoes == 500

    def test_cadastra_tres_pensoes_alimenticias(self):
        simulador_irpf = SimuladorIRPF()
        simulador_irpf.cadastra_pensao_alimenticia(200)
        simulador_irpf.cadastra_pensao_alimenticia(200)
        simulador_irpf.cadastra_pensao_alimenticia(200)

        assert simulador_irpf.total_pensao_alimenticia == 600
        assert simulador_irpf.total_deducoes == 600

