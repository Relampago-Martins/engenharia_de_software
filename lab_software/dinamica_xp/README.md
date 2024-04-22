# Projeto Inadimplência

- Grupo: Pink Horse

## Como rodar o projeto

```bash
    python3 -m venv .venv
    
    # windows
    ./.venv/scripts/activate

    # ubuntu
    python3 -m venv .venv
    source .venv/bin/activate
    sudo apt install libpq-dev python3-dev

    pip install -r requirements.txt
    python index.py

    #Rodar testes1
    python test.py

    #Rodar testes2
    behave
```

## Escopo do problema

Não se sabe quantos clientes estão devendo e quanto eles devem.

## Solução

Gerar um relatório com a quantidade de clientes que estão devendo e quanto eles devem.

## Histórias (Funcionalidades)

1. Ler arquivo de clientes
2. Ler arquivo de pagamentos
3. Transformar dados dos arquivos em dados manipuláveis
4. Calcular quanto cada cliente deve
5. Combinar os dados de clientes e pagamentos
6. Listar cada cliente que está devendo e quanto ele deve
7. Listar pagamentos já efetuados com valor e cliente que pagou.
8. Listar pagamentos por data de pagamento, em ordem crescente.
9. Testar se programa está funcionando corretamente

## Testes de aceitação

1. Testar se o arquivo pagamentos.csv foi acessado corretamente
2. Testar se o arquivo clientes.csv foi acessado corretamente
3. Testar se pagamentos.csv possui as colunas 'cliente_id', 'valor' e 'foi_pago'
4. Testar se clientes.csv possui as colunas 'id' e 'nome'
5. Testar se a função get_devedores retorna uma lista de dicionários
6. Testar se os aquivos possuem dados além dos cabeçalhos
7. Testar se a função float_to_currency retorna o valor correto
8. Testar se a função get_devedores retorna o nome do cliente
9. Testar se a função get_devedores retorna o valor correto do cliente

## Sprints

| História | Complexidade (pnts)| Horas 3 |
| -------- | -------- | -------- |
| Ler arquivo de clientes   | 2     | 10 minutos     |
| Ler arquivo de pagamentos   | 2     | 10 minutos     |
| Transformar dados dos arquivos em dados manipuláveis    | 0     | 10 minutos     |
| Calcular quanto cada cliente deve    | 13     | 10 minutos     |
| Combinar os dados de clientes e pagamentos    | 5    | 10 minutos     |
| Listar cada cliente que está devendo e quanto ele deve    | 2     | 10 minutos     |
| Listar pagamentos já efetuados com valor e cliente que pagou    | 2     | 10 minutos     |
| Listar pagamentos por data de pagamento, em ordem crescente    | 13     | 10 minutos     |
| Testar se programa está funcionando corretamente    | 20    | 10 minutos     |

## Melhorias

- [X] Integração com supabase

- [X] Criação de testes de conexão com banco de dados
- [ ] Criação de testes de integração

- [X] Integração do csv para o banco de dados (comando COPY)
- [X] Refatorar consultas do index.py para consultar o banco de dados.

## Relatório de atividade

PERGUNTAR E REPOSTAS DO NOTAS (NOTARI)
Explique como foi o processo de programação
adotado.
TDD

O ciclo de vida do TDD foi seguido?
sim

Como foi a experiência de testar antes de escrever
o código?

Foi diferente, quase como uma mudança de paradigma.

O que achastes desta dinâmica?

Legal, foi divertido poder testar esse processo de programação, nunca tinhamos feito testes antes.
