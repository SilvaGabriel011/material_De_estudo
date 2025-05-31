# for number in range(1,11):
#     print(number)

# def soma(a,b):
#    return print(a + b)
# print(soma(5,3))

# lista = [ 3, 5, 7, 12, 33, 124, 43, 23]
# maximum = 0
# for x in lista:
#     if x > maximum:
#         maximum = x
# print(maximum)
# import random
# numer_escolhido = int(input("digite um valor aleatório: \n"))
# numero_escolhido= random.randint(0, numer_escolhido)
# if numero_escolhido % 2 == 0:
#     print(f'o numero escolhido é par: {numero_escolhido}')
# else:
#     print(f'o numero escolhido é impar: {numero_escolhido}')


# def maior_numero(lixta):
#     maximum = none
#     for x in lixta:
#         if x > maximum:
#             maximum = x
#         elif isinstance(x, str) == True:
#             continue
#     return(maximum)
# def maior_numero(lixta):
#     maximum = None
#     for x in lixta:
#         if isinstance(x,(float,int)):
#             if maximum is None or maximum < x:
#                 maximum = x
#     return maximum

# lista = [ 3, 5, 7, 1142, 33333, 124, 43, 23, 'a']
# print(maior_numero(lista))

# x= 10
# while x >= 1:
#     print(x)
#     x-= 1
#     # print(x)

# import random
# #esolhe uma palavra aleatoria da lista de palavras
# lista_de_palavras = ['controle', 'mouse', 'teclado', 'papel', 'caneta']
# palavra_escolhida = random.choice(lista_de_palavras)
# # print(palavra_escolhida)

# ### transforma a palavra escolhida em sublinhado
# espaço_em_branco = ''
# for letra in palavra_escolhida:
#     espaço_em_branco += "_"
# print(palavra_escolhida)
# print(espaço_em_branco)


# letra_escolhida_pelo_usuario = ''
# mostrar_ao_usuario_aonde_ele_está = ''
# completou_a_palavra = False
# vidas_no_jogo = 5

# while completou_a_palavra == False and vidas_no_jogo > 0:
#     letra_escolhida_pelo_usuario = input('digite uma letra: ').strip().lower()
#     for letra in palavra_escolhida:
#         if letra_escolhida_pelo_usuario == letra:
#             mostrar_ao_usuario_aonde_ele_está += letra
#             print(mostrar_ao_usuario_aonde_ele_está)
#         else:
#             mostrar_ao_usuario_aonde_ele_está += "_"
#             print(mostrar_ao_usuario_aonde_ele_está)
#     if palavra_escolhida == mostrar_ao_usuario_aonde_ele_está:
#         completou_a_palavra = True
#     else:
#         vidas_no_jogo - 1


# import random
# word_list = [ 'alora', 'solucao', 'uniforme', 'colegio']

# word_choice = random.choice(word_list)

# blank_spaces=''
# for letter in word_choice:
#     blank_spaces += "_"

# print(word_choice)
# print(blank_spaces)

# game_status = False
# lifes = 6
# letter_box = []

# while not game_status and lifes > 0:
#     display = ''
#     user_guess = input("Guess a letter: ")
    
#     if user_guess in letter_box:
#         print('letter already guessed')
#         continue
    
    
#     for letter in word_choice:
#         if letter == user_guess:
#             display += letter
#             letter_box.append(letter)
#         elif letter in letter_box:
#             display += letter
#         else:
#             display += "_"
#     print(display)
    
#     if user_guess not in word_choice:
#         lifes -= 1     
#         print(f"you stil has {lifes} lifes")
#         if lifes == 0 :
#             print("game is lost\n")
#             print(f'the word was\n {word_choice}')
    
#     if display == word_choice:
#         game_status = True
#         print("won game")

# import random 

# word_list = ['desafio', 'costas', 'escolha', 'teste', 'mecanicas']
# word_choice = random.choice(word_list)
# # print(word_choice)
# blank_space = ''
# for letter in word_choice:
#     blank_space += "_"
# print(f'voce tem as seguintes letras para advinhar a palvra:\n{blank_space}')
# # user_guess = input('digite uma letra: ')
# # for letter in word_choice:
# #     if user_guess == letter:
# #         print(True)
# #     else:
# #         print(False)
# game_won = False
# lifes_game = 6
# box_of_letters = []
# tried_letters = []
# while not game_won and lifes_game > 0:
#     display = ''
#     user_guess = input('digite uma letra: ')
    
#     tried_letters.append(user_guess)
    
#     if user_guess in box_of_letters:
#         print(f"voce ja tentou essa letra: {user_guess}")
    
#     # if user_guess not in box_of_letters and not in word_choice:
#     #     lifes_game -= 1
    
#     for letter in word_choice:
#         if user_guess == letter:
#             display += letter
#             box_of_letters.append(letter)
#         elif letter in box_of_letters:
#             display += letter
#         else:
#             display += '_'
#     print(f'\n{display}')
    
#     if user_guess not in box_of_letters:
#         lifes_game -= 1
#         print(f'voce perdeu uma vida\nvoce ainda tem **{lifes_game}** vidas')
#     if lifes_game == 0:
#         print(f'voce perdeu, a palavra era: {word_choice}')
#     if display == word_choice:
#         print('Parabens voce acertou a palavra')
#         game_won = True
#     print(f'voce ja tentou as seguintes letras {tried_letters}')

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# print(alphabet.index('a') )
# number = 0
# new_text = ''

# def encrypt(a,b):
#     for letter in a:
#         number = alphabet.index(letter)
#         number = number + b
#         new_text += alphabet[number]
#     print(new_text)

# def life_in_weeks(age):
#     weeks = 90 - age
#     weeks_left = weeks * 52
#     return f"You have left {weeks_left} weeks in life"

# print(life_in_weeks(56))

# def calc_love_score(name1,name2):
#     name1 = name1.lower().strip()
#     name2 = name2.lower().strip()
    
#     box_of_letters = []
#     score_true = 0
#     score_love = 0
    
#     for letter in name1:
#         box_of_letters.append(letter)
#     for letter in name2:
#         box_of_letters.append(letter)
    
#     for letter in box_of_letters:
#         if letter == 't':
#             score_true += 1
#         if letter == 'r':
#             score_true += 1
#         if letter == 'u':
#             score_true += 1
#         if letter == 'e':
#             score_true += 1
#         if letter == 'l':
#             score_love += 1
#         if letter == 'o':
#             score_love += 1
#         if letter == 'v':
#             score_love += 1
#         if letter == 'e':
#             score_love += 1

#     return str(score_true) + str(score_love)


# print(calc_love_score("Kanye West", "Kim Kardashian"))


# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def encrypt(text, shift):
#     new_word = ''
    
#     for letter in text:
#         if letter == " ":
#             new_word += ' '
#         elif letter in alphabet:
#             new_index = (alphabet.index(letter) + shift) % 26
#             new_word += alphabet[new_index]
#         else:
#             new_word += letter  # preserva pontuação, números, etc.
    
#     print(f"Encrypted message: {new_word}")

# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)
# else:
#     print("Invalid option.")
print ('bela é linda demais, teste vscode github')