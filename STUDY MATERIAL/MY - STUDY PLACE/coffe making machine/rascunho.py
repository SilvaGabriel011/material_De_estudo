# import dados_externos_cafe

# # print(dados_externos_cafe.MENU['latte']['ingredients'])


# def diminui_agua(dicionario):
#     agua = str(dicionario['latte']['ingredients']['water'])
#     return dicionario['latte']['ingredients'][agua]
    

# print(diminui_agua(dados_externos_cafe.MENU))

# def do_hot_drink(dicionario_stock,dicionario_bebida):
#     #vai usar
#     agua_utilizada = dicionario_bebida['water']
#     cafe_utilizado = dicionario_bebida['coffe']
#     leite_utilizado = dicionario_bebida['milk']

#     #tem disponivel
#     agua_disponivel = dicionario_stock['ingredients']['water']
#     cafe_disponivel = dicionario_stock['ingredients']['coffe']
#     leite_disponivel = dicionario_stock['ingredients']['milk']

#     #conta
#     agua_sobra = agua_disponivel - agua_utilizada
#     cafe_sobra = cafe_disponivel - cafe_utilizado
#     leite_sobra = leite_disponivel - leite_utilizado

#     return {'agua': agua_sobra, 'cafe': cafe_sobra, 'leite': leite_sobra}



# def first_choice():
#     """"inicia junto do sistema, escolha de caminho"""
#     while True:
#         choice = input("what would u like to order? (espresso/latte/capuccino): ")
#         if choice != 'latte' and choice != "espresso" and choice != 'cappuccino':
#             print("try only: espresso OR latte OR cappuccino")
#             print('\n'*10)
#             continue
#         return choice

# print(first_choice())


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# def teste_print_dicionario(dicionario):
#     for ingrediente in dicionario['ingredients']:
#         print (dicionario['ingredients'][ingrediente])

# teste_print_dicionario(MENU["latte"])
# teste_print_dicionario(MENU["cappuccino"])


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

def atualizar_estoque(estoque,bebida):
    for ingrediente in bebida['ingredients']:
        usado = bebida['ingredients'][ingrediente]
        estoque[ingrediente] = estoque[ingrediente] - usado
    return estoque

print(stock_needed(resources,MENU['espresso']))

print(atualizar_estoque(resources,MENU['espresso']))