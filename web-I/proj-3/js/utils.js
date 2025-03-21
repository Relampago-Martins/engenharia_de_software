async function getToken(){
    resp = await fetch(`https://ucsdiscosapi.azurewebsites.net/Discos/autenticar`, {
        method: 'POST',
        headers: {
            'accept': '*/*',
            ChaveApi: chaveAPI
        },
    })
    return resp.text();
}
async function getDiscos(token, quantidade = 12, numeroInicio = 1){
    resp = await fetch(`https://ucsdiscosapi.azurewebsites.net/Discos/records?numeroInicio=${numeroInicio}&quantidade=${quantidade}`, {
        method: 'GET',
        headers: {
            'accept': '*/*',
            TokenApiUCS: token
        },
    })
    return resp.json();
}

async function getDisco(token, id){
    resp = await fetch(`https://ucsdiscosapi.azurewebsites.net/Discos/record?numero=${id}`, {
        method: 'GET',
        headers: {
            'accept': '*/*',
            TokenApiUCS: token
        },
    })
    return resp.json();
}

function renderDiscos(discos){
    discos.forEach(disco => {
        let cardDisco = $('#templateCardDisco').clone();

        cardDisco.attr('id', disco.id);
        cardDisco.removeClass('hidden');
        cardDisco.children('img').attr(
            'src', `data:image/png;base64,${disco.imagemEmBase64}`
        );
        $('#listaDiscos').append(cardDisco);
    });
}
/**
 * Toda vez que o usuário rolar a página até o final, carregar mais discos
 * 
 * Se ((topo da janela + altura da janela) == altura do documento) => carregar mais discos
 */
function setInfinityScroll(token){
    const discosData = DiscosData.getInstance();
    const maximoRegistros = 105;
    
    $(window).scroll(async function(){
        const numeroInicio = (discosData.getNumeroInicio() % (maximoRegistros + 1)) || 1
        let quantidade = 4;
        
        console.log('numeroInicio + quantidade', numeroInicio + quantidade);
        if (numeroInicio + quantidade > maximoRegistros){
            quantidade = maximoRegistros - ( numeroInicio - 1 );
        }
        if($(window).scrollTop() + $(window).height() == $(document).height()){
            const discos = await getDiscos(
                token,
                quantidade,
                numeroInicio,
            );
            renderDiscos(discos);
            discosData.incNumeroInicio(4);
        }
    });
}