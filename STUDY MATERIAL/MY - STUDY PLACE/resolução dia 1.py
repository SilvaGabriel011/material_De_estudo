#aaa
#define todas as letras do alfabeto dentro do array, pra ser usado dentro das funções
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# #define todas as funções
# def encrypt(text, shift):
#     new_text = ''
#     for letter in text:
#         if letter in alphabet:
#             position = alphabet.index(letter)
#             new_position = (position + shift) % 26
#             new_text += alphabet[new_position]
#         else:
#             new_text += letter
#     return new_text

# def decrypt(text, shift):
#     tru_text = ''
#     for letter in text:
#         if letter in alphabet:
#             position = alphabet.index(letter)
#             new_position = (position - shift) % 26
#             tru_text += alphabet[new_position]
#         else:
#             tru_text += letter
#     return tru_text

# def ceasar (direction, text, shift):
#     if direction == 'encode':
#         return encrypt(text, shift)
#     elif direction == 'decode':
#         return decrypt(text, shift)
#     else:
#         print("typo, try again")


# #define status para parar repetição
# should_continue = True

# #monta a estrutura de repetição
# while should_continue:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
    
#     result = ceasar(direction, text, shift)
#     print(f'The direction{direction}d text is: {result}')
    
#     again = input('wanna go again? ')
#     if again != 'y':
#         should_continue = False
#         print('bye')













# leilao_status = True
# dicionario_de_valores ={}
# while leilao_status:
    
#     decisao = input("Alguem quer fazer um lance? digite 's' para SIM e 'n' para NAO\n").lower().strip()
#     if decisao == "s":
#         nome = input("Digite o nome do bidder: ")
#         valor = input("digite o valor do bidder: ")
        
#         for key in dicionario_de_valores:
#             key += nome
#         for nome in dicionario_de_valores:
#         print('\n'*100)
#     else:
#         leilao_status = False


# decisao = input("Alguem quer fazer um lance? digite 's' para SIM e 'n' para NAO\n").lower().strip()
# if decisao == "s":
#     nome = input("Digite o nome do bidder: ")
#     valor = input("digite o valor do bidder: ")




####### PARA CONSEGUIR LOOPAR DENTRO DE UM DICIONARIO NA PARTE DOS VALORES E NAO DAS CHAVES::::::
# def find_highest_bidder(bidding_dicitionary):
#     highets_bid = 0
#     for bidder in bidding_dicitionary:
#         bid_amount = bidding_dicitionary[bidder]
#         if bid_amount > highets_bid:
#             highets_bid = bid_amount
#             winner = bidder



# def is_leap_year(year):
#     # Write your code here. 
#     # Don't change the function name.
#     first_decision = year % 4 
#     if first_decision == 0:
        
#     else:
#         return False


# #LEAP YEAR CHALLENGE
# boleano = 1989 % 4
# boleano1 = 1989 % 100 # 4 * 25
# boleano2 = 1989 % 400 # 4 * 25 * 4 
# print(boleano, boleano1, boleano2)



# def add(n1, n2):
#     return n1 + n2

# def sub(n1, n2):
#     return n1 - n2

# def mult(n1, n2):
#     return n1 * n2

# def div(n1, n2):
#     return n1 / n2

# operacoes = {
#     "+": add,
#     "-": sub,
#     "*": mult,
#     "/": div,
# }

# def ler_numero(msg):
#     while True:
#         try:
#             return float(input(msg))
#         except ValueError:
#             print("Por favor, digite um número válido.")

# def ler_operador():
#     operador = input("Digite o operador (*, +, -, /): ").strip()
#     while operador not in operacoes:
#         print("Operador inválido. Use apenas '*', '+', '-', '/'")
#         operador = input("Digite o operador correto: ").strip()
#     return operador

# # Início da calculadora
# print("Bem-vindo à calculadora!")

# resultado_atual = None
# usar_resultado_anterior = False

# while True:
#     if not usar_resultado_anterior:
#         numero1 = ler_numero("Digite o primeiro número: ")
#     else:
#         numero1 = resultado_atual
#         print(f"\nUsando resultado anterior: {numero1}")

