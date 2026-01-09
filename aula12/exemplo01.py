import pandas as pd

produtos = ['Notebook', 'Smartphone', 'Tablet', 'Smartwatch', 'Câmera', 'Notebook']
qtds_estoque = [16, 28, 19, 13, 26, 9]

serie_produtos = pd.Series(produtos)
serie_quantidade = pd.Series(qtds_estoque)
# print(serie_quantidade)
# print(serie_produtos)
# #para printar como lista, com ordem

# #printando pelo rótulo
# print(serie_produtos[1])
# print(serie_produtos[1], serie_produtos[2])

# #printando pelos dois rótulos
# print(serie_produtos[[1, 2]])

# # #Só valores, sem a posições
# print(serie_produtos [[2,5]].values)

#filtrando elementos
# print(serie_quantidade[serie_quantidade < 20]) #mostra os menores que 20
# print(serie_produtos[serie_produtos == 'Notebook']) #mostra somente notebooks
# print(serie_produtos[serie_produtos.str.startswith('Smart')]) #filtra as palavras que iniciam com Smart
# print(serie_produtos[serie_produtos.str.endswith('phone')]) #filtra as palavras que iniciam com Smart
# print(serie_produtos[serie_produtos.str.contains('t')]) #filtra as palavras que iniciam com Smart

#Operações:
# serie_quantidade = serie_quantidade + 10 #Somar 10 em todos os números da lista
# print(serie_quantidade)
# serie_quantidade[serie_quantidade > 30] += 25
# print(serie_quantidade)

# #Multiplicação entre séries
# preco = [3000, 800, 2500, 600, 1990, 850]
# total = serie_quantidade * preco
# print(total)

serie_estoque = pd.Series(qtds_estoque, index=produtos)
print(serie_estoque)
# print(serie_estoque['Notebook'])
# print(serie_estoque[['Notebook', 'Tablet']])
# print(serie_estoque[['Notebook', 'Tablet']].values)
# print(serie_estoque[serie_estoque < 20]) #filtrar pela quantidade
# print(serie_estoque[serie_estoque.index.str.startswith('Smart')]) #filtrar pelo nome

# serie_estoque += 5
# print(serie_estoque)

# serie_estoque.loc['Headphone'] = None #Acrescentando um novo produto na lista
# print(serie_estoque)

preco = pd.Series([3000, 800, 2500, 600, 1990, 850], index=produtos)

serie_total_produtos = serie_estoque * preco
print(serie_total_produtos)