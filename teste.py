import os
os.system('cls') or None
V = ["A", "B", "C", "D", "E"]
matriz = [[2,1,0,1,0],
          [1,0,1,1,0],
          [0,1,0,2,0],
          [1,1,2,0,1],
          [0,0,0,1,0]]
ordem = (len(V))
grau = []   
tamanho = 0
print("A ordem do Grafo é", ordem) # Ordem é o número de vértices

vertice1 = V.index(input("Digite o primeiro vértice: ").upper())
vertice2 = V.index(input("Digite o segundo vértice: ").upper())

for i in range(ordem):  #percorre a linha da matriz
    grau.append(0)  # Adiciona um espaço novo no vetor 
    for j in range(ordem):  # percorre a coluna da matriz
        grau[i] = grau[i] + matriz[i][j]    # soma o valor da matriz no local atual ao vetor atual que está com o valor 0
        tamanho = tamanho + matriz[i][j]    # Soma os valores de cada local da matriz
    print("Grau do vetor", V[i],"é" , grau[i]) #Grau é a somatória de todos os números de um vértice
print("O tamanho do grafo é", tamanho/2) # tamanho é a soma de todos os números de uma matriz divido por 2

maior = 0
menor = 0

for i in range(ordem):
    if grau[i]>grau[maior]:
        maior = i

    if grau[i]<grau[menor]:
        menor = i
print("O vertice com menor Grau é ", V[menor])
print("O vertice com maior Grau é ", V[maior])

if matriz[vertice1][vertice2] > 0:
    print(V[vertice1],"e" , V[vertice2], "são vizinhos")
else:
    print(V[vertice1],"e" , V[vertice2], "não são vizinhos")