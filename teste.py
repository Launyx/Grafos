import os
os.system('cls') or None
V = ["A", "B", "C", "D", "E"]
matriz = [[2,1,0,1,0],
          [1,0,1,1,0],
          [0,1,0,2,0],
          [1,1,2,0,1],
          [0,0,0,1,0]]


caminho = []
ordem = (len(V))
grau = []   
tamanho = 0
print("A ordem do Grafo é", ordem) # Ordem é o número de vértices

correcao = False

while correcao == False:
    vertice1 = V.index(input("Digite o primeiro vértice: ").upper())    # Obtém um vértice do usuário e coloca em maiúsculo 
    vertice2 = V.index(input("Digite o segundo vértice: ").upper())     # Com esse resultado, pega o indice em que esse vértice está no vetor V[] e o aloca em uma variável

    if vertice1 != vertice2:
        correcao = True
    else:
        print("Erro, digite vértices diferentes")


caminho.append(V[vertice1]) # Coloca o primeiro vértice do caminho da lista caminho

for i in range(ordem):  #percorre as linhas da matriz
    grau.append(0)  # Adiciona um espaço novo no vetor grau 
    for j in range(ordem):  # percorre as colunas da matriz
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

for i in range(ordem):
    if i > vertice1:    # verifica os valores das colunas depois do primeiro vértice
        if matriz[vertice1][i] > 0: # verifica se os valores das colunas da linha do primeiro vértice são maiores que 0 (tem conexão)
            caminho.append(V[i])    # coloca a letra na lista caminho, baseada na coluna do primeiro vértice

caminho.append(V[vertice2]) # coloca o último vértice do caminho no fim da lista caminho

tamanhoCaminho = len(caminho)

if matriz[vertice1][vertice2] > 0:  # Verifica se os vértices dados pelo usuário são vizinhos
    print(V[vertice1],"e" , V[vertice2], "são vizinhos")
else:
    print(V[vertice1],"e" , V[vertice2], "não são vizinhos")
print("Caminho de", V[vertice1], "até", V[vertice2], ": ", end="")
for i in range(tamanhoCaminho):
    print(caminho[i], end=' ')