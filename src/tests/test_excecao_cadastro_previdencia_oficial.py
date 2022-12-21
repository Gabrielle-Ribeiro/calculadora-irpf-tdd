from IRPF.SimuladorIRPF import SimuladorIRPF
import pytest


class TestExecaoCadastroPrevidenciaOficial:

    @pytest.fixture
    def simulador_irpf(self):
        return SimuladorIRPF()

    def test_excecao_descricao_em_branco_em_previdencia_oficial(self, simulador_irpf):
        with pytest.raises(Exception) as resultado:
            simulador_irpf.cadastra_previdencia_oficial("", 150)
        assert "DescricaoEmBrancoException" in str(resultado)

    def test_excecao_descricao_none_em_previdencia_oficial(self, simulador_irpf):
        with pytest.raises(Exception) as resultado:
            simulador_irpf.cadastra_previdencia_oficial(None, 100)
        assert "DescricaoEmBrancoException" in str(resultado)

    def test_excecao_valor_invalido_em_previdencia_oficial(self, simulador_irpf):
        with pytest.raises(Exception) as resultado:
            simulador_irpf.cadastra_previdencia_oficial("Previdencia Oficial", -2)
        assert "ValorDeducaoInvalidoException" in str(resultado)

    def test_excecao_outro_valor_invalido_em_previdencia_oficial(self, simulador_irpf):
        with pytest.raises(Exception) as resultado:
            simulador_irpf.cadastra_previdencia_oficial("Previdencia Oficial", -200)
        assert "ValorDeducaoInvalidoException" in str(resultado)

    def test_excecao_valor_none_em_previdencia_oficial(self, simulador_irpf):
        with pytest.raises(Exception) as resultado:
            simulador_irpf.cadastra_previdencia_oficial("Previdencia Oficial", None)
        assert "ValorDeducaoInvalidoException" in str(resultado)