document.addEventListener('DOMContentLoaded', function() {
    // Obtenha referências para o botão e o iframe
    var botaoIPCA = document.getElementById('botaoIPCA');
    var botaoOutro = document.getElementById('botaoOutro');
    var botaoSELIC = document.getElementById('botaoSELIC');
    var botaoPIB = document.getElementById('botaoPIB');
    var iframeGrafico = document.getElementById('graficoFrame');
    var tituloApresentacao = document.getElementById('tituloApresentacao');

    // Função para trocar o conteúdo do iframe
    function trocarConteudo(src, largura, altura) {
        iframeGrafico.src = src;
        iframeGrafico.style.width = largura;
        iframeGrafico.style.height = altura;
    }

    // Função para trocar o Titulo
    function trocarTitulo(titulo) {
        tituloApresentacao.innerText = titulo;
    }

    // Adicione um ouvinte de evento de clique ao botão IPCA
    botaoIPCA.addEventListener('click', function() {
        // Chame a função para trocar o conteúdo para grafico.html
        trocarConteudo('grafico.html',"530","1260");
        trocarTitulo('Variação IPCA - Indice de Preço ao Consumidor Amplo');
    });

    // Adicione um ouvinte de evento de clique ao botão IPCA
    botaoSELIC.addEventListener('click', function() {
        // Chame a função para trocar o conteúdo para grafico.html
        trocarConteudo('grafico2.html',"530","1200");
        trocarTitulo('Taxa Selic');
    });


    // Adicione um ouvinte de evento de clique ao botão Outro
    botaoOutro.addEventListener('click', function() {
        // Chame a função para trocar o conteúdo para outro-arquivo.html
        trocarConteudo('margemBruta.html',100,100);
        trocarTitulo('');
    });

        // Adicione um ouvinte de evento de clique ao botão Outro
        botaoPIB.addEventListener('click', function() {
            // Chame a função para trocar o conteúdo para outro-arquivo.html
            trocarConteudo('pib.html',300,800);
            trocarTitulo('Crescimento Trimestral do PIB');
        });
});
