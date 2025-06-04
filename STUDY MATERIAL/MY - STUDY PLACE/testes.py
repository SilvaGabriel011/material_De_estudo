# #aa


# # alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



# # # print(alphabet.index('a'))



# # number = alphabet.index('a')
# # new_number = number + 2

# # print(alphabet[new_number])

# # alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# # def encrypt(text, shift):
# #     new_text = ''
# #     for letter in text:
# #         if letter in alphabet:
# #             position = alphabet.index(letter)
# #             new_position = (position + shift) % 26
# #             new_text += alphabet[new_position]
# #         else:
# #             new_text += letter
# #     return new_text

# # def decrypt(text, shift):
# #     tru_text = ''
# #     for letter in text:
# #         if letter in alphabet:
# #             position = alphabet.index(letter)
# #             new_position = (position - shift) % 26
# #             tru_text += alphabet[new_position]
# #         else:
# #             tru_text += letter
# #     return tru_text

# # def caesar(direction, text, shift):
# #     if direction == 'encode':
# #         return encrypt(text, shift)
# #     elif direction == 'decode':
# #         return decrypt(text, shift)
# #     else:
# #         return "Typo, try again."

# # # Main program loop
# # should_continue = True
# # while should_continue:
# #     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# #     text = input("Type your message:\n").lower()
# #     shift = int(input("Type the shift number:\n"))

# #     result = caesar(direction, text, shift)
# #     print(f"The {direction}d text is: {result}")

# #     again = input("Wanna go again? Type 'y' for yes or 'n' for no:\n").lower()
# #     if again != 'y':
# #         should_continue = False
# #         print("Goodbye!")



# # student_scores = {
# #     'Harry': 88,
# #     'Ron': 78,
# #     'Hermione': 95,
# #     'Draco': 75,
# #     'Neville': 60
# # }

# # def transform_into_grades(dicionario):
# #     # #dicionario de grades 
# #     # possible_grades= {
# #     #     '91 - 100':'outstanding', '81 - 90': 'Exceeds Expectations',
# #     #     '71 - 80': 'Acceptable', '70 or lower': 'Fail',
# #     #     }
    
# #     #acho q tem que loopar entre os dois dicionarios... 
    
# #     for key in dicionario:
# #         if dicionario[key] > 91:
# #             dicionario[key] == 'outstanding'
# #         elif 81 < dicionario[key] < 90:
# #             dicionario[key] == 'Exceeds Expectations'
# #         elif 71 < dicionario[key] < 80:
# #             dicionario[key] == 'Acceptable'
# #         elif dicionario[key] < 70:
# #             dicionario[key] == 'Fail'
# #     return dicionario

# # print(transform_into_grades(student_scores))



# # student_grades = 



# # dicionario = {
# #     'Outstanding': 91, 'Exceeds Expectations': 90,
# #     'Acceptable': 80, 'Fail': 70
# #     }

# # teste = dicionario['Outstanding'] > 91

# # print(teste)


# # student_scores = {
# #     'Harry': 88,
# #     'Ron': 78,
# #     'Hermione': 95,
# #     'Draco': 75,
# #     'Neville': 60
# # }

# # dicionario_notas = {
# #     'Outstanding': 91, 'Exceeds Expectations': 90,
# #     'Acceptable': 80, 'Fail': 70
# #     }

# # # def analisador_de_notas(a,b):
# # #     if a[key] == b[key]:
# # #         return True
# # #     else:
# # #         return False

# # # print(analisador_de_notas(student_scores, dicionario_notas))


# # # print(student_scores['Harry'])
# # def exchange(amor):
# #     for key in amor:
# #         if 91 < amor[key]:
# #             # O VALOR DA CHAVE AGORA É 'OUTSTANDING'
# #             amor[key] = 'Outstanding'
# #         elif 81 < amor[key] < 90:
# #             amor[key] = 'Exceeds Expectations'
# #         elif 71 < amor[key] < 80:
# #             amor[key] = 'Acceptable'
# #         elif amor[key] < 70:
# #             amor[key] = 'Fail'
# #         else:
# #             print('typo')
# #     return amor

# # print(exchange(student_scores))


