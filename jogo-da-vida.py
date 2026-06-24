# Define uma função que recebe a matriz atual e calcula a próxima geração
def proxima_geracao(matriz):

    # Pega o tamanho da matriz
    # Como a matriz é quadrada, n vale para linhas e colunas
    n = len(matriz)

    # Cria uma nova matriz n x n preenchida com zero
    # Essa matriz vai guardar o próximo estado
    nova = [[0 for _ in range(n)] for _ in range(n)]

    # Percorre cada linha da matriz
    for i in range(n):

        # Percorre cada coluna da matriz
        for j in range(n):

            # Conta quantos vizinhos vivos existem ao redor da célula atual
            vivos = 0

            # Percorre as linhas vizinhas: linha acima, linha atual e linha abaixo
            for x in range(i - 1, i + 2):

                # Percorre as colunas vizinhas: esquerda, atual e direita
                for y in range(j - 1, j + 2):

                    # Ignora a própria célula, porque ela não conta como vizinha
                    if x == i and y == j:
                        continue

                    # Verifica se a posição do vizinho está dentro da matriz
                    # Evita acessar posições inválidas, como -1 ou maior que n
                    if 0 <= x < n and 0 <= y < n:

                        # Soma o valor do vizinho
                        # Se for 1, soma um vivo
                        # Se for 0, não altera a contagem
                        vivos += matriz[x][y]

            # Verifica se a célula atual está viva
            if matriz[i][j] == 1:

                # Se a célula viva tiver 2 ou 3 vizinhos vivos, continua viva
                if vivos == 2 or vivos == 3:
                    nova[i][j] = 1

                # Se tiver menos de 2 ou mais de 3, ela morre
                # Não precisa colocar else, porque nova já começa com 0

            # Caso contrário, a célula atual está morta
            else:

                # Se a célula morta tiver exatamente 3 vizinhos vivos, ela nasce
                if vivos == 3:
                    nova[i][j] = 1

    # Retorna a nova matriz calculada
    return nova


# Define uma função para imprimir a matriz na tela
def imprimir_matriz(matriz):

    # Percorre cada linha da matriz
    for linha in matriz:

        # Imprime os valores da linha separados por espaço
        print(*linha)


# Define uma função que executa a simulação por várias gerações
def simular(matriz, geracoes):

    # A matriz atual começa sendo a matriz digitada pelo usuário
    atual = matriz

    # Mostra que essa é a geração inicial
    print("Geração 0:")

    # Imprime a matriz inicial
    imprimir_matriz(atual)

    # Pula uma linha para organizar a saída
    print()

    # Repete o processo da geração 1 até a geração desejada
    for g in range(1, geracoes + 1):

        # Calcula a próxima geração a partir da matriz atual
        atual = proxima_geracao(atual)

        # Mostra qual geração está sendo impressa
        print(f"Geração {g}:")

        # Imprime a matriz dessa geração
        imprimir_matriz(atual)

        # Pula uma linha para separar as gerações
        print()


# Lê o tamanho da matriz quadrada
# Exemplo: se digitar 3, a matriz será 3x3
n = int(input("Tamanho da matriz: "))

# Lê a quantidade de gerações que serão simuladas
geracoes = int(input("Quantidade de gerações: "))

# Cria uma lista vazia para guardar a matriz
matriz = []

# Mostra uma mensagem antes de o usuário digitar a matriz
print("Digite a matriz binária:")

# Repete n vezes, porque a matriz tem n linhas
for _ in range(n):

    # Lê uma linha digitada pelo usuário
    # split() separa os números por espaço
    # map(int, ...) converte cada valor para inteiro
    # list(...) transforma tudo em uma lista
    linha = list(map(int, input().split()))

    # Adiciona a linha digitada dentro da matriz
    matriz.append(linha)

# Chama a função que executa a simulação
simular(matriz, geracoes)