from IRPF.SimuladorIRPF import SimuladorIRPF


class TestCadastroRendimentos:
    def test_cadastra_um_novo_rendimento(self):
        simulador_irpf = SimuladorIRPF()
        simulador_irpf.cadastra_rendimento("Salário", 10000)

        assert simulador_irpf.total_rendimentos == 10000