# # travel_log = {
# #     'France':{
# #         'cities_visited': ['paris', 'lille', 'dijon'],
# #         'total_visits' : 8
# #         },
# #     'germany': {
# #         'cities_visited': ['stuttgart', 'berlin','stutgart'],
# #         'total_visits': 10             
# #         }
# # }


# # print(travel_log['germany']['cities_visited'][2])


# # lsit = travel_log['France']
# # requerido = lsit[1]

# # print(requerido)
# # print(travel_log['France'][1])  

# # nested_list = [1,2,[4,5]]

# # print(nested_list[2][1])

# # nesting_test = {}

# # nesting_test['andar'] = 10000
# # nesting_test['correr'] = 1
# # print(nesting_test)
# # print(nesting_test['andar']>nesting_test['correr'])
# # print(nesting_test)
# # nome = input("digite nome: ")
# # valor = input("digite um valor: ")
# # nesting_test[nome]= valor
# # # nesting_test[1] = valor
# # nome2 = input("digite nome: ")
# # valor2 = input("digite um valor: ")
# # nesting_test[nome2]=valor2
# # print(nesting_test)
# # # print(nesting_test)
# # # print(nesting_test[nome]>nesting_test[nome2])



# # for key in nesting_test:
# #     nesting_test[key] = '1 ' + key
# #     print(key, nesting_test[key])


# # nesting_names_values = {}
# # leilao_status = True
# # while leilao_status:
    
# #     decisao = input("voce quer dar um lance? digite 's' para SIM e 'n' para não\n").strip().lower()
# #     maior = 0
# #     ganhador = ''
# #     if decisao == 's':
# #         nome= input("qual seu nome? ")
# #         lance = int(input("qual seu lance? "))
# #         print('\n' * 1000)
# #         nesting_names_values[nome] = lance
# #     elif decisao != 's' or 'n' or 'sim' or 'não' or 'nao':
# #         print('erro de digitação? tente novamente....')
# #     else:
# #         maior = max(nesting_names_values.values())

# #         for nome in nesting_names_values:
# #             if nesting_names_values[nome] == maior:
# #                 ganhador = nome
# #         # ganhador = nesting_names_values[maior]
# #         print(f'o maior valor é de: {maior} e o vencedor é {ganhador}')
# #         leilao_status = False
# #         # print(nesting_names_values)






# # #LEAP YEAR CHALLENGE
# # year = int(input("coloque um ano: "))


# # def verifica_leap(ano):
# #     if ano % 4 == 0:
# #         if ano % 100 == 0:
# #             if ano % 400 == 0:
# #                 return True
# #             else:
# #                 return False
# #         else:
# #             return True
# #     else:
# #         return False

# # print(verifica_leap(year))



# # def add(n1,n2):
# #     """soma dos argumentos/parametros

# #     Args:
# #         n1 (int): number
# #         n2 (int): number

# #     Returns:
# #         number = n3 + n4
# #     """
# #     return n1 + n2
# # def sub(n3,n4):
# #     """_subtração dos argumentos/parametros

# #     Args:
# #         n3 (int): number
# #         n4 (int): number

# #     Returns:
# #         number: n3 - n4
# #     """
# #     return n3 - n4
# # def mult(n5,n6):
# #     """multiplicação dos argumentos/parametros

# #     Args:
# #         n5 (int): numero
# #         n6 (int): numero

# #     Returns:
# #     number: n5 * n6
# #     """
# #     return n5 * n6
# # def div(n7,n8):
# #     """divisao dos argumentos/parametros

# #     Args:
# #         n7 (_type_): _description_
# #         n8 (_type_): _description_

# #     Returns:
# #         _type_: _description_
# #     """
# #     return n7/n8

# # # soma = add
# # # subtracao = sub
# # # multplicar = mult
# # # dividir = div

# # dicionario_de_operações = {
# #     "+": add,
# #     "-": sub,
# #     "*": mult,
# #     "/": div,
# #     }


# # status_calculator = True

