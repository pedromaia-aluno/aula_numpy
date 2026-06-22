# Demonstração do Poder do NumPy

Este projeto é um exemplo simples criado para o curso **Python aplicado à análise de dados e aprendizado de máquina**.

O objetivo é mostrar, de forma prática, como o NumPy pode tornar operações numéricas mais simples, diretas e rápidas quando comparado ao uso de listas nativas do Python.

O arquivo `main.py` carrega dados de alunos a partir de um CSV, transforma esses dados em uma matriz NumPy e compara o tempo de execução de uma mesma operação feita de duas formas:

- usando listas comuns do Python;
- usando operações vetorizadas com NumPy.

## Estrutura do Projeto

```text
.
|-- dados.csv
|-- main.py
`-- README.md
```

## Estrutura do CSV

O arquivo `dados.csv` contém informações simples sobre alunos. A primeira linha é o cabeçalho, e as demais linhas representam os registros.

```csv
idade,nota,frequencia%
18,8.5,100
18,9.0,95
16,7.5,70
15,6.7,85
```

As colunas são:

- `idade`: idade do aluno, armazenada como número inteiro.
- `nota`: nota do aluno, armazenada como número decimal.
- `frequencia%`: percentual de frequência do aluno, armazenado como número decimal.

O CSV possui 213 registros de alunos, além da linha de cabeçalho.

## Explicação do `main.py`

### Importação das bibliotecas

```python
import csv
import timeit
import numpy as np
```

Nesta parte, o código importa as bibliotecas necessárias:

- `csv`: usada para ler o arquivo `dados.csv`;
- `timeit`: usada para medir o tempo de execução das operações;
- `numpy`: usada para criar e manipular arrays numéricos de forma eficiente.

O NumPy é importado com o apelido `np`, que é uma convenção muito comum na comunidade Python.

### Carregamento dos dados em uma lista nativa

```python
matrizNativa = []

with open("dados.csv", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)

    for idade, nota, frequencia in leitor:
        matrizNativa.append([
            int(idade),
            float(nota),
            float(frequencia)
        ])
```

Este bloco abre o arquivo CSV e lê seus dados linha por linha.

A função `next(leitor)` pula o cabeçalho do arquivo, pois ele contém apenas os nomes das colunas.

Em seguida, cada linha é convertida para os tipos corretos:

- `idade` vira `int`;
- `nota` vira `float`;
- `frequencia` vira `float`.

Cada registro é adicionado à lista `matrizNativa`, formando uma matriz comum do Python.

### Conversão da lista para NumPy

```python
matrizNumpy = np.array(matrizNativa)
```

Aqui, a lista nativa é convertida para um `ndarray`, que é a estrutura principal do NumPy.

Essa conversão permite realizar operações matemáticas diretamente sobre colunas ou conjuntos inteiros de dados, sem precisar percorrer manualmente cada linha com um `for`.

### Operação usando lista nativa

```python
def operacao_nativa():
    return [linha[1] + 0.5 for linha in matrizNativa if linha[1] <= 9.5]
```

Esta função percorre a lista `matrizNativa` e acessa a posição `1` de cada linha, que corresponde à nota do aluno.

A operação faz duas coisas:

- seleciona apenas notas menores ou iguais a `9.5`;
- soma `0.5` a cada uma dessas notas.

Essa abordagem funciona bem, mas depende de uma repetição linha por linha em Python.

### Operação usando NumPy

```python
def operacao_numpy():
    return matrizNumpy[:, 1][matrizNumpy[:, 1] <= 9.5] + 0.5
```

Esta função realiza a mesma operação, mas usando recursos do NumPy.

A expressão `matrizNumpy[:, 1]` seleciona toda a coluna de notas. Depois, o trecho `matrizNumpy[:, 1] <= 9.5` cria uma máscara booleana para filtrar apenas as notas menores ou iguais a `9.5`.

Por fim, o NumPy soma `0.5` diretamente em todos os valores filtrados.

Essa forma é chamada de operação vetorizada. Em vez de escrever um laço manual, o NumPy aplica a operação sobre vários valores de uma só vez, de maneira mais eficiente.

### Benchmark das operações

```python
tempo_nativo = timeit.timeit(operacao_nativa, number=10000)
tempo_numpy = timeit.timeit(operacao_numpy, number=10000)
```

Este bloco mede quanto tempo cada função leva para executar.

O parâmetro `number=10000` indica que cada operação será executada 10.000 vezes. Isso ajuda a comparar melhor o desempenho das duas abordagens.

### Exibição dos resultados

```python
print(f"Tempo (lista nativa): {tempo_nativo:.6f}s")
print(f"Tempo (NumPy):        {tempo_numpy:.6f}s")
print(f"NumPy foi {tempo_nativo / tempo_numpy:.2f}x mais rápido")
```

No final, o programa imprime:

- o tempo gasto pela operação com lista nativa;
- o tempo gasto pela operação com NumPy;
- quantas vezes o NumPy foi mais rápido nesse teste.

Os valores podem variar de acordo com o computador, mas a ideia principal é mostrar como o NumPy facilita operações numéricas e pode oferecer ganhos de desempenho.

## Como Executar

Instale o NumPy, caso ainda não esteja instalado:

```bash
pip install numpy
```

Depois, execute o arquivo principal:

```bash
python main.py
```

Você verá no terminal uma comparação entre o tempo da operação feita com listas nativas e o tempo da operação feita com NumPy.

## Conceitos Demonstrados

- Leitura de arquivos CSV com Python.
- Conversão de dados para tipos numéricos.
- Criação de arrays com NumPy.
- Seleção de colunas em matrizes.
- Filtros com máscaras booleanas.
- Operações vetorizadas.
- Comparação de desempenho com `timeit`.
