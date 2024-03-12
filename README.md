## Realização e Entrega

Este projeto foi realizado por [Alan Kelvin](https://github.com/alankelvin-dev), [Antony Thiago](https://github.com/antonyt8) e [Lucas Pereira](https://github.com/lucaspda-1).


# Cálculo de Médias Móveis - Projeto de Estruturas de Dados

## Descrição do Projeto

Este projeto foi desenvolvido como parte da disciplina de Estruturas de Dados do Curso de Bacharelado em Sistemas de Informação do Instituto Federal de Alagoas - Campus Maceió, sob a orientação do Prof. MSc. Ricardo Nunes (ricardo@ifal.edu.br). O objetivo deste projeto é implementar um algoritmo em Python para calcular a média móvel do volume de tráfego em intervalos de tempo específicos para cada interseção em um sistema de monitoramento de tráfego em tempo real.

## Funcionalidades Implementadas

1. **Leitura de Dados do Volume de Tráfego:**
   - O programa permite a leitura dos dados do volume de tráfego a partir do teclado ou de um arquivo texto.

2. **Configuração do Valor K para Média Móvel:**
   - É possível alterar o valor de K, que representa o tamanho da janela de períodos para o cálculo da média móvel. O valor padrão é 7.

3. **Exibição das Médias Móveis Calculadas:**
   - Após a leitura dos dados, o programa exibe as médias móveis calculadas para os períodos de tempo definidos.

4. **Salvamento das Médias Móveis em Arquivo:**
   - Além de exibir as médias móveis, o programa também permite salvar em um arquivo as médias móveis calculadas para os dados lidos.

## Implementação e Restrições

### Definição do Tipo de Dado (TAD) e Funções Auxiliares

- Foi criado um tipo de dado personalizado para armazenar os dados e realizar o cálculo da média móvel. Além disso, foram implementadas funções auxiliares para inicializar a estrutura de deque e calcular a média móvel.

### Tratamento dos Primeiros Elementos

- Para os primeiros K elementos, onde não há elementos anteriores suficientes, atribuímos o valor None para a média móvel.

### Teste e Validação

- O algoritmo foi testado com diferentes conjuntos de dados para garantir que está calculando as médias móveis corretamente.

### Link dos Materias consultados:

https://panda.ime.usp.br/panda/static/pythonds_pt/03-EDBasicos/15-Deques.html
https://www.w3schools.com/python/python_file_open.asp
https://www.instagram.com/reel/C2pFq9NOZar/?igsh=MnYwbWNlbnJ4aXd0
https://classroom.google.com/c/NjM4MTQ4ODM1NjYw/m/NjM4MTQ4ODM1NzMz/details
https://www.udemy.com/course/estrutura-de-dados-e-algoritmos-python-guia-completo/learn/lecture/21139490?start=225#overview
https://www.udemy.com/course/estrutura-de-dados-e-algoritmos-python-guia-completo/learn/lecture/21139484#overview
https://cursos.alura.com.br/forum/topico-duvida-sobre-iteraveis-e-__iter__-161648

### Comentário da equipe sobre se conseguiu ou não realizar tudo o que foi proposto:
- Acho que sim professor , só ficamos com dúvida a respeito de como seria a saída no console do programa e como seria para salvar as médias móveis.

### Comentário destacando possíveis problemas identificados no código, dificuldades encontradas na escrita e/ou funcionalidades que deveriam ser implementadas, mas não foram.
- Não tava conseguindo iterar sobre o deque mas a gente viu que tem um método especial para fazer iterar que é o 
__iter__(). Mas depois mudamos o jeito de fazer a media movel pois tava dando errado. Também não sabiamos como tinha que abrir e ler o arquivo no python com o open.

### Comentário da equipe sobre o desempenho do cálculo da média móvel considerando a notação Big O
- Como tem um  laço for iterando sobre todos os elementos da lista uma vez, resultando em uma complexidade de tempo de O(n), com isso no pior caso vai conferir elemento por elemento 1 , por 1.

