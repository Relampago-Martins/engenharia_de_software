/** 
 * Singlenton
*/
class DiscosData{
    discos = [];
    quantidade = 0;
    numeroInicio= 1;

    static instance = null;
    static getInstance(){
        if(DiscosData.instance == null){
            DiscosData.instance = new DiscosData();
        }
        return DiscosData.instance;
    }

    getDiscos(){
        return this.discos;
    }

    getQuantidade(){
        return this.quantidade;
    }

    getNumeroInicio(){
        return this.numeroInicio;
    }

    setDiscos(discos){
        this.discos = discos;
    }

    setQuantidade(quantidade){
        this.quantidade = quantidade;
    }

    setNumeroInicio(numeroInicio){
        this.numeroInicio = numeroInicio;
    }

    addDisco(disco){
        this.discos.push(disco);
    }
}