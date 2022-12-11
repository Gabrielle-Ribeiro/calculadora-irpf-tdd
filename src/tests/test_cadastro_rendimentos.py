from IRPF.SimuladorIRPF import SimuladorIRPF


class TestCadastroRendimentos:
    def test_cadastra_um_novo_rendimento(self):
        simulador_irpf = SimuladorIRPF()
        simulador_irpf.cadastra_rendimento("Salário", 10000)

        assert simulador_irpf.total_rendimentos == 10000

    def test_cadastra_dois_novos_rendimentos(self):
        simulador_irpf = SimuladorIRPF()
        simulador_irpf.cadastra_rendimento("Salário", 10000)
        simulador_irpf.cadastra_rendimento("Dividendos", 2000)

        assert simulador_irpf.total_rendimentos == 12000

    def test_cadastra_tres_novos_rendimentos(self):
        simulador_irpf = SimuladorIRPF()
        simulador_irpf.cadastra_rendimento("Salário", 10000)
        simulador_irpf.cadastra_rendimento("Dividendos", 2000)
        simulador_irpf.cadastra_rendimento("Aluguel", 1800)

        assert simulador_irpf.total_rendimentos == 13800
