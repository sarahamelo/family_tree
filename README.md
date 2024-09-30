# Permutação de Árvore Genealógica

### Sobre o projeto
O projeto tem como objetivo calcular as permutações de uma árvore genealógica onde só é permitido colocar
nome e idade de cada membro da família e, de acordo com os casos de negócio, o programa irá calcular todas
as possibilidades.

### Casos de Negócio
Para que o programa fique o mais perto da realidade possível, criamos alguns casos de negócio. Claro, nem
todas as famílias seguem esse padrão, mas foi nossa solução para que a árvore fique mais coesa e mais realista.

1. Uma pessoa mais nova não pode ser genitora de uma pessoa mais velha;
2. Se a diferença de idade entre duas pessoas for 15 anos ou menos, elas devem ser consideradas irmãs ou um casal;
3. Se a diferença de idade entre duas pessoas for mais de 15 anos e menos de 50, elas devem ser consideradas filho e pai;
4. Se a diferença de idade entre duas pessoas for mais de 50 anos e menos de 80, elas devem ser consideradas avô e neto;
5. Se a diferença de idade entre duas pessoas for mais de 80 anos, elas devem ser consideradas bisavô e bisneto.

Vamos primeiro realizar a **análise sintática** (ou análise gramatical) e, em seguida, a análise do tempo de execução usando a notação Big O.

## Análise Sintática do Código

A análise sintática envolve a decomposição do código em suas unidades fundamentais, como estruturas de controle, chamadas de função e atribuições. Vamos dividir o código por partes.

#### Função `definir_relacoes_possiveis(pessoa1, pessoa2)`

- **Cabeçalho**: Define uma função com dois parâmetros (`pessoa1`, `pessoa2`), ambos sendo tuplas que contêm nome e idade.
  
  ```python
  def definir_relacoes_possiveis(pessoa1, pessoa2):
  ```

- **Desempacotamento de tuplas**:
  
  ```python
  nome1, idade1 = pessoa1
  nome2, idade2 = pessoa2
  ```

  Aqui as tuplas `pessoa1` e `pessoa2` são desempacotadas para atribuir valores às variáveis `nome1`, `idade1`, `nome2` e `idade2`.

- **Atribuição de lista vazia**:
  
  ```python
  relacoes = []
  ```

  Inicializa uma lista vazia para armazenar as relações possíveis.

- **Estruturas condicionais**: O código contém múltiplos blocos de `if-elif` que verificam diferenças de idade para inferir as relações. O fluxo de controle segue as condições de idade para diferentes relações.

  ```python
  if idade1 > idade2 and 20 <= (idade1 - idade2) <= 50:
      relacoes.append('pai/mãe')
  ```

  Similarmente, há outros blocos condicionais para "irmão/irmã", "casal", "avô/avó", etc.

- **Retorno**:

  ```python
  return relacoes
  ```

  Retorna a lista de relações possíveis entre duas pessoas.

#### Função `gerar_combinacoes(membros)`

- **Cabeçalho**: Define a função que recebe a lista de membros e retorna as combinações de relações.

  ```python
  def gerar_combinacoes(membros):
  ```

- **Laço duplo**: O loop aninhado percorre todos os pares de membros (sem repeti-los).

  ```python
  for i in range(len(membros)):
      for j in range(i + 1, len(membros)):
  ```

  Este laço usa índices para comparar cada pessoa com todas as outras que vêm após ela na lista.

- **Chamada de função**:

  ```python
  relacoes = definir_relacoes_possiveis(pessoa1, pessoa2)
  ```

  Chama a função `definir_relacoes_possiveis` para calcular as possíveis relações entre `pessoa1` e `pessoa2`.

- **Adição à lista**:

  ```python
  combinacoes_possiveis.append([pessoa1[0], pessoa2[0], relacao])
  ```

  Para cada relação encontrada, o código a armazena na lista de combinações.

#### Função `gerar_permutacoes_validas(membros, combinacoes)`

- **Cabeçalho**: Define a função que recebe os membros e as combinações e gera permutações válidas.

  ```python
  def gerar_permutacoes_validas(membros, combinacoes):
  ```

- **Função recursiva**: Define a função recursiva `gerar` para construir as permutações incrementais.

  ```python
  def gerar(permutacao_atual, pessoas_na_permutacao):
  ```

  A função recursiva verifica se todas as pessoas foram conectadas e adiciona a permutação à lista se a condição for satisfeita.

- **Chamada recursiva**:

  ```python
  gerar(nova_permutacao, novas_pessoas_na_permutacao)
  ```

  A função chama a si mesma recursivamente até que todas as combinações válidas tenham sido geradas.

#### Função `arvore_genealogica()`

- **Cabeçalho**: Função principal que interage com o usuário e coordena as funções anteriores.

  ```python
  def arvore_genealogica():
  ```

