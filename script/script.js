document.addEventListener('DOMContentLoaded', function() {
    // Obtenha referências para o botão e o iframe
    var botaoIPCA = document.getElementById('botaoIPCA');
    var botaoOutro = document.getElementById('botaoOutro');
    var botaoSELIC = document.getElementById('botaoSELIC');
    var iframeGrafico = document.getElementById('graficoFrame');

    // Função para trocar o conteúdo do iframe
    function trocarConteudo(src) {
        iframeGrafico.src = src;
    }

    // Adicione um ouvinte de evento de clique ao botão IPCA
    botaoIPCA.addEventListener('click', function() {
        // Chame a função para trocar o conteúdo para grafico.html
        trocarConteudo('grafico.html');
    });

    // Adicione um ouvinte de evento de clique ao botão IPCA
    botaoSELIC.addEventListener('click', function() {
        // Chame a função para trocar o conteúdo para grafico.html
        trocarConteudo('grafico2.html');
    });

    // Adicione um ouvinte de evento de clique ao botão Outro
    botaoOutro.addEventListener('click', function() {
        // Chame a função para trocar o conteúdo para outro-arquivo.html
        trocarConteudo('margemBruta.html');
    });
});
