vet_peso = [26, 22, 4, 18, 13, 9]
vet_preco = [64, 85, 52, 99, 39, 54]
vet_atual = []
matriz_resultado = []
itens = 6
# capacidade + 1 por conta do zero inicial
capacidade = 27
degrau = 0
vet_capac_pessoa = [23, 20, 20, 26]


def montaMatriz(capacidade, vet_peso, vet_atual, vet_preco, degrau, itens):
    
    for a in range(0, capacidade):
        vet_atual.append(0)
    matriz_resultado.append(vet_atual)

    for k in sorted(vet_peso):
        vet_atual = []
        degrau += 1
        for i in range(0, capacidade):
            if (k <= i):
                posPeso = vet_peso.index(k)
                valorCorr = vet_preco[posPeso]
                aux = i - k
                valorSoma = valorCorr + matriz_resultado[degrau-1][aux]
                if (valorSoma < matriz_resultado[degrau - 1][i]):
                    vet_atual.append(matriz_resultado[degrau - 1][i])
                else:
                    vet_atual.append(valorSoma)
            else:
                if (matriz_resultado[degrau - 1][i] != 0):
                    vet_atual.append(matriz_resultado[degrau - 1][i])
                else:
                    vet_atual.append(0)
        matriz_resultado.append(vet_atual)
    return matriz_resultado



# imprime(matriz_resultado)

# Faz a soma da família

matriz_resultado =  montaMatriz(capacidade, vet_peso, vet_atual, vet_preco, degrau, itens)

def calculaCapacidadeFamilia(matriz_resultado, vet_capac_pessoa):
    linha = []
    capacidade_familia = 0
    linha = matriz_resultado[len(matriz_resultado)-1]
    for capacidade in vet_capac_pessoa:
        capacidade_familia += linha[capacidade]

    return capacidade_familia

def imprime(matriz_resultado):
    linha = []
    for i in range(0, capacidade):
        print("", i, end=",")
    print()
    for linha in matriz_resultado:
        print(linha)

print(calculaCapacidadeFamilia(matriz_resultado, vet_capac_pessoa))
