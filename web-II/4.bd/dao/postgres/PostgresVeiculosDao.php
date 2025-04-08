<?php

include_once('VeiculoDao.php');
include_once('dao/DAO.php');

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
}

?>