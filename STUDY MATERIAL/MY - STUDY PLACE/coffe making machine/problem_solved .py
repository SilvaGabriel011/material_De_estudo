import dados_externos_cafe
import testing_area_coffe

MENU = dados_externos_cafe.MENU
RESOURCES = dados_externos_cafe.resources


def machine_software(bebidas, recursos):
    """Retorna True se for encerrado normalmente, ou False se terminar por erro."""
    while True:
        choice = testing_area_coffe.first_choice()

        # 1. Se pedir report, mostra e recomeça
        if choice == 'report':
            testing_area_coffe.print_report(recursos)
            continue

        # 2. Verifica disponibilidade de ingredientes
        if not testing_area_coffe.stock_needed(recursos, bebidas[choice]):
            # encerra se faltar algo
            return False

        # 3. Solicita pagamento
        paid = testing_area_coffe.payment_amount()
        cost = bebidas[choice]['cost']
        change = testing_area_coffe.payment_change(paid, cost)
        if change is False:
            # fundo insuficiente
            return False
        print(f"Here is your {choice}. Your change: ${change:.2f}")

        # 4. Atualiza estoque
        recursos = testing_area_coffe.atualizar_estoque(recursos, bebidas[choice])

        # 5. Pergunta se quer mais
        next_ = input("Do you want another? (y/n): ").strip().lower()
        if next_ != 'y':
            print("Thank you, goodbye!")
            return True


# Não envolve em print() porque já retorna status
machine_software(MENU, RESOURCES)
