# def imprime_hello():
#     print('hello world')
# imprime_hello()

# def return_double(a):
#     return (a * 2)
# print(return_double(4))

# def soma(a,b):
#     return a + b

# print(soma(3,41))

# def par_impar(a):
#     if a % 2 == 0:
#         return('numero par')
#     else:
#         return('numero impar')
        
# print(par_impar(4))

# lixta = [ 1, 2 , 3 , 4, 5, 6, 110]

# def retorna_maior(a):
#     maior = 0
#     for n in a:
#         if maior < n:
#             maior = n
#             # print(maior)
#         else:
#             maior = maior
#     print(maior)

# retorna_maior(lixta)

# lixta = ['bela', 'amor', 'casa', 'bebe', 'aus']
# def teste(a):
#     for termo in a:
#         print(f'\n {termo}')
# teste(lixta)

# def imprimir10(anta):
#     while 0 < anta <= 11:
#         print(anta)
#         anta -= 1
#     print(anta)
# imprimir10(10)

# def teste(a):
#     while 0 < a <= 10:
#         print(a)
#         a -= 1

# teste(10)

# def imprimir(a):
#     while 1 <= a <= 5:
#         print(a)
#         a += 1
# imprimir(1)

# def fatorial(a):
#     bara = 1
#     while a > 1:
        
#     #     # a * (a - 1) * ( a - 2 ) * (a - 3) * (a - a)
#     #     # 5  * ( 5 - 1 ) * (5 - 2) * (5 - 3) * (5 - 4) 
#     #     # 20 * (5 - 2) * (5 - 3) * (5 - 4) )
#     #     # 60 * (5 - 3) * (5 - 4) 
#     #     # 120 * (5 - 4) 
#         bara = bara * a
#         print(bara)
#         a -= 1
#         print(a)
#     return bara,a
# print(fatorial(5))

# def soma_lista(a):
#     b = 0
#     for elementos in a:
#         b += elementos
#         # print(b)
#     return b
# lixya = [ 1, 2 ,33, 4, 44 , 5]
# print(soma_lista(lixya))

# def quantos_pares(a):
#     contador = 0
#     for numeros in a:
#         if numeros % 2 == 0:
#             contador += 1
#             print(f'é par {numeros}')
#         else:
#             print(f"nao é par {numeros}")
#     return 'soma de pares = ',contador

# lixya = [ 2, 4 , 6 , 10, 5, 55, 5555, 53]

# print(quantos_pares(lixya))

# def lista_reversa(a):
#     b = -1
#     while b != len(a) :
#         print(a[b])
#         b += 1

# lixya = [ 1,2,3]
# print(lista_reversa(lixya))

# def lista_reversa(a):
#     b = 1  # Começamos do último elemento (-1)
#     while b <= len(a):
#         print(a[-b])  # Índices negativos acessam a lista de trás para frente
#         b += 1

# lixya = [2, 4, 6, 10, 5, 55, 5555, 53]
# lista_reversa(lixya)  # Chamamos a função sem precisar do print


# def numero_lista(a,b):
#     if a in b:
#         print(True)
#     else:
#         print(False)

# lixya = [2, 4, 3]

# print(numero_lista(33,lixya))

# def maiusculas(a):
#     listax = []
#     for termo in a:
#         listax.append(termo.upper())
#     return listax

# lixya = [ 'a','b', 'c', 'd']
# print(maiusculas(lixya))

# def soman(a):
#     n = 1
#     soma = 0
#     while n <= a:
#         soma += n
#         # soma = soma + n
#         n += 1
#         # n = n + 1
#     return soma
# print(soman(3))

# # +=  --> x = x + 1
# # -= --> x = x - 1

