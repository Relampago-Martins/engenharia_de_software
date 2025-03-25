<?php
class Estado{
    private $id;
    private $sigla;
    private $nome;

    public function __construct($id, $sigla, $nome)
    {
        $this->id = $id;
        $this->sigla = $sigla;
        $this->nome = $nome;
    }

    public static function withID($id)
    {
        $instance = new self();
        $instance->id = $id;
        return $instance;
    }

    public function getId() { return $this->id; }

    public function getSigla() { return $this->sigla; }
    public function setSigla($sigla) {$this->sigla = $sigla;}

    public function getNome() { return $this->nome; }
    public function setNome($nome) {$this->nome = $nome;}
}

$estados[] = new Estado(1, "AC", "Acre");
$estados[] = new Estado(2, "AL", "Alagoas");
$estados[] = new Estado(3, "AP", "Amapá");
$estados[] = new Estado(4, "AM", "Amazonas");
$estados[] = new Estado(5, "BA", "Bahia");
$estados[] = new Estado(6, "RS", "Rio Grande do Sul");

?>