- **Entrada de dados**: Solicita nomes e idades e os armazena em uma lista de membros.

  ```python
  nome = input("Nome: ").strip()
  ```

- **Verificação**: Garante que pelo menos duas pessoas tenham sido inseridas antes de prosseguir.

  ```python
  if len(membros) < 2:
      print("É necessário pelo menos duas pessoas para gerar a árvore genealógica.")
      return
  ```

- **Chamada das funções**: Gera combinações e permutações válidas e as exibe.

  ```python
  combinacoes = gerar_combinacoes(membros)
  permutacoes = gerar_permutacoes_validas(membros, combinacoes)
  ```

---

## Complexidade de Tempo

### O que é Complexidade de Tempo (Big O)?

A **complexidade de tempo** (Big O) nos diz como o tempo de execução de um algoritmo cresce à medida que a entrada aumenta. No seu caso, estamos falando de como o código responde conforme você adiciona mais pessoas (membros da família).

- **O(1)** significa que o tempo de execução é **constante**, ou seja, o tempo não muda independentemente do número de membros. 
- **O(n)** significa que o tempo de execução **cresce linearmente**, ou seja, o tempo aumenta proporcionalmente ao número de membros.
- **O(n²)** significa que o tempo de execução **cresce quadraticamente**, ou seja, se o número de membros dobra, o tempo de execução pode quadruplicar.
- **O(n!)** (fatorial) significa que o tempo de execução **cresce muito rapidamente** com o aumento da entrada, tornando o código **extremamente lento para grandes números**.

### 2. Função `definir_relacoes_possiveis`

Essa função compara a idade de duas pessoas e decide quais relações familiares elas podem ter (pai/mãe, filho, etc.). Ela sempre faz a mesma quantidade de verificações, independentemente do número de pessoas na lista.

- **Complexidade**: **O(1)** (tempo constante).
  
  Isso significa que o tempo que a função leva para ser executada **não muda** dependendo do número de membros da família. Toda vez que ela é chamada, leva o mesmo tempo para rodar, independentemente da quantidade de pessoas.

### 3. Função `gerar_combinacoes`

#### O que é O(n²)?

Quando falamos em **O(n²)**, estamos nos referindo ao fato de que o número de operações (ou comparações) **cresce quadraticamente** com o número de elementos. Isso geralmente acontece quando estamos comparando todos os pares possíveis de elementos em um conjunto.

No caso da função `gerar_combinacoes`, estamos gerando todos os **pares** de pessoas, o que significa que precisamos calcular quantos pares únicos podemos formar a partir de um grupo de `n` pessoas.

#### Fórmula para Comparações de Pares

Se você tiver `n` pessoas, o número de comparações de pares possíveis é dado pela fórmula de **combinação** de 2 elementos entre `n`:

C(n,2) = n(n-1)/2

Essa fórmula nos diz quantos pares distintos podemos formar a partir de um grupo de `n` pessoas. Agora vamos aplicar isso aos exemplos mencionados.

#### Exemplo 1: 2 pessoas

Se você tem 2 pessoas (n = 2), o número de comparações de pares é:

C(2,2) = 2(2-1)/2 = 2*1/2 = 1

Isso significa que com 2 pessoas, há **1** comparação possível (comparando a primeira pessoa com a segunda).

#### Exemplo 2: 3 pessoas

Se você tem 3 pessoas (n = 3), o número de comparações de pares é:

C(3,2) = 3(3-1)/2 = 3*2/2 = 3

Isso significa que com 3 pessoas, você pode fazer **3** comparações (comparando cada pessoa com as outras duas).

#### Exemplo 3: 10 pessoas

Se você tem 10 pessoas (n = 10), o número de comparações de pares é:

C(10,2) = 10(10-1)/2 = 10*9/2 = 45

Isso significa que com 10 pessoas, há **45** comparações possíveis.

#### Por que isso acontece?

A explicação é que estamos comparando **todos os pares** de pessoas, mas sem repetir combinações. Então, por exemplo, se compararmos a pessoa A com a pessoa B, não precisamos comparar B com A novamente, pois já fizemos essa comparação.

Essa é a natureza da combinação **C(n, 2)**: selecionamos 2 pessoas de um grupo de `n` sem importar a ordem, o que nos dá o número total de pares distintos.

#### Resumo

- Com **2 pessoas**, há **1** comparação (A com B).
- Com **3 pessoas**, há **3** comparações (A com B, A com C, B com C).
- Com **10 pessoas**, há **45** comparações.

O crescimento segue a fórmula de combinação, que é proporcional a **n²**. Portanto, a complexidade é **O(n²)**, pois o número de comparações cresce quadraticamente conforme o número de pessoas aumenta.

### 4. Função `gerar_permutacoes_validas(membros, combinacoes)`

