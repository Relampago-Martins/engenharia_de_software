# Projeto Inadimplência

- Grupo: Pink Horse

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

- [ ] Deixar o resultado mais bonito (usando lib `rich` -> `pip install rich`)
