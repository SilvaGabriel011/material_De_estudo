import dados_externos_cafe
import math

MENU_2 = dados_externos_cafe.MENU
stock = dados_externos_cafe.resources

# print(dados_externos_cafe.resources["water"])

#acesso so os ingredientes
# print(MENU_2['latte']['ingredients'])

#acesso ao valor direto -- tipo float
# print(MENU_2['latte']['cost'])

# def descorbri_tipo(valor):
#     if isinstance(valor,float):
#         return True
#     else:
#         return False

# valornum = (MENU_2['latte']['cost'])
# valor_false = 12
# print(descorbri_tipo(valornum))
# print(descorbri_tipo(valor_false))


# def print_report(resources):
#     remaning_water = resources['water']
#     remaning_milk = resources['milk']
#     remaning_coffe = resources['coffee']
#     print(f"Water Remaning = {remaning_water}\nMilk Remaning = {remaning_milk}\nCoffe Remaning = {remaning_coffe}")

# print_report(stock)





#breakdown all to numbers and good naming 

# print(MENU_2['espresso']['ingredients']['water'])




#1. parte === interceptar cliente e decicdir caminho
def first_choice():
    """"inicia junto do sistema, escolha de caminho"""
    while True:
        choice = input("what would u like to order? (espresso/latte/capuccino): ").lower().strip()
        if choice == 'report':
            return choice
        elif choice != 'latte' and choice != "espresso" and choice != 'cappuccino':
            print("try only: espresso OR latte OR cappuccino")
            # print('\n'*10)
            continue
        return choice

# print(first_choice())
#2. parte === se o usuario pedir report imprime os ingredientes que restam na maquino
def print_report(resources):
    """"recebe um dicionario e retorna formatado seus valores"""
    remaning_water = resources['water']
    remaning_milk = resources['milk']
    remaning_coffe = resources['coffee']
    print(f"Water Remaning = {remaning_water}\nMilk Remaning = {remaning_milk}\nCoffe Remaning = {remaning_coffe}")

#3. troco
def payment_change(paid_item,item_value):
    if paid_item < item_value:
        print(f"there's not enough money\nITEM COSTS:{item_value}\nPAID VALUE:{paid_item}")
        return False
    else:
        return paid_item - item_value 

# print(payment_change(10,2))

#4. quanto foi pago
def payment_amount():
    ''''retorna a quantidade paga'''
    quarter_value = 0.50
    dimes_value = 0.20
    nickels_value = 0.10
    pennies_value = 0.01
    
    quarter_quantity =int(input("how many quarters?: "))
    dimes_quantity = int(input("hoy many dimes?: "))
    nickels_quantity = int(input("hoy many nickels?: "))
    pennies_quantity = int(input("hoy many pennies?: "))
    
    paid_value = (quarter_quantity * quarter_value) + (dimes_quantity * dimes_value) + (nickels_quantity * nickels_value) + (pennies_quantity * pennies_value)
    return paid_value
    
# print(payment_amount())


#5. quanto precisa pagar
def payment_needed(item, dicionario):
    if item == 'latte':
        return dicionario['latte']['cost']
    elif item == 'capuccino':
        return dicionario['cappuccino']['cost']
    else:
        return dicionario['espresso']['cost']

#6. custo de ingredientes pra maquina
def atualizar_estoque(estoque,bebida):
    for ingrediente in bebida['ingredients']:
        usado = bebida['ingredients'][ingrediente]
        estoque[ingrediente] = estoque[ingrediente] - usado
    return estoque



# DICIONARIO1 = {
#         'agua': 300,
#         'leite': 200,
#         'cafe' : 50
#             }

# DICIONARIO2 = {
#         'agua': 100,
#         'leite': 50,
#         'cafe' : 10
#             }



# def imprime_dicionario(dicionario):
#     return print(dicionario)

# imprime_dicionario(dicionario1)

def stock_needed(estoque ,bebeida):
    #condição de fazer, se algum desses aqui der TRUE, sai da função com false
        #se sair da função como false imprime 'nao da pra fazer' 
        #pode loopar dentro ainda com a quantidade reduzida

    faltando = {}
    
    for ingrediente in bebeida['ingredients']:
        precisa = bebeida['ingredients'][ingrediente]
        if ingrediente in estoque:
            disponivel = estoque[ingrediente]
        else:
            disponivel
        
        if disponivel < precisa:
            falta = precisa - disponivel
            faltando[ingrediente] = falta
    if len(faltando) == 0:
        return True
    else:
        print(f"Faltam os seguintes ingredients: {faltando}")
        return False

