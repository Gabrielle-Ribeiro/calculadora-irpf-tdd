from IRPF.SimuladorIRPF import SimuladorIRPF
import pytest


class TestExcecaoCadastroPensaoAlimenticia:

    @pytest.fixture
    def simulador_irpf(self):
        return SimuladorIRPF()

    def test_excecao_valor_invalido(self, simulador_irpf):
        with pytest.raises(Exception) as resultado:
            simulador_irpf.cadastra_pensao_alimenticia(-15)
        assert "ValorPensaoAlimenticiaInvalidoException" in str(resultado)

    def test_excecao_outro_valor_invalido(self, simulador_irpf):
        with pytest.raises(Exception) as resultado:
            simulador_irpf.cadastra_pensao_alimenticia(-1099)
        assert "ValorPensaoAlimenticiaInvalidoException" in str(resultado)

    def test_excecao_valor_none(self, simulador_irpf):
        with pytest.raises(Exception) as resultado:
            simulador_irpf.cadastra_pensao_alimenticia(None)
        assert "ValorPensaoAlimenticiaInvalidoException" in str(resultado)