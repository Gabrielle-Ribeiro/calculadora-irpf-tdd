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

    def test_excecao_descricao_none_em_deducoes(self, simulador_irpf):
        with pytest.raises(Exception) as resultado:
            simulador_irpf.cadastra_deducao(None, 10)
        assert "DescricaoEmBrancoException" in str(resultado)

    def test_excecao_valor_invalido_em_deducoes(self, simulador_irpf):
        with pytest.raises(Exception) as resultado:
            simulador_irpf.cadastra_deducao("Saude", -1)
        assert "ValorRendimentoInvalidoException" in str(resultado)

    def test_excecao_outro_valor_invalido_em_deducoes(self, simulador_irpf):
        with pytest.raises(Exception) as resultado:
            simulador_irpf.cadastra_deducao("Previdencia privada", -100)
        assert "ValorRendimentoInvalidoException" in str(resultado)

    def test_excecao_valor_none_em_deducoes(self, simulador_irpf):
        with pytest.raises(Exception) as resultado:
            simulador_irpf.cadastra_deducao("Saude", None)
        assert "ValorRendimentoInvalidoException" in str(resultado)