# # while status_calculator: 
# #     decisao_1= input("Voce quer fazer uma operação? se sim 's' se nao 'n':\n").lower().strip()
# #     if decisao_1 == 's':
# #         numero1 = int(input("qual o primeiro numero que voce vai usar: "))
# #         numero2 = int(input('qual o segundo número: '))
# #         operacao = str(input("qual operador: use '*' para mulplicação\n '+' para soma\n '-' para subtração\n '/' para divisão:\n OBS: USE APENAS O SIMBOLO, ex: *\n")).strip()
# #         if operacao not in dicionario_de_operações:
# #             while operacao not in dicionario_de_operações:
# #                 print("digite apenas, * , + , - , /")
# #                 operacao = input("digite agora o sinal correto:\n")
# #         if operacao == '/' and numero2 == 0:
# #             while operacao == '/' and numero2 == 0:
# #                 print('divisão por 0, não suportada')
# #                 # numero1 = int(input("qual o primeiro numero que voce vai usar: "))
# #                 numero2 = int(input('qual o segundo número: '))
# #                 operacao = str(input("qual operador: use '*' para mulplicação\n '+' para soma\n '-' para subtração\n '/' para divisão:\n OBS: USE APENAS O SIMBOLO, ex: *\n")).strip()
# #             resultado = (dicionario_de_operações[operacao](numero1,numero2))
# #             # continue
# #         else:
# #             resultado = (dicionario_de_operações[operacao](numero1,numero2))
# #         print(f'{numero1} {operacao} {numero2} = {resultado}')
# #         status_provisorio = True
# #         while status_provisorio:        
# #             decisao_2 = input(f"voce quer continuar com o valor {resultado}, para alguma outra operação? SE SIM DIGITE 'S' se não digite 'n':\n").lower()
# #             if decisao_2 == 's':
# #                 numero3 = int(input('qual o segundo número:\n'))
# #                 operacao = str(input("qual operador: use '*' para mulplicação\n '+' para soma\n '-' para subtração\n '/' para divisão:\n OBS: USE APENAS O SIMBOLO, ex: *\n")).strip()
# #                 resultado1 = (dicionario_de_operações[operacao](resultado,numero3))
# #                 print(f'\n{resultado} {operacao} {numero3} = {resultado1}')
# #             else:
# #                 status_provisorio = False
# #                 continue
# #     else:
# #         print("Encerrando calculadora")
# #         status_calculator = False


# # import random
# # cartas_possiveis = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# # cartas_selecionadas = []
# # game_status = True 
# # par_cartas_aleatorias = []

# # def escolhe_carta_dentro_do_baralho(baralho):
# #     """" função tem que retornar de forma ALEATORIA uma carta do baralho
# #         sendo que o baralho é um array """
# #     carta_escolhida = random.choice(baralho)
# #     cartas_selecionadas.append(carta_escolhida)
# #     return cartas_selecionadas

# # def soma_valores_de_cartas(bar):
# #     """soma os valores de cartas que foram selecionadas,
# #         loop dentro do array de cartas selecionadas"""
# #     return sum(bar)

# # def escolhe_2_cartas_dentro_do_baralho(baralho):
# #     """" ao incio do jogo retorna as duas primeiras cartas
# #         posso, jogar isso dentro de dois arrays
# #         um para um dealer, que so mostra o primeiro termo
# #         outro array pro jogador, que consegue ver as duas primeiras cartas sorteadas
# #         """
# #     carta_escolhida1 = random.choice(baralho)
# #     carta_escolhida2 = random.choice(baralho)
# #     par_cartas_aleatorias.append(carta_escolhida1)
# #     par_cartas_aleatorias.append(carta_escolhida2)
# #     return par_cartas_aleatorias

# # def escolhe_vencedor_ou_empate(mao1,mao2):
# #     """"compara os valores da soma das cartas com intuito de declarar quem venceu
# #     pode tambem declarar que houve empate
# #     """
# #     """"tem como função retornar quem ganhou a partida"""
# #     maoo1=sum(mao1)
# #     maoo2=sum(mao2)
# #     vencedor =''
    
# #     #se mao1 for maior q 21 estoura automaticamente, mao2 ganha
# #     if maoo1 > 21:
# #         return vencedor == mao2
# #         # return (f'o vencedor foi: mao2 com {maoo2} pontos totais e {mao2} pontos de cada carta')

