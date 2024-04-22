Feature: Relatório de Inadimplência (BDD)
  Eu como gerente de uma loja
  Quero gerar um relatório de inadimplência
  Para saber quem são os clientes que estão devendo e quanto eles devem

  Scenario: Inicialização do sistema
    Given Dado que o sistema está inicializado
    And o banco de dados está conectado
    And as tabelas de clientes e pagamentos existem
    And as tabelas não estão vazias
    When Quando eu abrir a interface do sistema
    Then Então devo ver a tela principal do sistema

  Scenario: Consultar devedores
    Given Dado que tenho clientes que estão devendo,
    And Dado que o sistema está inicializado 
    When Quando eu escolher na interface listar devedores 
    Then Então devo ver uma tabela com os nomes dos clientes e o valor que eles devem
