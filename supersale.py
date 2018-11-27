import sys


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

def calculaCapacidadeFamilia(matriz_resultado, vet_capac_pessoa):
    linha = []
    capacidade_familia = 0
    linha = matriz_resultado[len(matriz_resultado)-1]

    for capacity in vet_capac_pessoa:
        capacidade_familia += linha[capacity-1]

    return capacidade_familia

def imprime(matriz_resultado):
    linha = []
    for i in range(0, qtd_pessoas):
        print("", i, end=",")
    print()
    for linha in matriz_resultado:
        print(linha)

case = sys.argv[1] #Cases
indice = 2

for caso in range(0,int(case)):
    qtdItens = int(sys.argv[indice])
    indice += 1
    vet_peso = []
    vet_preco = []
    for item in range(0, int(qtdItens)):
        vet_preco.append(int(sys.argv[indice + item]))
        vet_peso.append(int(sys.argv[indice + item + 1]))
        indice += 1

    indice += 1
    qtd_pessoas = int(sys.argv[indice + item])
    indice += item
    vet_capPessoa = []
    for indPessoa in range(0, int(qtd_pessoas)):
        vet_capPessoa.append(int(sys.argv[indice+1]))
        indice += 1

    indice += 1   
    
    matriz_resultado = []
    matriz_resultado =  montaMatriz(max(vet_capPessoa), vet_peso, [], vet_preco, 0)
    print('\n Matriz')
    imprime(matriz_resultado)
    print(calculaCapacidadeFamilia(matriz_resultado, vet_capPessoa))