# #     #se mao2 for maior q 21 estoura automaticamente, mao1 ganha
# #     elif maoo2 > 21:
# #         return vencedor == mao1
# #         # return (f'o vencedor foi: mao1 com {maoo1} pontos totais e {mao1} pontos de cada carta')

# #     #casos que precisa comparar mão à mão

# #     elif maoo1 > maoo2:
# #         return vencedor == maoo1
# #         # return (f'o vencedor foi: mao1 com {maoo1} pontos totais e {mao1} pontos de cada carta')
# #     elif maoo2 > maoo1:
# #         return vencedor == maoo2
# #         # return (f'o vencedor foi: mao2 com {maoo2} pontos totais e {mao2} pontos de cada carta')
# #     elif maoo1 == maoo2:
# #         vencedor == 'empate'
# #         return vencedor

# # def decisao_do_computador(mao,baralho):
# #     """tem como função fazer com que o computador
# #     decida se vai querer mais cartas ou não
# #     ENQUANTO O VALOR TOTAL DAS CARTAS FOR MENOR QUE 17 PEDE UMA CARTA"""
# #     total = sum(mao)
# #     while total < 17:
# #         mao.append(escolhe_carta_dentro_do_baralho(baralho))
# #         total = soma_valores_de_cartas(mao)
# #     return {total:mao}

# # def adicionar_carta_ao_pool_de_cartas(baralho,mao,decisao):
# #     """tem como função adicionar a carta que o jogador
# #     solicitou ao seu deck de cartas
# #     SE CARTA A MAIS FOR PEDIDA ADICONE AO ARRAY DE CARTAS"""
# #     # print(f"suas cartas são: {mao} ")
# #     status_pedido = True
# #     while status_pedido:
# #         decision = input("Do you want more cards? type 'y' for yes and 'n' for no:\n").lower()
# #         if decisao == "y":
# #             carta_pedida = escolhe_carta_dentro_do_baralho(baralho)
# #             mao.append(carta_pedida)
# #             total_de_pontos=sum(mao)
# #             print(f"suas cartas atuais são: {mao}, totalizando em {total_de_pontos}")
# #             if total_de_pontos > 21:
# #                 return(f"\njogador perdeu, estourou com um total de {total_de_pontos}\ne com as cartas: {mao}")
# #             else:
# #                 continue
# #         elif decision != 'y' and decision != 'n':
# #             print("typo, just 'n' or 'y'")
# #         else:
# #             return {total_de_pontos:mao}

# # # mao_jogador = []
# # # mao_computador = []
# # while game_status == True:
# #     decision =input("Do you wanna play some blak jack (21), Put 'y' for YES and 'n' for nyo:\n").lower()
# #     if decision == 'y':
# #         mao_jogador = escolhe_2_cartas_dentro_do_baralho(cartas_possiveis)
# #         mao_computador = escolhe_carta_dentro_do_baralho(cartas_possiveis)
# #         print(f"your cards:{mao_jogador}, current score: {sum(mao_jogador)}")
# #         print(f"computer's first card: {mao_computador}")
# #         decision = input(f"Do you want more cards? ")
# #         if decision == 'y':
# #             adicionar_carta_ao_pool_de_cartas(cartas_possiveis,mao_jogador,decision)
# #     elif decision != 'y' and decision != 'n' :
# #         print("typo, try again... 'y' or 'n'")    
# #         continue
# #     elif decision == 'n':
# #         print('thats fine, see you later!')
# #         game_status = False


# ################REFAZENDO O JACK BLACK 21
# # import random

# # baralho = [1,2,3,4,5,6,7,8,9,10,10,10,11]