Esta função é responsável por gerar **todas as permutações possíveis** de conexões (ou seja, relações familiares) entre os membros da família, usando as combinações geradas anteriormente. Agora vamos explicar o que isso significa em termos de **complexidade** e **tempo de execução**.

#### O que a função faz:

1. Ela **tenta criar uma permutação de relações** entre as pessoas, onde cada pessoa é conectada a outra pessoa com uma relação específica (por exemplo, pai, mãe, irmão, etc.).
2. A função utiliza **recursão** para testar todas as maneiras possíveis de conectar as pessoas com base nas combinações de relações.
3. O objetivo é **conectar todas as pessoas sem repetir relações**, o que resulta em um grande número de permutações.

#### Complexidade O(n²!)

- **Por que O(n²!)?**
  A complexidade de **O(n²!)** (fatorial quadrático) vem do fato de que estamos gerando **todas as permutações** de combinações de relações. 

  Vamos dividir essa explicação:

  - **Combinações de pares**: A função `gerar_combinacoes` gera todas as possíveis combinações de pares entre os membros. Como explicado anteriormente, o número de combinações é **O(n²)**, ou seja, para `n` pessoas, o número de pares possíveis cresce quadraticamente.
  
  - **Permutações de combinações**: Agora, para cada conjunto de combinações gerado, a função `gerar_permutacoes_validas` tenta organizar essas combinações em todas as formas possíveis de conectar as pessoas. Isso envolve testar todas as **permutações** dessas combinações.

  O número de permutações de `n` itens (neste caso, as combinações de relações) é **n!** (fatorial). Então, se você tem `k` combinações, o número de permutações possíveis será **k!**.

  Como já sabemos que o número de combinações possíveis é **O(n²)**, a complexidade final será **O((n²)!)**, ou seja, **fatorial em relação ao número de combinações quadráticas**.

#### Exemplo Simples:

- Imagine que você tenha 3 pessoas (A, B, C).
- O número de combinações de pares de pessoas seria **C(3, 2) = 3** (A com B, A com C, B com C).
- Agora, a função precisa gerar todas as **permutações** dessas 3 combinações, o que dá **3! = 6 permutações**.

Conforme o número de pessoas aumenta, o número de combinações e permutações aumenta drasticamente, o que explica o crescimento fatorial.

### 5. Função `arvore_genealogica()`

A função `arvore_genealogica` é a **função principal**, que combina todas as outras funções para gerar a árvore genealógica. Ela recebe os membros da família e coordena as seguintes operações:

1. **Recebe a entrada**: Solicita ao usuário para inserir o nome e a idade dos membros da família.
2. **Verifica se há membros suficientes**: Ela garante que há pelo menos duas pessoas para começar a gerar a árvore genealógica.
3. **Chama as funções**:
   - Chama `gerar_combinacoes` para gerar todas as combinações possíveis de pares de pessoas.
   - Chama `gerar_permutacoes_validas` para gerar todas as permutações válidas que conectam os membros.

#### Complexidade O(n²!)

A função `arvore_genealogica` é dominada pelo tempo de execução das funções que ela chama, especialmente a função `gerar_permutacoes_validas`, que, como vimos, tem complexidade **O(n²!)**.

- **Por que O(n²!)?**
  Como o tempo de execução da função `arvore_genealogica` depende principalmente do tempo de execução de `gerar_permutacoes_validas`, a complexidade geral da função será a mesma: **O(n²!)**.

#### Impacto na Prática

- Para **poucos membros** (por exemplo, 3 ou 4), a função pode ser executada de forma relativamente rápida.
- Para **muitos membros** (10 ou mais), o número de permutações cresce rapidamente, tornando a função muito lenta, já que o número de combinações e permutações se torna muito grande.

### Resumo Simplificado

**Conclusão**: Para **poucos membros** (2, 3, 4), o código é rápido e responsivo. Para **muitos membros** (10 ou mais), o código pode demorar bastante para rodar, devido ao crescimento fatorial do tempo de execução na função que gera as permutações.

---

### Resumo da Complexidade:

- **`definir_relacoes_possiveis`**: O(1)
- **`gerar_combinacoes`**: O(n²)
- **`gerar_permutacoes_validas`**: O(n²!)
- **`arvore_genealogica`**: O(n²!)

No geral, a complexidade mais impactante é a da função `gerar_permutacoes_validas`, que é O(n²!) no pior caso, tornando este algoritmo pouco eficiente para um grande número de membros.

--- 

## **Responsividade do Código**

### **Relação ao Número de Membros**
A responsividade do código é fortemente afetada pelo número de membros da família inseridos, pois o código tem seções cuja complexidade depende desse fator.

- **Entrada de Dados**:
  O código solicita que o usuário insira nome e idade dos membros da família. Se o número de membros for pequeno (2 ou 3), o código será executado rapidamente, mas à medida que o número de membros cresce, a complexidade aumenta e o tempo de resposta (execução) será afetado.

