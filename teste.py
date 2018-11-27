


vet_peso = [17,23,4,3,21,33]
vet_preco = [64,85,52,99,39,54]
vet_atual = []
matriz_resultado = []
itens = 3
vet_capac_pessoa = [23,20,20,26]

#vet_peso = [17,23,24]
#vet_preco = [72,44,31]
#itens = 3
# capacidade + 1 por conta do zero inicial
capacidade = 26 + 1
degrau = 0
#vet_capac_pessoa = [26]


def montaMatriz(capacidade, vet_peso, vet_atual, vet_preco, degrau):
    
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

# Faz a soma da família

matriz_resultado =  montaMatriz(capacidade, vet_peso, vet_atual, vet_preco, degrau)

def calculaCapacidadeFamilia(matriz_resultado, vet_capac_pessoa):
    linha = []
    capacidade_familia = 0
    linha = matriz_resultado[len(matriz_resultado)-1]
    #print(linha)
    for capacity in vet_capac_pessoa:
        #print(capacity, vet_capac_pessoa)
        capacidade_familia += linha[capacity]

    return capacidade_familia

def imprime(matriz_resultado):
    linha = []
    for i in range(0, capacidade):
        print("", i, end=",")
    print()
    for linha in matriz_resultado:
        print(linha)

print(calculaCapacidadeFamilia(matriz_resultado, vet_capac_pessoa))
#imprime(matriz_resultado)