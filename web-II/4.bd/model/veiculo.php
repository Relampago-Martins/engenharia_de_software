<?php
class Veiculo{
    private $nome;
    private $ano;
    private $placa;
    private $cor;
    private $marca_id;
    private $id;

    public function __construct($id, $nome, $ano, $placa, $cor, $marca_id) {
        $this->id = $id;
        $this->nome = $nome;
        $this->ano = $ano;
        $this->placa = $placa;
        $this->cor = $cor;
        $this->marca_id = $marca_id;
    }

    public function getNome() {
        return $this->nome;
    }

    public function setNome($nome) {
        $this->nome = $nome;
    }

    public function getAno() {
        return $this->ano;
    }

    public function setAno($ano) {
        $this->ano = $ano;
    }

    public function getPlaca() {
        return $this->placa;
    }

    public function setPlaca($placa) {
        $this->placa = $placa;
    }

    public function getCor() {
        return $this->cor;
    }

    public function setCor($cor) {
        $this->cor = $cor;
    }

    public function getMarcaId() {
        return $this->marca_id;
    }
    public function setMarcaId($marca_id) {
        $this->marca_id = $marca_id;
    }

    public function getId() {
        return $this->id;
    }
}

?>