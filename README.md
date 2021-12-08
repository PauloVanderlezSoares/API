# API
Essa API criada utilizando o FastAPI, recebe um arquivo JSON com dois valores e uma operação (adição, subtração, multiplicação e divisão), e retorna o resultado da operação entre os dois valores.

## Como utilizar
- Para executar o programa é necessário o módulo FastAPI. O servidor é criado com o código no terminal:

  $ uvicorn main:app --reload

- Para testar as funções da API, é necessário o módulo pytest, utilizando o código:

  $ python3 -m pytest teste_api.py

- Documentação criada com ScanAPI, para gerar documentação:

  $ scanapi run doc_main.yaml

## Outras observaçÕes

Todas requests estão no arquivo do Jupyter Notebook request_api_calculos.ipynb