#     numero2 = ler_numero("Digite o segundo número: ")
#     operador = ler_operador()

#     if operador == '/' and numero2 == 0:
#         print("Divisão por zero não é permitida.")
#         continue

#     resultado_atual = operacoes[operador](numero1, numero2)
#     print(f"Resultado: {resultado_atual}")

#     continuar = input("\nVocê quer continuar com o resultado atual? (s/n): ").lower().strip()
#     if continuar == 's':
#         usar_resultado_anterior = True
#     else:
#         nova_operacao = input("Deseja iniciar uma nova operação? (s/n): ").lower().strip()
#         if nova_operacao != 's':
#             print("Encerrando a calculadora.")
#             break
#         else:
#             usar_resultado_anterior = False



# def somar_array(lista):
#     return sum(lista)

# # # Adiciona cartas
# cartas_pegas_dealer =  teste(arrio)
# cartas_pegas_jogador = teste(arrio)
# # # Soma apenas os valores já existentes
# # print("Cartas selecionadas:", cartas_selecionadas)
# # print("Soma total:", somar_array(cartas_selecionadas))

# # print (arrio[0])

# print(somar_array(cartas_pegas_dealer))
# print(somar_array(cartas_pegas_jogador))


# def vencedor(mao1,mao2):
#     """"tem como função retornar quem ganhou a partida"""
#     maoo1=sum(mao1)
#     maoo2=sum(mao2)
#     vencedor =''
#     #se mao1 for maior q 21 estoura automaticamente, mao2 ganha
#     if maoo1 > 21:
#         vencedor = maoo2
#         return (f'o vencedor foi: mao1 com {maoo2} pontos totais e {mao2} pontos de cada carta')
#     #se mao2 for maior q 21 estoura automaticamente, mao1 ganha
#     elif maoo2 > 21:
#         vencedor = maoo1
#         return (f'o vencedor foi: mao1 com {maoo1} pontos totais e {mao1} pontos de cada carta')

#     #casos que precisa comparar mão à mão

#     elif maoo1 > maoo2:
#         vencedor = maoo1
#         return (f'o vencedor foi: mao1 com {maoo1} pontos totais e {mao1} pontos de cada carta')
#     elif maoo2 > maoo1:
#         vencedor = maoo2
#         return (f'o vencedor foi: mao1 com {maoo2} pontos totais e {mao2} pontos de cada carta')
#     elif maoo1 == maoo2:
#         vencedor = 'empate'
#         return vencedor
        


# ### PODERIA CRIAR UM DICIONARIO COM AS SITUAÇÕES ? 
# ### SWITCH CASE É MELHOR DO QUE ESSE TANDO DE IF ELSE? 

# maozona1=[1,2,3,1]
# maozona2=[1,2,3]

# print(vencedor(maozona1,maozona2))


# ###### função que adiciona a carta a mais que o usuario pediu ao array de cartas do usuario






# def teste(arraeio):
#     carta_escolhida1 = random.choice(arraeio)
#     carta_escolhida2 = random.choice(arraeio)
#     cartas_selecionadas.append(carta_escolhida1)
#     cartas_selecionadas.append(carta_escolhida2)
#     return cartas_selecionadas

# print(teste(arrio))
# algo = teste(arrio)


# print(algo[0])


# mao_do_pc = [2,3,4]
# def decisao_computador(mao,baralho):
#     total = sum(mao)
#     # print(total)
#     while total < 17:
#         mao.append(pede_carta(baralho))
#         total = sum(mao)
#         # print(total)
#     return mao,total
# impressao = decisao_computador(mao_do_pc,arrio)
# print(impressao)

# import random

# arrio = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# cartas_selecionadas = []

# def pede_carta(deq):
#     carta = random.choice(deq)
#     return carta


