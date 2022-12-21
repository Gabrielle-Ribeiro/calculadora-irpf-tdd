from IRPF.SimuladorIRPF import SimuladorIRPF
import pytest


class TestExecaoCadastroDeducoes:

    @pytest.fixture
    def simulador_irpf(self):
        return SimuladorIRPF()

    def test_excecao_descricao_em_branco_em_deducoes(self, simulador_irpf):
        with pytest.raises(Exception) as resultado:
            simulador_irpf.cadastra_deducao("", 130)
        assert "DescricaoEmBrancoException" in str(resultado)

    def test_excecao_descricao_none(self, simulador_irpf):
        with pytest.raises(Exception) as resultado:
            simulador_irpf.cadastra_rendimento(None, 10)
        assert "DescricaoEmBrancoException" in str(resultado)


