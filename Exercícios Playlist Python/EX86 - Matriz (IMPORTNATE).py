mat = [[0,0,0],[0,0,0],[0,0,0]] #A lista já foi criada com o formato correto. Basta substituir os números

for l in range(0,3): #Para a linha entre 0 e 3
    for c in range(0,3): #e para coluna entre 0 e 3
        mat[l][c] = int(input(f'Digite um número para [{l},{c}] ')) #Ele vai inserir na posição conforme o contador. 
print (mat[0])
print (mat[1])
print (mat[2])