# arreio_de_cartas = [1,2,3]
# def carta_ao_array_de_cartas(maiscartas,baralho):
#     print(f"suas cartas são: {arreio_de_cartas}, somando {sum(arreio_de_cartas)}") # mostra o que ta antes de começar a iteração do jogo 
#     status_pedido = True # status que eu preciso pra conseguir sair do while
#     while status_pedido == True:
#         maiscartas = input("voce quer mais cartas?\n") #tomada de decisão no começo 
#         if maiscartas == 'y':
#             carta_pedida = pede_carta(baralho) #usa a função de pegar uma carta aleatoria do baralho pra dentro de uma variavel
#             arreio_de_cartas.append(carta_pedida) #adiciona a nova carta puxada ao arreio 
#             total_de_pontos = sum(arreio_de_cartas) #faz a somatoria dos pontos pra mostrar qual a nova pontuação agora com a nova carta adicionada ao deck
#             print(f"suas cartas atuais são: {arreio_de_cartas}, totalizando em {total_de_pontos}")
#             if total_de_pontos > 21: # se a somatoria das cartas bater mais do que 21 o jogador perde automaticamente
#                 return(f"\njogador perdeu, estourou com um total de {total_de_pontos}\ne com as cartas: {arreio_de_cartas}")
#                 # POSSO ADICIONAR UMA CONTAGEM PRAS CARTAS DO COMPUTADOR PRA MOSTRAR COM QUANTOS POTNOS O PC VENCEU 
#                 # break
#                 ## ja declara como perdedor
#             else:
#                 continue # ENQUANTO NAO FOR MAIS DO QUE 21 PONTOS O JOGO CONTINUA NO LOOP DE PERGUNTAR SE QUER MAIS CARTAS OU NÃO
#                 # print(arreio_de_cartas, total_de_pontos)
#             # status_pedido = False
#         elif maiscartas != 'y' and maiscartas != 'n': #SE O JOGADOR DIGITA ALGO DIFERENTE DE Y OU N, ELE VOLTA PRO INPUT, PERMITINDO TYPO'S 
#             print("typo, try again, JUST 'n' or 'y' ")
#         else: #SE O JOGADOR NAO QUER MAIS CARTAS, RETORNA A SOMATÓRIA DAS CARTAS E ENCERRA O LOOP,
#             #POSSO TENTAR AQUI TBM PEGAR O ARREIO DAS CARTAS... 
#             # APESAR DE QUE COM A SOMATORIA EU JA CONSIGO FAZER O JOGO FUNCIONAR 
#             mao = sum(arreio_de_cartas)
#             return mao


# testando = carta_ao_array_de_cartas(input,arrio)
# print(testando)


# import random

# baralho = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# # Função que retorna uma carta aleatória do baralho
# def escolhe_carta(baralho):
#     return random.choice(baralho)

# # Distribui duas cartas iniciais para jogador e computador
# def distribui_cartas(baralho):
#     return [escolhe_carta(baralho), escolhe_carta(baralho)]

# # Decide vencedor comparando mãos do jogador e computador
# def escolhe_vencedor(mao_jogador, mao_computador):
#     pontos_jogador = sum(mao_jogador)
#     pontos_computador = sum(mao_computador)

#     if pontos_jogador > 21:
#         return "Computador venceu! Jogador estourou!"
#     if pontos_computador > 21:
#         return "Jogador venceu! Computador estourou!"

#     if pontos_jogador > pontos_computador:
#         return "Jogador venceu!"
#     elif pontos_jogador < pontos_computador:
#         return "Computador venceu!"
#     else:
#         return "Empate!"

# # Computador pede cartas até ter pelo menos 17 pontos
# def computador_joga(mao_computador, baralho):
#     while sum(mao_computador) < 17:
#         mao_computador.append(escolhe_carta(baralho))
#     return mao_computador

# # Jogador escolhe pedir cartas ou parar
# def jogador_joga(mao_jogador, baralho):
#     while True:
#         print(f"Suas cartas: {mao_jogador}, total: {sum(mao_jogador)}")
#         if sum(mao_jogador) > 21:
#             print("Você estourou!")
#             break
#         decisao = input("Quer mais cartas? ('y' ou 'n'):").lower()
#         if decisao == 'y':
#             mao_jogador.append(escolhe_carta(baralho))
#         elif decisao == 'n':
#             break
#         else:
#             print("Digite apenas 'y' ou 'n'.")
#     return mao_jogador