### **Função `definir_relacoes_possiveis`**

Essa função é "responsiva" no sentido de que ela sempre executa em tempo constante para dois membros, independentemente de quantos membros existam no total. Cada vez que é chamada, verifica uma série de condições para calcular as relações, mas o número de operações é sempre fixo.

- **Complexidade**: O(1)
- **Responsividade**: Muito rápida, pois não depende do número de membros no total, apenas faz comparações entre dois indivíduos.

### **Função `gerar_combinacoes`**

A função `gerar_combinacoes` tem sua execução diretamente proporcional ao número de membros na família, pois gera combinações de pares de pessoas. Isso significa que, à medida que o número de membros aumenta, o número de comparações entre pares cresce quadraticamente.

- **Loop duplo**:
  O primeiro `for` percorre todos os membros, e o segundo `for` compara cada membro com todos os outros membros subsequentes. Esse comportamento gera um aumento significativo no número de operações à medida que o número de membros aumenta.

```python
for i in range(len(membros)):
    for j in range(i + 1, len(membros)):
```

- **Responsividade**: Para pequenas entradas (até 10 membros, por exemplo), o código responderá rapidamente. No entanto, à medida que o número de membros cresce, a função começará a demorar mais, pois para cada membro precisa comparar com todos os outros.

- **Complexidade**: O(n²)

### **Função `gerar_permutacoes_validas`**

A função `gerar_permutacoes_validas` é onde o código se torna potencialmente **menos responsivo** para grandes entradas, pois envolve a geração de permutações de todas as combinações possíveis.

A função é recursiva, e, em termos de tempo de execução, a quantidade de permutações que podem ser geradas cresce de forma **fatorial** com o número de membros. Isso significa que, com apenas alguns membros adicionais, o número de combinações possíveis aumenta drasticamente, afetando a "responsividade" da função.

- **Recursividade**:
  A função chama a si mesma, gerando novas permutações até que todas as pessoas estejam conectadas.

```python
def gerar(permutacao_atual, pessoas_na_permutacao):
    if len(pessoas_na_permutacao) == len(membros):
        permutacoes_possiveis.append(list(permutacao_atual))
        return

    for combinacao in combinacoes:
        pessoa1, pessoa2, relacao = combinacao
        if pessoa1 not in pessoas_na_permutacao or pessoa2 not in pessoas_na_permutacao:
            nova_permutacao = list(permutacao_atual)
            nova_permutacao.append(combinacao)
            novas_pessoas_na_permutacao = set(pessoas_na_permutacao)
            novas_pessoas_na_permutacao.add(pessoa1)
            novas_pessoas_na_permutacao.add(pessoa2)
            gerar(nova_permutacao, novas_pessoas_na_permutacao)
```

- **Complexidade**: O(n²!) no pior caso (fatorial), o que significa que a função se torna muito lenta para grandes entradas.
- **Responsividade**: Para entradas pequenas, o código pode ser razoavelmente rápido, mas, à medida que o número de combinações aumenta, ele se torna significativamente mais lento, afetando a experiência do usuário.

### **Entrada do Usuário na Função `arvore_genealogica`**

Essa função coleta dados do usuário, o que é um ponto onde a responsividade depende diretamente da interação humana. Ela solicita nomes e idades e espera por respostas.

- **Responsividade**: Instantânea para receber entrada, mas o tempo de execução geral será afetado pelo número de membros que o usuário inserir.

### **Impacto da Responsividade no Tempo de Execução (Big O)**

- **Definir relações possíveis (`definir_relacoes_possiveis`)**: O(1)
- **Gerar combinações (`gerar_combinacoes`)**: O(n²)
- **Gerar permutações válidas (`gerar_permutacoes_validas`)**: O(n²!)

A principal função a afetar a responsividade é `gerar_permutacoes_validas`, cujo tempo de execução cresce de forma fatorial. Isso significa que, para uma pequena lista de membros, o código funciona eficientemente, mas à medida que o número de membros cresce, a performance degrada significativamente.

### Resumo Detalhado da Responsividade

- **Entrada do usuário**: Imediata, depende do tempo que o usuário leva para inserir os dados.
- **Definir relações (`definir_relacoes_possiveis`)**: Tempo constante, sempre rápido.
- **Gerar combinações (`gerar_combinacoes`)**: Cresce quadraticamente, tornando-se mais lento para entradas grandes.
- **Gerar permutações (`gerar_permutacoes_validas`)**: Crescimento fatorial, a principal área onde a responsividade é comprometida para entradas grandes.
  
Assim, a responsividade do código, em termos de tempo de execução, é boa para entradas pequenas, mas se torna lenta para entradas grandes devido à natureza combinatória e recursiva do problema.
