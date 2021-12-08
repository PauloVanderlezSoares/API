import pytest
from requests import post


class TesteAPI:
    def setup(self):
        self.url = "http://127.0.0.1:8000"

    def teste_resposta(self):
        resp = post("http://127.0.0.1:8000",
                    json={"val_1": 10, "val_2": 2, "operacao": "adição"})
        assert resp.ok

    def teste_adicao(self):
        resp = post("http://127.0.0.1:8000",
                    json={"val_1": 10, "val_2": 2, "operacao": "adição"})
        assert resp.text == '"10.0 + 2.0 = 12.0"'

    def teste_subtracao(self):
        resp = post("http://127.0.0.1:8000",
                    json={"val_1": 10, "val_2": 2, "operacao": "subtracao"})
        assert resp.text == '"10.0 - 2.0 = 8.0"'

    def teste_multiplicacao(self):
        resp = post("http://127.0.0.1:8000",
                    json={"val_1": 10, "val_2": 2, "operacao": "multiplicacao"})
        assert resp.text == '"10.0 x 2.0 = 20.0"'

    def teste_divisao(self):
        resp = post("http://127.0.0.1:8000",
                    json={"val_1": 10, "val_2": 2, "operacao": "divisão"})
        assert resp.text == '"10.0 / 2.0 = 5.0"'

    def teste_divisao_zero(self):
        resp = post("http://127.0.0.1:8000",
                    json={"val_1": 10, "val_2": 0, "operacao": "divisão"})
        assert resp.text == '"Não existe divisão por 0"'

    def teste_operacao_invalida(self):
        resp = post("http://127.0.0.1:8000",
                    json={"val_1": 10, "val_2": 0, "operacao": "Python"})
        assert resp.text == '"Operação inválida!"'
