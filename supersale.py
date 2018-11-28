import sys

def montaMatriz(matriz_resultado,capacidade, vet_peso, vet_atual, vet_preco, degrau):
    
    #Preenche a primeira linha com zero
    for a in range(0, capacidade):
        vet_atual.append(0)
    matriz_resultado.append(vet_atual)
    sorted(vet_peso)
    for k in range(0,len(vet_peso)):
        vet_atual = []
        degrau += 1
   
        for i in range(0, capacidade):
            if (vet_peso[k] <= i):
                valorCorr = vet_preco[k]
                aux = i - vet_peso[k]
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
        capacidade_familia += linha[capacity]
        
    return capacidade_familia


def main():
    var = []
    case = int(input())
     
    for caso in range(0,case):
        qtdItens = int(input())
        vet_peso = []
        vet_preco = []
        for item in range(0, qtdItens):
            pw = input().split(" ")
            vet_preco.append(int(pw[0]))
            vet_peso.append(int(pw[1]))
            
        qtd_pessoas = int(input())
        vet_capPessoa = []
        for indPessoa in range(0, qtd_pessoas):
            vet_capPessoa.append(int(input()))
                    
        matriz_resultado = []
        vet_atual = []
       
        montaMatriz(matriz_resultado, max(vet_capPessoa)+1, vet_peso, vet_atual, vet_preco, 0)
        var.append(calculaCapacidadeFamilia(matriz_resultado, vet_capPessoa))
    
    for a in var:
        print(a)
    print()

if __name__ == '__main__':
	main()