# # def escolhe_carta_aleatoria(baralho):
# #     """" escolhe uma carta aleatoria do baralho
# #     retorna a carta
# #     """
# #     carta = random.choice(baralho)
# #     return carta
# # def seleciona_duas_Cartas_aleatorias(baralho):
# #     """"gera as 2 primeiras cartas que o jogador se baseia pra decidir se pede mais
# #     alem disso
# #     separa as duas primeiras cartas do pc tambem
# #     retorna mao
# #     """
# #     mao = []
# #     novacarta1 = escolhe_carta_aleatoria(baralho)
# #     novacarta2 = escolhe_carta_aleatoria(baralho)
# #     mao.append(novacarta1)
# #     mao.append(novacarta2)
# #     return mao
# # def decisao_computador(mao,baralho):
# #     """"enquanto o computador nao atinge 17 pontos ele pede mais uma carta,
# #     esse carta é adicionada ao arreio de cartas do computador
# #     parametros: baralho(todas as cartas possiveis)
# #                 mao(pra conseguir ja computar as duas cartas que sao geradas no inicio do jogo)
    
# #     """
# #     while sum(mao) < 17:
# #         outra_carta = escolhe_carta_aleatoria(baralho)
# #         mao.append(outra_carta)
# #     return mao
# # def nova_Carta_adicionada_enquanto_jogador_pede(mao,baralho):
# #     """"tem como função adicionar uma nova carta caso o jogador queira
# #     caso ruim:
# #     caso a somatoria das cartas de acima de 21, sai da iteração e retorna as cartas
# #     caso normal:
# #     retorna o array de cartas que compoem a mao do jogador    
# #     """
# #     # print(f"suas cartas são: {mao} e voce tem o total de pontos: {sum(mao)}")
# #     while True:
# #         nova_carta = escolhe_carta_aleatoria(baralho)
# #         mao.append(nova_carta)
# #         if sum(mao) > 21:
# #             return mao
# #         print(f"your cards are {mao} and the total amount of points are {sum(mao)}")
# #         decisao = input("do u want a new card? y/n\n").lower()
# #         if decisao == "y":
# #             continue
# #         elif decisao != "y" and decisao != "n":
# #             print("typo, just Y and N, no capital needed")
# #         else:
# #             return mao
# # def ver_quem_ganhou(mao_pc, mao_jg):
# #     """"ver quem ganhou a partir do retorno das outras fx, que retornam os arreios de cartas 
# #     seja do pc
# #     seja do jogador
    
# #     retorna:
# #         pc vencedor
# #         jogador vencedor
# #         empate
# #         """
# #     mao_jg1 = sum(mao_jg)
# #     mao_pc1 = sum(mao_pc)
    
# #     if mao_jg1 > 21:
# #         return (f"computador ganhou, jogador estourou os pontos COM TOTAL DE {mao_jg1} e a mao de {mao_jg}")
# #     elif mao_pc1 > 21:
# #         return (f"jogador ganhou, computador estourou os pontos COM TOTAL DE {mao_pc1} e a mao de {mao_pc}")
# #     elif mao_pc1 > mao_jg1:
# #         return (f"o vencedor foi o computador com {mao_pc1} pontos e {mao_pc} de cartas")
# #     elif mao_jg1 > mao_pc1:
# #         return (f"o vencedor foi o jogador com {mao_jg1} pontos e {mao_jg} de cartas")
# #     else:
# #         return (f"EMPATE Jogador com:{mao_jg1} points\nE PC com: {mao_pc1} points ")

# # def jogo(baralho):
# #     while True:
# #         jogar = input("voce quer jogar 21? y/n\n").lower().strip()
# #         if jogar == 'y':
# #             mao_jogador = seleciona_duas_Cartas_aleatorias(baralho)
# #             mao_computador = seleciona_duas_Cartas_aleatorias(baralho)
# #             print(f"o JOGADOR tem {mao_jogador} de cartas e {sum(mao_jogador)} de pontos")
# #             print(f"o COMPUTADOR tem {mao_computador[0]} de carta e {sum(mao_computador)} de pontos")
# #             decisao2 = input("voce quer uma nova carta? y/n\n").lower().strip()
# #             if decisao2 == "y":
# #                 nova_Carta_adicionada_enquanto_jogador_pede(mao_jogador,baralho)
# #                 decisao_computador(mao_computador,baralho)
# #                 print(ver_quem_ganhou(mao_computador,mao_jogador))
# #             elif decisao2 != 'y' and decisao2 != 'n':
# #                 print('typo, just y or n')
# #             else:
# #                 print(ver_quem_ganhou(mao_computador,mao_jogador))
# #         elif jogar == 'n':
# #             print("ok,bye")
# #             break

