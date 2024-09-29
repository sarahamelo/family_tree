# Função para definir as relações possíveis entre duas pessoas com base nas idades e regras
def definir_relacoes_possiveis(pessoa1, pessoa2):
    nome1, idade1 = pessoa1
    nome2, idade2 = pessoa2
    relacoes = []

    # Pai/mãe e filho: diferença de idade entre 20 e 50 anos
    if idade1 > idade2 and 20 <= (idade1 - idade2) <= 50:
        relacoes.append('pai/mãe')
    elif idade2 > idade1 and 20 <= (idade2 - idade1) <= 50:
        relacoes.append('filho')

    # Irmãos: diferença de idade de até 15 anos e ambos menores de 50 anos
    if abs(idade1 - idade2) <= 15 and idade1 < 50 and idade2 < 50:
        relacoes.append('irmão/irmã')

    # Casal: diferença de idade de até 15 anos e ambos maiores ou iguais a 18 anos
    if abs(idade1 - idade2) <= 15 and idade1 >= 18 and idade2 >= 18:
        relacoes.append('casal')

    # Avô/avó e neto: diferença de idade de pelo menos 50 anos
    if idade1 > idade2 and (idade1 - idade2) >= 50:
        relacoes.append('avô/avó')
    elif idade2 > idade1 and (idade2 - idade1) >= 50:
        relacoes.append('neto')

    # Bisavô/bisavó e bisneto: diferença de idade de pelo menos 80 anos
    if idade1 > idade2 and (idade1 - idade2) >= 80:
        relacoes.append('bisavô/bisavó')
    elif idade2 > idade1 and (idade2 - idade1) >= 80:
        relacoes.append('bisneto')

    return relacoes

# Função para gerar todas as combinações possíveis de relações entre membros
def gerar_combinacoes(membros):
    combinacoes_possiveis = []

    # Percorrer todos os pares de membros para determinar suas relações
    for i in range(len(membros)):
        for j in range(i + 1, len(membros)):
            pessoa1 = membros[i]
            pessoa2 = membros[j]

            # Procurar as possíveis relações entre pessoa1 e pessoa2
            relacoes = definir_relacoes_possiveis(pessoa1, pessoa2)

            for relacao in relacoes:
                combinacoes_possiveis.append([pessoa1[0], pessoa2[0], relacao])

    return combinacoes_possiveis

# Função para gerar permutações que conectem todas as pessoas, sem sobreposição de relações
def gerar_permutacoes_validas(membros, combinacoes):
    permutacoes_possiveis = []

    # Função recursiva para gerar todas as permutações
    def gerar(permutacao_atual, pessoas_na_permutacao):
        # Se todas as pessoas foram conectadas, adicionar permutação à lista
        if len(pessoas_na_permutacao) == len(membros):
            permutacoes_possiveis.append(list(permutacao_atual))
            return

        # Verificar todas as combinações para adicionar novas relações
        for combinacao in combinacoes:
            pessoa1, pessoa2, relacao = combinacao

            # Verificar se podemos adicionar essa combinação à permutação atual
            if pessoa1 not in pessoas_na_permutacao or pessoa2 not in pessoas_na_permutacao:
                nova_permutacao = list(permutacao_atual)
                nova_permutacao.append(combinacao)

                # Atualizar o conjunto de pessoas conectadas
                novas_pessoas_na_permutacao = set(pessoas_na_permutacao)
                novas_pessoas_na_permutacao.add(pessoa1)
                novas_pessoas_na_permutacao.add(pessoa2)

                # Chamada recursiva para gerar mais combinações
                gerar(nova_permutacao, novas_pessoas_na_permutacao)

    # Iniciar com todas as pessoas e sem combinações
    gerar([], set())

    return permutacoes_possiveis

# Função principal para receber a entrada e gerar a árvore genealógica
def arvore_genealogica():
    membros = []
    print("Digite o nome e a idade dos membros da família. Digite 'sair' para finalizar.")
    
    # Receber os membros da família do usuário
    while True:
        nome = input("Nome: ").strip()
        if nome.lower() == 'sair':
            break
        try:
            idade = int(input(f"Idade de {nome}: ").strip())
            if idade <= 0:
                print("A idade deve ser um número positivo.")
                continue
            membros.append((nome, idade))
        except ValueError:
            print("Por favor, insira um número válido para a idade.")

    # Verificar se há pelo menos duas pessoas
    if len(membros) < 2:
        print("É necessário pelo menos duas pessoas para gerar a árvore genealógica.")
        return

    # Gerar todas as combinações possíveis
    combinacoes = gerar_combinacoes(membros)

    # Gerar todas as permutações possíveis que conectem todos os membros
    permutacoes = gerar_permutacoes_validas(membros, combinacoes)
    
    # Exibir as permutações possíveis
    if permutacoes:
        print("\nPermutações possíveis da árvore genealógica:")
        for idx, permutacao in enumerate(permutacoes):
            print(f"Permutação {idx + 1}:")
            for relacao in permutacao:
                print(f"  {relacao[0]} é {relacao[2]} de {relacao[1]}")
            print()
    else:
        print("\nNenhuma permutação possível foi encontrada.")

# Chamar a função principal
arvore_genealogica()
