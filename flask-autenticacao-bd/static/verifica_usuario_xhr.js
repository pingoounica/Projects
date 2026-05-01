const tx_usuario = document.getElementById("tx-usuario");
const paragrafo_erro = document.getElementById("paragrafo-erro");

tx_usuario.addEventListener('input', function(){
    let usuario = tx_usuario.value;

    let xhr = new XMLHttpRequest();
    xhr.open("GET","/existe?usuario=" + usuario);
    xhr.onreadystatechange = function(){
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200){
            let json = JSON.parse(xhr.responseText);
            paragrafo_erro.textContent = json.mensagem;
        }
    }

    xhr.send();
});
