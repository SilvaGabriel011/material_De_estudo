import dados_externos_cafe
import testing_area_coffe


MENU_BEBIDAS = dados_externos_cafe.MENU
RECURSOS = dados_externos_cafe.resources


def machine_software(bebidas,recursos):
    software_status = True
    while software_status == True:
        
        drink_choice = testing_area_coffe.first_choice()
        
        if drink_choice == 'report':
            testing_area_coffe.print_report(recursos)
            continue
        
        if not testing_area_coffe.stock_needed(recursos, bebidas[drink_choice]):
            # encerra se faltar algo
            return False
        
        paid_value = testing_area_coffe.payment_amount()
        theres_change = testing_area_coffe.payment_change(paid_value,float(bebidas[drink_choice]['cost']))
        if theres_change == False:
            continue
        else:
            print(f"there it is you {drink_choice}, and your exchange is: {theres_change:.2f}")
            
        enough_ingridients = testing_area_coffe.stock_needed(recursos,bebidas[drink_choice])
        if enough_ingridients == False:
            software_status = False
        else:
            recursos = testing_area_coffe.atualizar_estoque(recursos,bebidas[drink_choice])
        next_ = input("Do you want another? (y/n): ").strip().lower()
        if next_ != 'y':
            print("Thank you, goodbye!")
            return True

(machine_software(MENU_BEBIDAS,RECURSOS))