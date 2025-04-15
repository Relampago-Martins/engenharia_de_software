<?php

include_once '../VeiculoDao.php';
include_once '../DAO.php';

class PostgresVeiculoDao extends DAO implements VeiculoDao {
    private $table_name = 'veiculo';

    public function insere($veiculo){
        $query = "INSERT INTO " . $this->table_name . 
        " (placa, nome, cor, ano, marca_id) VALUES" .
        " (:placa, :nome, :cor, :ano, :marca_id)";

        $stmt = $this->conn->prepare($query);

        // bind values 
        $stmt->bindParam(":placa", $veiculo->getPlaca());
        $stmt->bindParam(":nome", $veiculo->getNome());
        $stmt->bindParam(":cor", $veiculo->getCor());
        $stmt->bindParam(":ano", $veiculo->getAno());
        $stmt->bindParam(":marca_id", $veiculo->getMarcaId());

        if($stmt->execute()){
            return $this->conn->lastInsertId();;
        }else{
            return -1;
        }
    }


    public function remove($veiculo){
        $query = "DELETE FROM " . $this->table_name . 
        " WHERE id = :id";

        $stmt = $this->conn->prepare($query);

        // bind values 
        $stmt->bindParam(":id", $veiculo->getId());

        if($stmt->execute()){
            return true;
        }else{
            return false;
        }
    }
    public function altera($veiculo){
        return;
    }
    public function buscaPorPlaca($placa){
        return;
    }
    public function buscaPorNome($nome){
        return;
    }

    public function buscaTodos() {
        $query = "SELECT id, placa, nome, cor, ano, marca_id FROM {$this->table_name} ORDER BY id";

        $stmt = $this->conn->prepare($query);
        $stmt->execute();

        $veiculos = [];

        while($row = $stmt->fetch(PDO::FETCH_ASSOC)){
            extract($row);
            $veiculo = new Veiculo(
                $id,
                $nome,
                $placa,
                $placa,
                $cor,
                $marca_id
            );

            array_push($veiculos, $veiculo);
        }
        return $veiculos;
    }

}

?>