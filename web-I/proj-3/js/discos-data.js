/** 
 * Singlenton
*/
class DiscosData{
    discoAtivoId = 0;
    numeroInicio= 1;

    static instance = null;
    static getInstance(){
        if(DiscosData.instance == null){
            DiscosData.instance = new DiscosData();
        }
        return DiscosData.instance;
    }

    getNumeroInicio(){
        return this.numeroInicio;
    }
   
    incNumeroInicio(numeroInicio){
        this.numeroInicio += numeroInicio;
    }

    getDiscoAtivoId(){
        return this.discoAtivoId;
    }

    setDiscoAtivoId(discoAtivoId){
        this.discoAtivoId = discoAtivoId;
    }

}