
peso = [2,4,1,5]
vet_preco = [14,23,56,34]
matriz_resultado = []
vet_zero = []
itens = 6
capacidade = 3


for i in range(0,capacidade):
    vet_zero.append(0);
matriz_resultado.append(vet_zero)

for i in range(0,capacidade):
    for j in range(1,itens):
        a = matriz_resultado[j-1][i]
        
        if (peso[j] > i):
            b = 0
        else:
            b = matriz_resultado[j-1][i-peso[j]] + vet_preco[j]
            if (a > b):
                matriz_resultado[j][i] = a
            else:
                matriz_resultado[j][i] = b



print(matriz_resultado)