# # Fluxo principal do jogo
# def jogo():
#     while True:
#         iniciar = input("Quer jogar Blackjack? ('y' ou 'n'): ").lower()
#         if iniciar == 'n':
#             print("Até a próxima!")
#             break
#         elif iniciar != 'y':
#             print("Digite apenas 'y' ou 'n'.")
#             continue

#         mao_jogador = distribui_cartas(baralho)
#         mao_computador = distribui_cartas(baralho)

#         print(f"Sua mão inicial: {mao_jogador} - total {sum(mao_jogador)}")
#         print(f"Carta inicial do computador: {mao_computador[0]}")

#         mao_jogador = jogador_joga(mao_jogador, baralho)
#         if sum(mao_jogador) <= 21:
#             mao_computador = computador_joga(mao_computador, baralho)

#         print(f"\nResultado:")
#         print(f"Sua mão final: {mao_jogador} - total {sum(mao_jogador)}")
#         print(f"Mão final do computador: {mao_computador} - total {sum(mao_computador)}")

#         resultado = escolhe_vencedor(mao_jogador, mao_computador)
#         print(resultado)

# # Inicia o jogo
# jogo()

# import random

# baralho = [1,2,3,4,5,6,7,8,9,10,10,10,11]

# def escolhe_carta_aleatoria(baralho):
#     """Escolhe uma carta aleatória do baralho"""
#     return random.choice(baralho)

# def seleciona_duas_Cartas_aleatorias(baralho):
#     """Gera as duas primeiras cartas de uma mão"""
#     return [escolhe_carta_aleatoria(baralho), escolhe_carta_aleatoria(baralho)]

# def decisao_computador(mao, baralho):
#     """O computador continua pedindo cartas até ter pelo menos 17 pontos"""
#     while sum(mao) < 17:
#         mao.append(escolhe_carta_aleatoria(baralho))
#     return mao

# def nova_Carta_adicionada_enquanto_jogador_pede(mao, baralho):
#     """Adiciona cartas à mão do jogador enquanto ele quiser e não estourar"""
#     while True:
#         print(f"Suas cartas: {mao} - total: {sum(mao)}")
#         if sum(mao) > 21:
#             print("Você estourou!")
#             return mao
#         decisao = input("Você quer uma nova carta? (y/n): ").lower()
#         if decisao == "y":
#             mao.append(escolhe_carta_aleatoria(baralho))
#         elif decisao == "n":
#             return mao
#         else:
#             print("Entrada inválida. Digite apenas 'y' ou 'n'.")

# def ver_quem_ganhou(mao_pc, mao_jg):
#     """Compara as mãos e declara o vencedor"""
#     mao_jg1 = sum(mao_jg)
#     mao_pc1 = sum(mao_pc)

#     if mao_jg1 > 21:
#         return "Computador ganhou! Jogador estourou os pontos."
#     elif mao_pc1 > 21:
#         return "Jogador ganhou! Computador estourou os pontos."
#     elif mao_pc1 > mao_jg1:
#         return f"Computador venceu com {mao_pc1} pontos. Mão: {mao_pc}"
#     elif mao_jg1 > mao_pc1:
#         return f"Jogador venceu com {mao_jg1} pontos. Mão: {mao_jg}"
#     else:
#         return f"Empate! Jogador: {mao_jg1} | Computador: {mao_pc1}"

# def jogo(baralho):
#     while True:
#         jogar = input("Você quer jogar 21? (y/n): ").lower().strip()
#         if jogar == 'y':
#             mao_jogador = seleciona_duas_Cartas_aleatorias(baralho)
#             mao_computador = seleciona_duas_Cartas_aleatorias(baralho)

#             print(f"JOGADOR: {mao_jogador} - total: {sum(mao_jogador)}")
#             print(f"COMPUTADOR: [{mao_computador[0]}, ?]")

#             mao_jogador = nova_Carta_adicionada_enquanto_jogador_pede(mao_jogador, baralho)
#             mao_computador = decisao_computador(mao_computador, baralho)

#             print("\nFinal das cartas:")
#             print(f"JOGADOR: {mao_jogador} - total: {sum(mao_jogador)}")
#             print(f"COMPUTADOR: {mao_computador} - total: {sum(mao_computador)}")

