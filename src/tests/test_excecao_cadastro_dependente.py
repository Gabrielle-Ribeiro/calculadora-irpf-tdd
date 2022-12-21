from IRPF.SimuladorIRPF import SimuladorIRPF
import pytest


class TestExecaoCadastroPrevidenciaOficial:

    @pytest.fixture
    def simulador_irpf(self):
        return SimuladorIRPF()

    def test_excecao_nome_em_branco_em_dependente(self, simulador_irpf):
        with pytest.raises(Exception) as resultado:
            simulador_irpf.cadastra_dependente("", "01/01/0001")
        assert "NomeEmBrancoException" in str(resultado)

    def test_excecao_descricao_none_em_dependente(self, simulador_irpf):
        with pytest.raises(Exception) as resultado:
            simulador_irpf.cadastra_dependente(None, "11/11/1111")
        assert "NomeEmBrancoException" in str(resultado)