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

    def test_excecao_descricao_none(self, simulador_irpf):
        with pytest.raises(Exception) as resultado:
            simulador_irpf.cadastra_rendimento(None, 3000)
        assert "DescricaoEmBrancoException" in str(resultado)

    def test_excecao_valor_invalido(self, simulador_irpf):
        with pytest.raises(Exception) as resultado:
            simulador_irpf.cadastra_rendimento("Salario", -1)
        assert "ValorRendimentoInvalidoException" in str(resultado)

    def test_excecao_outro_valor_invalido(self, simulador_irpf):
        with pytest.raises(Exception) as resultado:
            simulador_irpf.cadastra_rendimento("Salario", -100)
        assert "ValorRendimentoInvalidoException" in str(resultado)

    def test_excecao_valor_none(self, simulador_irpf):
        with pytest.raises(Exception) as resultado:
            simulador_irpf.cadastra_rendimento("Salario", None)
        assert "ValorRendimentoInvalidoException" in str(resultado)