# # jogo(baralho)







# # def funcao1(parametro):
# #     def funcao2(parametro2):
# #         return parametro * parametro2


# # def is_prime(valor):
# #     if valor == 1:
# #         return False
# #     elif valor == 2:
# #         return True
    
    
# #     elif valor % valor == 0 and valor % 1 == 0:
# #         return True
# #     else:
# #         return False
    
# # print(is_prime(75))

# # import random 


# # def lista_numeros():
# #     lista = []
# #     for i in range(1,101):
# #         lista.append(i)
# #     return lista

# # # print(lista_numeros())

# # numero_escolhido = random.choice(lista_numeros())
# # print(numero_escolhido)

# import dados_externos
# import random

# # print(dados_externos.famous_data[1])
# # print(dados_externos.famous_data[1])


# # def acessar_item_aleatorio_da_lista(lista):
# #     return lista[random.randint(0,len(lista) + 1)]

# # print(acessar_item_aleatorio_da_lista(dados_externos.famous_data))


# # def numero_de_seguidores(dicionario):


# #TESTANDO COISAS DE DICIONARIO

# # DICIONARIO = {'asa':"PRIMEIRO", 'baca':"SEGUNDO", 'xaca':"TERCEIRO"}

# # print(DICIONARIO)

# # print(DICIONARIO(0))


# # lista = [1,2,3,4,5]

# # for i in lista:
# #     print (i)

# # d = [
# #     {
# #     "nome": "Alice",
# #     "idade": 30,
# #     "pais": "BR"
# # },
# #     {    "nome": "Aitana",
# #     "idade": 27,
# #     "pais": "ESP"},
# #         {
# #         'name': 'Instagram',
# #         'follower_count': 346,
# #         'description': 'Social media platform',
# #         'country': 'United States'
# #     },
# # ]


# # def pegar_dic_aleatorio_na_lista_de_dicionarios(lista):
# #     return lista[random.randint(0,len(lista)-1)]

# # DICIONARIO = pegar_dic_aleatorio_na_lista_de_dicionarios(d)


# # def pegar_dvalor_numerico_dentro_do_dicionario(dic):
# #     for chave,valor in dic.items():
# #         if isinstance(valor,int):
# #             return valor

# # print(pegar_dvalor_numerico_dentro_do_dicionario(DICIONARIO))

# # def retorna_Valores_no_dicionario_Se_valor_for_inteiro(dicionario):
# #     for value in dicionario.values():
# #         if isinstance(value,int):
# #             return value

# # def compare_value(value1,value2):
# #     if value1 > value2:
# #         return value1
# #     else: 
# #         return value2

# # def enquanto_jogador_acerta():
# #     contador = 0
# #     while True:
# #         if 


# # for i in d:
# #     print(i)


# # for i in d:
# #     for _ in d.values():
# #         print(_)

# # for chave,valor in d.items():
# #     if isinstance(valor,int):
# #         print(valor)
# # def valor_dentro_de_dicionario(dic):
# #     for chave,valor in dic.items():
# #         if isinstance(valor,int):
# #             return valor

# # print(valor_dentro_de_dicionario(d))


# d = [
#     {
#         'name': 'Messi',
#         'follower_count': 890,
#         'description': 'footblall player',
#         'country': 'Argentina'
#     },
#     {
#         'name': 'Loud',
#         'follower_count': 36,
#         'description': 'e-sports team',
#         'country': 'Brasil'
#     },
#         {
#         'name': 'Instagram',
#         'follower_count': 346,
#         'description': 'Social media platform',
#         'country': 'United States'
#     },
# ]

# def pegar_dic_aleatorio_na_lista_de_dicionarios(lista):
#     return lista[random.randint(0,len(lista)-1)]

# DICIONARIO = pegar_dic_aleatorio_na_lista_de_dicionarios(d)

# def pegar_dvalor_numerico_dentro_do_dicionario(dic):
#     for valor in dic.values():
#         if isinstance(valor,int):
#             return valor

