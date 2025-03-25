<?php

function getEstado($id, $estados){
    $estado = null;
    
    foreach($estados as $std) {
        if($std->getId()==$id){
            $estado = $std; 
        }
    }
    if($estado===null) {
        $estado = new Estado(null, null, null, null);
    }

    return $estado;
}

function alterarEstado(){
    
}

?>