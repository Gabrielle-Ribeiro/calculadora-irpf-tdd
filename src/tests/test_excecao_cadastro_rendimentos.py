from IRPF.SimuladorIRPF import SimuladorIRPF
import pytest


class TestExecaoCadastroRendimentos:

    @pytest.fixture
    def simulador_irpf(self):
        return SimuladorIRPF()

    def test_excecao_descricao_em_branco(self, simulador_irpf):
        with pytest.raises(Exception) as resultado:
            simulador_irpf.cadastra_rendimento("", 3000)
        assert "DescricaoEmBrancoException" in str(resultado)