# def apresenta_opções(op1,op2):
#     print("quem voce acha que tem mais seguidores?\n")
#     print(f"OPÇÃO A: {op1}\nOPÇÃO B: {op2}\n")

# def quem_e_maior(op1,op2):
#     if op1 > op2:
#         return op1
#     else:
#         return op2

# tesste1 = pegar_dvalor_numerico_dentro_do_dicionario(DICIONARIO)

# def jogo_joga(dicionario):
#     while game_Status == True:
#         contador = 0
        
#         op1 = pegar_dic_aleatorio_na_lista_de_dicionarios(dicionario)
#         op2 = pegar_dic_aleatorio_na_lista_de_dicionarios(dicionario)

#         print("quem voce acha que tem mais seguidores?\n")
#         print(f"OPÇÃO A: {op1}\nOPÇÃO B: {op2}\n")

#         while True:
#             choice = input("digite apenas a ou b:").lower()
#             if choice != 'a' and choice != 'b':
#                 print("digitee apenas a ou b\n")
#             else:
#                 if choice == 'a':
#                     choice = op1
#                 else:
#                     choice = op2
#                 break

#         ganahdor = quem_e_maior(op1,op2)
#         if choice == ganahdor:
#             contador +=1 
#         else:
#             print(f"voce pontuou: {contador} mas perdeu na verdade quem era {ganahdor}")
#             game_Status = False
#             break


# # def jogador_escolhe_se_joga(dicionario):
# #     choice = input("voce quer jogar? Y/N\n").lower()
# #     while True:
# #         if choice == 'y':
# #             jogo(dicionario)
# #         elif choice != 'y' and 'n':
# #             print("apenas y ou n")
# #             continue
# #         else:
# #             print("ok, obrigado")

# import random
# import dados_externos

# DICIONARIO = {
#         'name': 'Messi',
#         'follower_count': 890,
#         'description': 'footblall player',
#         'country': 'Argentina'
#         }

# d = [
#     {
#         'name': 'Messi',
#         'follower_count': 890,
#         'description': 'footblall player',
#         'country': 'Argentina'
#     },
#     {
#         'name': 'Loud',
#         'follower_count': 36,
#         'description': 'e-sports team',
#         'country': 'Brasil'
#     },
#         {
#         'name': 'Instagram',
#         'follower_count': 346,
#         'description': 'Social media platform',
#         'country': 'United States'
#     },
# ]


# def saudacao():
#     print("bem vindo ao jogo de maior menor")

# def quer_jogar():
#     while True:
#         choice = input("Voce quer jogar: y/n").lower()
#         if choice == 'y':
#             return True
#         elif choice != 'y' and choice != 'n':
#             print("apenas y ou n")
#             continue
#         else:
#             return False

# def escolhe_dicionario_aleatorio(lista):
#     return lista[random.randint(0,len(lista) - 1)]

# # print(escolhe_dicionario_aleatorio(d))


# def esolhe_valor_dentro_do_dicionario(dicionario):
#     for value in dicionario.values():
#         if isinstance(value,int):
#             return value

# # dicionarioo = (escolhe_dicionario_aleatorio(d))

# # print(esolhe_valor_dentro_do_dicionario(dicionarioo))
# def comparar_valores_De_seguidores(conta1,conta2):
#     if conta1 > conta2:
#         return conta1
#     else:
#         return conta2

# def escolha_do_jogador(dicionario1,dicionario2):
#     escolha = input(f"escolha entre {dicionario1} e {dicionario2}")
#     return escolha

# def imprime_dicionario_sem_valor_de_Seguidres(dicionario):
#     return {
#         key:value 
#         for key, value in dicionario.items()
#         if not isinstance(value,(int,float))
#     }

# # print(imprime_dicionario_sem_valor_de_Seguidres(DICIONARIO))

# def comparar_valores_de_seguidores_definir_maior(valor1,valor2):
#     if valor1 > valor2:
#         return valor1
#     else:
#         return valor2

# def jogador_Esscolhee(dicionario1,dicionario2):
#     choice = input(f"qual personagem tem mais seguidores?: {dicionario1}\nou\n{dicionario2}")
#     if choice == dicionario1:
#         return esolhe_valor_dentro_do_dicionario(dicionario1)
#     else:
#         return esolhe_valor_dentro_do_dicionario(dicionario2)

