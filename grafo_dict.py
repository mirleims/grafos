#!/usr/bin/env python
# coding: utf-8

# In[23]:


# GRAFO --> G(V,E)
# V representas os vértices
# E representa as arestas
"""
Dado o número de arestas de um grafo e suas arestas em listas
o código retorna o grafo em forma de dicionário e uma lista com
os vértices pais


Exemplo:

        1
       / \
      2   3
     / \   \
    5   6   4
    
    
     
    Entradas:  
        número de arestas: 5
        arestas: [1 3][1 2][2 5][2 6][3 4]
        
    Saídas:
        grafo: {1: [3, 2], 2: [5, 6], 3: [4]}
        

"""


arestas=[]
n_arestas = int(input('Digite o número de arestas:'))
i=1

while(i<=n_arestas):
    V1,V2 = input("Digite a aresta: ").split(" ")
    V1=int(V1)
    V2=int(V2)
    i+=1
    arestas.append([V1,V2])

    
temp= arestas[0][0]
vertices_pais=[temp]
for i in arestas:
    if(i[0]!= temp):
        vertices_pais.append(i[0])
        temp=i[0]

grafo ={}
rel=[]
temp=arestas[0][0]
for j in arestas:
    for i  in vertices_pais:
        if(i==j[0] and temp == i):
            rel.append(j[1])
            grafo[i]=rel
        if(i==j[0] and j[0]!=temp):
            temp=i
            rel=[j[1]]
            grafo[i]=rel
print(grafo)

