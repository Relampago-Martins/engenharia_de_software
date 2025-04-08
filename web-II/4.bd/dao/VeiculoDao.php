<?php

interface VeiculoDAO{

    public function insere($veiculo);
    public function remove($veiculo);
    public function altera($veiculo);
    public function buscaPorPlaca($placa);
    public function buscaPorNome($nome);
    public function buscaTodos();
}
?>