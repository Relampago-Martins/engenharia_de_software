package precos;

import precos.descontos.TabelaDePreco;
import precos.fretes.ServicoDeFrete;


/**
 * Classe responsável por calcular o preço de um produto.
 * 
 * SOLID:
 * 	- OCP (Open/Closed Principle)
 * 
 * Muito bem feita a classe,
 * O uso de interfaces para os serviços e desconto garante
 * que a criação de novos tipos de descontos de forma 
 * independente e sem alterar o código existente.
 * 
 * Problema:
 *  - A interface de ServicoDeFrete é simples de mais e os ifs
 *   para calcular o frete são feitos na implementação.
 */
public class CalculadoraDePrecos {
	
	private TabelaDePreco tabela;
	private ServicoDeFrete frete;
	
	public CalculadoraDePrecos(TabelaDePreco tabela, ServicoDeFrete frete) {
		this.tabela = tabela;
		this.frete = frete;
	}

    public double calcula(Produto produto) {
        double desconto = tabela.calculaDesconto(produto.getValor());
        double valorFrete = frete.calculaFrete(produto.getEstado());
        return produto.getValor() * (1 - desconto) + valorFrete;
    }
}