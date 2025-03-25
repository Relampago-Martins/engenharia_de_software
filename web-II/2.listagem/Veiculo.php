<?php
class Veiculo {
    
    private $id;
    private $nome;
    private $placa;
    private $marca;

    public function __construct( $id, $nome, $placa, $marca)
    {
        $this->id=$id;
        $this->nome=$nome;
        $this->placa=$placa;
        $this->marca=$marca;
    }

    public function getId() { return $this->id; }
    public function setId($id) {$this->id = $id;}

    public function getNome() { return $this->nome; }
    public function setNome($nome) {$this->nome = $nome;}

    public function getPlaca() { return $this->placa; }
    public function setPlaca($placa) {$this->placa = $placa;}

    public function getMarca() { return $this->marca; }
    public function setMarca($marca) {$this->marca = $marca;}
}

$veiculo = new Veiculo(1, "Fusca", "ABC-1234", "VW");
$veiculos[0] = $veiculo;
$veiculo = new Veiculo(2, "Gol", "DBC-1884", "VW");
$veiculos[1] = $veiculo;
$veiculo = new Veiculo(3, "Onix", "CFR-1899", "GM");
$veiculos[2] = $veiculo;
$veiculo = new Veiculo(4, "Cruze", "HYS-6543", "GM");
$veiculos[3] = $veiculo;

# ou

$veiculos[] = new Veiculo(5, "Tracker", "MTH-6884", "GM");
$veiculos[] = new Veiculo(6, "C3", "IUJ-4547", "Citroen");
$veiculos[] = new Veiculo(7, "Fastback", "ILJ-5812", "FIAT");
$veiculos[] = new Veiculo(8, "Argo", "IJT-9812", "FIAT");


?>