# def jogador_ganhou(valor_jogador,valor_verdade):
#     if valor_jogador > valor_verdade:
#         return True
#     else:
#         return False

# def jogo_joga(lista_de_dicionarios):
#     game_status = True
#     saudacao()
#     quer_jogar()
#     if quer_jogar == True:
#         while game_status == True:
#             dic1 = escolhe_dicionario_aleatorio(lista_de_dicionarios)
#             dic2 = escolhe_dicionario_aleatorio(lista_de_dicionarios)
#             valor1 = esolhe_valor_dentro_do_dicionario(dic1)
#             valor2 = esolhe_valor_dentro_do_dicionario(dic2)
#             valor_verdade = comparar_valores_de_seguidores_definir_maior(valor1,valor2)
#             dicionario_sem_valor_numerico1 = imprime_dicionario_sem_valor_de_Seguidres(dic1)
#             dicionario_sem_valor_numerico2 = imprime_dicionario_sem_valor_de_Seguidres(dic2)
#             choice = input(f"quem voce acha que tem mais seguidores:\nA:{dicionario_sem_valor_numerico1}\nou\nB:{dicionario_sem_valor_numerico2}")
#             if choice == 'a':
#                 valor_jogador = dic1
#             else:
#                 valor_jogador = dic2
#             jogador_ganhou(valor_jogador,valor_verdade)
#             if valor_verdade == True:
#                 continue
#             else:
#                 game_status = False
#                 break
#     else:
#         print('tchau')

# jogo_joga(dados_externos.famous_data)


# arquivo jogo.py

# import random

# DADOS = [
#     {"name": "A", "followers": 10},
#     {"name": "B", "followers": 20},
# ]

# # ----- STUBS -------------------------------------------------
# def sortear_perfil(lista):
#     """Stub: devolve sempre o primeiro item (por enquanto)."""
#     return lista[0]

# def extrair_numero(perfil):
#     """Stub: devolve 0 para não quebrar cálculo."""
#     return 0

# def formatar_perfil(perfil):
#     """Stub: devolve string fixa."""
#     return "<perfil>"

# # -------------------------------------------------------------

# def main():
#     perf_a = sortear_perfil(DADOS)
#     perf_b = sortear_perfil(DADOS)
#     print("A:", formatar_perfil(perf_a))
#     print("B:", formatar_perfil(perf_b))
#     num_a = extrair_numero(perf_a)
#     num_b = extrair_numero(perf_b)
#     print("Soma provisória:", num_a + num_b)

# if __name__ == "__main__":
#     main()



import random
import dados_externos


DICIONARIO = {
        'name': 'Messi',
        'follower_count': 890,
        'description': 'footblall player',
        'country': 'Argentina'
        }

d = [
    {
        'name': 'Messi',
        'follower_count': 890,
        'description': 'footblall player',
        'country': 'Argentina'
    },
    {
        'name': 'Loud',
        'follower_count': 36,
        'description': 'e-sports team',
        'country': 'Brasil'
    },
        {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
]


#### AREA DE PROCESSAMENTO INTERNO ###########

#1 PEGAR UM DICIONARIO DA LISTA DE DICIONARIOS - ALEATORIAMENTE
def dic_from_list_random(lista):
    return random.choice(lista)

# print(dic_from_list_random(d))

#2 pegar apenas o par chave valor que contem uma chave com valor tipo numerico:

def key_number_type(dicionario):
    for key in dicionario.values():
        if isinstance(key,(float,int)):
            return key

# print(key_number_type(dic_from_list_random(d)))













# def saudacao():
#     return "BEM VINDO AO JOGO DE MAIOR OU MENOR"

# def despedida():
#     return 'obrigado por tentar a saida errada'

# def jogo():
    


# def quer_jogar():
#     while True:
#         jogador_quer = input("voce quer jogar: N/Y").lower().strip()
#         if jogador_quer == 'y':
#             jogo()
#         elif jogador_quer == 'n':
#             despedida()
#         else:
#             print("apenas y ou n")