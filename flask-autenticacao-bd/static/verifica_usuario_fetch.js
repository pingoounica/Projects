const tx_usuario = document.getElementById("tx-usuario");
const paragrafo_erro = document.getElementById("paragrafo-erro");

tx_usuario.addEventListener("input", function(){
    let usuario = tx_usuario.value;

    if (usuario.trim() === '') {
        paragrafo_erro.textContent = '';
        return;
    }

    fetch("/existe?usuario=" + usuario)
        .then(resposta => resposta.json())
        .then(json => {
            paragrafo_erro.textContent = json.mensagem;
        })
        .catch(() => {
            paragrafo_erro.textContent = 'Erro ao verificar usuario';
        });
});
