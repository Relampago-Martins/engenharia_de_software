# Projeto Inadimplência

- Grupo: Pink Horse

## Escopo do problema

Não se sabe quantos clientes estão devendo e quanto eles devem.

## Solução

Gerar um relatório com a quantidade de clientes que estão devendo e quanto eles devem.

## Funcionalidades

1. Listar quanto cada cliente deve. Clientes que já pagaram não irão aparecer.
2. Informar quantos clientes estão devendo.
3. Informar valor total a receber.

## Histórias

1. Como gerente, eu quero poder consultar quanto cada cliente que está devendo, para que eu poça cobrar deles se necessário.

2. Como gerente, eu quero poder visualizar, quantos clientes estão devendo, para saber quantos clientes a empresa tem que cobrar.

3. Como gerente quero poder visualizar facilmente todo dia, o valor total a receber, para saber quanto dinheiro a empresa tem a receber.

## Testes de aceitação

1. Dado que eu tenha 3 clientes que devem 100, 200 e 300 reais, quando eu consultar quanto cada cliente deve, então eu devo ver 100, 200 e 300 reais.

2. Dado que eu tenha 3 clientes que devem 100, 200 e 300 reais, quando eu consultar quantos clientes estão devendo, então eu devo ver 3 clientes.

3. Dado que eu tenha 3 clientes que devem 100, 200 e 300 reais, quando eu consultar o valor total a receber, então eu devo ver 600 reais.

## Sprints

## Melhorias

- [ ] Deixar o resultado mais bonito (usando lib `rich` -> `pip install rich`)
