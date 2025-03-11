# Implementação do Algoritmo MaxMin Select

## Descrição do Projeto
Este projeto implementa o algoritmo de Seleção Simultânea do Maior e Menor Elementos (MaxMin Select) utilizando a abordagem de divisão e conquista. O algoritmo tem como objetivo encontrar, simultaneamente, o maior e o menor elemento de uma sequência de números de forma eficiente, reduzindo o número de comparações em comparação com uma abordagem ingênua. Ele divide o problema em subproblemas menores, resolve-os recursivamente e combina os resultados.

## Como o Algoritmo Funciona
O algoritmo MaxMin Select utiliza a técnica de divisão e conquista para encontrar o maior e o menor elemento de um array. Ele divide recursivamente o array em duas metades até que cada subproblema contenha um ou dois elementos. A cada divisão, o algoritmo realiza comparações para identificar os maiores e menores valores das sublistas e os combina.

### Passo a Passo da Implementação
1. **Caso base**: Se o array contém um único elemento, ele é tanto o maior quanto o menor.
2. **Caso de dois elementos**: Se o array contém dois elementos, realiza-se uma comparação direta entre eles para determinar o maior e o menor.
3. **Divisão e Conquista**: Para um array maior que dois elementos, o array é dividido em duas metades. O algoritmo é então chamado recursivamente para cada metade.
4. **Combinação dos resultados**: Após a recursão, os maiores e menores elementos das duas metades são combinados para encontrar o maior e o menor valor no array original.

## Como Executar o Projeto
### Pré-requisitos
- Python 3 instalado.

### Passos para Execução
1. Clone este repositório:
   ```bash
   git clone https://github.com//maxmin-select.git
