# Jogo da Vida

Projeto em Python que implementa o **Jogo da Vida de Conway**, um autômato celular baseado em uma matriz binária.

O programa recebe uma matriz quadrada inicial, aplica as regras do jogo a cada geração e imprime no terminal a evolução das células vivas e mortas.

## Tecnologias Utilizadas

* Python 3.11
* Docker

## Estrutura do Projeto

```text
jogo-da-vida/
├── Dockerfile
├── entradas.txt
├── jogo-da-vida.py
├── README.md
└── .gitignore
```

## Regras do Jogo da Vida

Cada posição da matriz representa uma célula.

Os valores possíveis são:

```text
1 = célula viva
0 = célula morta
```

A cada nova geração, o programa analisa os vizinhos de cada célula.

Cada célula pode ter até 8 vizinhos:

* acima
* abaixo
* esquerda
* direita
* diagonais

As regras aplicadas são:

1. Uma célula viva com 2 ou 3 vizinhos vivos permanece viva.
2. Uma célula viva com menos de 2 vizinhos vivos morre por solidão.
3. Uma célula viva com mais de 3 vizinhos vivos morre por superpopulação.
4. Uma célula morta com exatamente 3 vizinhos vivos se torna viva.
5. Nos demais casos, a célula permanece morta.

## Funcionamento do Programa

O arquivo principal é:

```text
jogo-da-vida.py
```

O programa executa os seguintes passos:

1. Lê o tamanho da matriz quadrada.
2. Lê a quantidade de gerações que serão simuladas.
3. Lê a matriz binária inicial.
4. Imprime a geração inicial.
5. Calcula e imprime cada geração seguinte.

## Arquivo de Entrada

O arquivo `entradas.txt` é usado para executar o programa sem precisar digitar os dados manualmente no terminal.

Exemplo usado no projeto:

```text
3
5
1 1 1
1 1 1
1 1 0
```

Neste exemplo:

* `3` define uma matriz `3x3`
* `5` define que serão simuladas 5 gerações
* As próximas 3 linhas representam a matriz inicial

Matriz inicial:

```text
1 1 1
1 1 1
1 1 0
```

## Execução Local com Python

Para executar diretamente no terminal usando o arquivo `entradas.txt`:

```bash
python jogo-da-vida.py < entradas.txt
```

Também é possível executar manualmente:

```bash
python jogo-da-vida.py
```

Nesse caso, o programa solicitará os dados nesta ordem:

```text
Tamanho da matriz:
Quantidade de gerações:
Digite a matriz binária:
```

## Execução com Docker

Este projeto usa apenas um script Python. Portanto, **não é necessário usar Docker Compose**.

Docker Compose seria útil em projetos com múltiplos serviços, como aplicação web, banco de dados, cache, filas etc. Para este projeto, Docker normal é suficiente.

## Dockerfile

O projeto utiliza o seguinte `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /jogo-da-vida

COPY . .

CMD ["sh", "-c", "python jogo-da-vida.py < entradas.txt"]
```

### Explicação do Dockerfile

```dockerfile
FROM python:3.11-slim
```

Define a imagem base com Python 3.11 em uma versão reduzida.

```dockerfile
WORKDIR /jogo-da-vida
```

Define o diretório de trabalho dentro do container.

```dockerfile
COPY . .
```

Copia todos os arquivos do projeto para dentro da imagem Docker.

```dockerfile
CMD ["sh", "-c", "python jogo-da-vida.py < entradas.txt"]
```

Executa o programa Python usando o arquivo `entradas.txt` como entrada padrão.

## Como Gerar a Imagem Docker

Na raiz do projeto, execute:

```bash
docker build -t jogo-da-vida .
```

Esse comando cria uma imagem Docker chamada:

```text
jogo-da-vida
```

## Como Rodar o Projeto com Docker

Depois de gerar a imagem, execute:

```bash
docker run --rm jogo-da-vida
```

O container executará o programa automaticamente usando o arquivo `entradas.txt`.

A flag `--rm` remove o container após a execução, evitando acúmulo de containers parados.


## Comandos Úteis

Gerar imagem Docker:

```bash
docker build -t jogo-da-vida .
```

Executar container:

```bash
docker run --rm jogo-da-vida
```

Executar Python localmente com o arquivo de entrada:

```bash
python jogo-da-vida.py < entradas.txt
```

Entrar no container para depuração:

```bash
docker run --rm -it --entrypoint sh jogo-da-vida
```

Dentro do container, é possível verificar os arquivos com:

```bash
ls -la
cat entradas.txt
python jogo-da-vida.py < entradas.txt
```

## Resultado Esperado

Ao executar o projeto, o programa imprime a matriz inicial como `Geração 0` e depois imprime cada nova geração até atingir a quantidade configurada no arquivo `entradas.txt`.

Exemplo de saída inicial:

```text
Tamanho da matriz: Quantidade de gerações: Digite a matriz binária:
Geração 0:
1 1 1
1 1 1
1 1 0
```

Em seguida, o programa imprime as próximas gerações calculadas pelas regras do Jogo da Vida.
