document.addEventListener('DOMContentLoaded', () => {
    const tabuleiro = document.getElementById('tabuleiro');
    const tiro = document.getElementById('tiro');
    let quadrados = [];

    // Criar o tabuleiro dinamicamente
    for (let i = 0; i < 10; i++) {
        for (let j = 0; j < 10; j++) {
            const quadrado = document.createElement('div');
            quadrado.classList.add('quadrado');
            quadrado.dataset.row = i;
            quadrado.dataset.col = j;
            quadrado.addEventListener('click', () => atirarNoQuadro(i, j));
            quadrados.push(quadrado);
            tabuleiro.appendChild(quadrado);
        }
    }

    // Função para atirar no quadrado
    atirarNoQuadro = (row, col) => {
        const quadrado = quadrados.find(s => s.dataset.row == row && s.dataset.col == col);
        quadrado.classList.add('clicado');

        // Adicione aqui a lógica do seu jogo para verificar se acertou ou errou
    };

    // Desabilitar o tabuleiro inicialmente
    desabilitarTabuleiro = () => {
        quadrados.forEach(quadrado => quadrado.style.pointerEvents = 'none');
    };

    // Habilitar o tabuleiro quando o botão de atirar for clicado
    atirar = () => {
        quadrados.forEach(quadrado => quadrado.style.pointerEvents = 'auto');
        tiro.disabled = true;
    };

    // Desabilitar o tabuleiro inicialmente
    desabilitarTabuleiro();
});