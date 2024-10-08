# FUT_UFBA

## Descrição do projeto
Este é um projeto feito utilizando o ambiente gráfico Tupy. A ideia foi criar um jogo inspirado no jogo mobile "Head Soccer", lançado em 2012. O jogo foi feito em python, utilizando os conhecimentos adquiridos na disciplina de "Programação orientada a objetos", ministrada pelo professor Rodrigo Rocha. Ele consiste em 2 personagens em um ambiente 2D, que podem ir para frente, para trás e pular. O objetivo do jogo é acertar a bola dentro do gol adversário, localizado na extremidade do seu lado do "campo", o máximo de vezes no tempo de 90 segundos. Para isso, basta acertar a bola com o seu personagem e jogá-la na direção desejada. Ganha aquele que fizer mais gols ao fim do tempo. Além disso, a cada 20 segundos, aproximadamente, uma powerbox aparece no centro do mapa e o personagem que consegue pegá-la (encostando nela) recebe um boost de velocidade e alcance de pulo por aproximadamente 8 segundos. O jogo também possui um botão pause, tal que clicando nele o jogo é pausado, dando duas opções aos jogadores: resume (continuar de onde parou) e restart (reiniciar o jogo).

## Orientações sobre como usar o programa
Para rodar o jogo, rode o arquivo `futufba.py`;

Ao rodar o jogo, o usuário se depara com a tela inicial. Basta pressionar enter, que aparecerão as informações indicando os comandos do jogo para o Player 1 (A, W e D) e Player 2 (setas para esquerda, para direita e para cima);

Para começar, pressione enter novamente e o jogo se inicia automaticamente, o timer começa a rodar e a bola cai do centro do mapa, equidistante dos dois players;

Cada jogador controla o seu player de escolha e interajem com a bola;

Para pausar o jogo, basta clicar no botão de pause no canto superior direito da tela ou apertar a tecla `p`, lá você pode escolher continuar o jogo, clicando em `resume` ou reiniciá-lo, clicando em `restart`

# Integrantes
## Caio Adriel Barbosa dos Santos - 222215084
Contribuições: Auxílio nas discussões de ideias, Implementação inicial do botão pause e resume, implementação do PowerBox e escrita do README.

Nota: 5

## Francisco Silva Santana - 222216228
Contribuições: Física da bola (colisões e gravidade), Detecção de Gol, Organização dos arquivos e constantes, Restart, Parte da implementação de pause, Pulo e Movimentação dos Players, Implementação das telas de início e fim.

Nota: 5

## Laís Abib Gonzalez - 222115785
Contribuições: Discussão de ideias, Implementação do placar, Implementação inicial de colisão Player-Bola e gravação dos vídeos.

Nota: 5

## Lucas Sampaio Souza Andrade - 220115578
Contribuições: Criação das artes do jogo, Adição de rotação da bola, Posicionamento de assets em campo, Idealização de funcionalidades e aplicações.

Nota: 5

# Referências
```sh
https://www.vobarian.com/collisions/2dcollisions2.pdf
```