#             print(ver_quem_ganhou(mao_computador, mao_jogador))
#         elif jogar == 'n':
#             print("Ok, até logo!")
#             break
#         else:
#             print("Entrada inválida. Digite apenas 'y' ou 'n'.")

# jogo(baralho)




# def is_prime(valor):
#     if valor == 1: 
#         return False
#     if valor == 2:
#         return True

#     valores = []
#     for i in range(2,valor):
#         valores.append(i)
        
#     for number in valores:
#         if valor % number == 0:
#             return False
#     return True

# print(is_prime(73))
# print(is_prime(75))

# import random 

# def escolha_dificuldade ():
#     """"fazer o jogador determinar qual a o numero de vidas que vai ter no jogo"""
#     while True:
#         choice = input("Escolha dificuldade, entre:\nFacil ou Dificil\n").lower().strip()
#         if choice == 'facil':
#             return 10
#         elif choice == "dificil":
#             return 5
#         elif choice != 'facil' and choice != "dificil":
#             print("Voce tentou uma opção invalida, digite novamente")
#             print('\n')



# def lista_numeros():
#     '''''poderia ser random.randint(1,100)
#         mas fiquei feliz de pensar na ideia de construir uma lista com os numeros e nao digitar um a um 
#         ta bom mas da pra melhorar'''
#     lista = []
#     for i in range(1,101):
#         lista.append(i)
#     return lista

# def jogador_joga(vidas,numero):
#     """""logica do jogo
#         acredito que fazer uma função pra isso ajuda, nao sei ao certo o porque, mas ajuda
#         """
#     chute = 0 
#     while chute != numero and vidas > 0:
#         chute = int(input("Make a guess:   \n"))
#         if numero < chute:
#             print(f"too high\n guess again\n")
#             vidas -= 1
#             print(F"voce tem **{vidas}** tentativas restantes ")
#             continue
#         elif numero > chute:
#             print(f"too low\n guess again\n")
#             vidas -= 1
#             print(F"voce tem **{vidas}** tentativas restantes ")
#             continue
#         elif numero == chute:
#             print(f"voce acertou, a resposta era: {chute}")
#             break
#     print(f"as suas vidas acabaram, resposta era: {numero}")
            
# def jogo_funciona():
#     print("bem vind ao jogo de advinhar o numero que o computador escolheu entre 1 e 100\n**se voce escolher facil voce tem 10 chances\n**se voce escolher dificil voce tem 5")
#     lista_numeros()
#     numero_escolhido = int(random.choice(lista_numeros()))
#     #numero_escolhido = random.randint(1,100)
#     escolha_jogador = escolha_dificuldade()
#     jogador_joga(escolha_jogador,numero_escolhido)

# jogo_funciona()


# def bug_function():
#     for i in range(1,21):
#         # i += 1
#         if i == 20:
#             print("you got it ")

# bug_function()

# from random import randint

# dice_images = ['1','2','3','4','5','6']
# dice_num = randint(1,6)
# print(dice_images[dice_num])

# """"" bug ta acontecendo pq o teto do randint 6, nao equivale ao endereço no ultimo termo dentro da lista
#         portanto quando chega ao ultimo endereço da lista nao encontra termo nenhum, assim gerando o bug
#             como fazer isso sempre acontecer? ::: dice_num = 6
#             como consertar: 5 substitui 6 ou randint
#                             0 susbtitui o 1
#                             (len[array])"""


# import maths
# import random

# def mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint(1,3)
#         new_item = maths.add(new_item,item)
#     b_list.append(new_item)
#     print(b_list)

# test_list = [1,2,3,5,8,13]

# mutate(test_list)

# def odd_or_even(number):
#     if number % 2 == 0:
#         return "This is an even number."
#     else:
#         return "This is an odd number."

# Target is the number up to which we count
# def fizz_buzz(target):
#     final_number = target + 1
#     for number in range(1,final_number):
#         if number % 3 == 0 and number % 5 == 0:
#             print("FizzBuzz")
#         elif number % 3 == 0:
#             print("Fizz")
#         elif number % 5 == 0:
#             print("Buzz")
#         else:
#             print([number])

# fizz_buzz(15)

