import csv

# Define as funções para analisar os dados

def contar_pares_impares(lista_numeros):
    pares = 0
    impares = 0
    for num in lista_numeros:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    return (pares, impares)

def contar_primos(lista_numeros):
    primos = []
    for num in lista_numeros:
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                primos.append(num)
    return primos

# Define a função principal que lê o arquivo e realiza as análises

def analisar_dados(arquivo):
    # Define as variáveis para armazenar os padrões e sequências
    padroes_pares_impares = set()
    sequencias = []
    sequencias_repetidas = set()
    primos_repetidos = set()

    # Abre o arquivo e lê os dados
    with open(arquivo, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            # Ignora a linha inicial com as descrições das colunas
            if row[0].startswith('item'):
                continue

            # Extrai os números de cada linha e converte para inteiros
            numeros = [int(num) for num in row[1:]]

            # Analisa a quantidade de números pares e ímpares e adiciona ao conjunto de padrões
            padrao = contar_pares_impares(numeros)
            padroes_pares_impares.add(padrao)

            # Analisa as sequências de números e adiciona à lista
            for i in range(len(numeros)-1):
                if numeros[i]+1 == numeros[i+1]:
                    sequencias.append((numeros[i], numeros[i+1]))
            
            # Analisa a repetição de sequências de números e adiciona ao conjunto de sequências repetidas
            sequencias_unicas = set(sequencias)
            for seq in sequencias_unicas:
                if sequencias.count(seq) > 1:
                    sequencias_repetidas.add(seq)
            
            # Analisa a repetição de números primos e adiciona ao conjunto de primos repetidos
            primos = contar_primos(numeros)
            primos_unicos = set(primos)
            for primo in primos_unicos:
                if primos.count(primo) > 1:
                    primos_repetidos.add(primo)
    
    # Retorna os resultados das análises
    return {
        'padroes_pares_impares': padroes_pares_impares,
        'sequencias': sequencias,
        'sequencias_repetidas': sequencias_repetidas,
        'primos_repetidos': primos_repetidos
    }
