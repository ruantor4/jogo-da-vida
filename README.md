# Simulação do Jogo da Vida

## Descrição

Este projeto implementa uma simulação do **Jogo da Vida (Game of Life)** usando Python.

O programa recebe uma **matriz binária** (0 = célula morta, 1 = célula viva) e calcula sua evolução ao longo de várias gerações seguindo regras simples de sobrevivência e nascimento.

---

## Regras

Para cada célula:

* **Viva (1):**

  * Continua viva se tiver **2 ou 3 vizinhos vivos**
  * Morre se tiver **menos de 2 ou mais de 3 vizinhos vivos**

* **Morta (0):**

  * Nasce se tiver **exatamente 3 vizinhos vivos**

---

## Como executar

1. Execute o arquivo Python:

```bash
python main.py
```

2. Informe:

* Tamanho da matriz
* Quantidade de gerações
* Valores da matriz (0 ou 1)

---

## Exemplo de entrada

```text
Tamanho da matriz: 3
Quantidade de gerações: 2

Digite a matriz binária:
0 1 0
1 1 1
0 0 0
```

## Exemplo de saída

```text
Geração 0:
0 1 0
1 1 1
0 0 0

Geração 1:
1 1 1
1 1 1
0 1 0

Geração 2:
1 0 1
1 0 1
1 1 1
```

---

## Estrutura do código

* `proxima_geracao(matriz)` → Calcula o próximo estado da matriz.
* `imprimir_matriz(matriz)` → Exibe a matriz na tela.
* `simular(matriz, geracoes)` → Executa a simulação por várias gerações.
