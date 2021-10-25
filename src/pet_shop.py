import pdb

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash_amount):
    pet_shop["admin"]["total_cash"] += cash_amount

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, number_of_pets_purchased):
    pet_shop["admin"]["pets_sold"] += number_of_pets_purchased

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    total_pets = []
    for pet in pet_shop["pets"]:
        if breed == pet["breed"]:
            total_pets.append(pet)
    return total_pets

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet_name == pet["name"]:
            return pet

def remove_pet_by_name(pet_shop, del_name):
    for pet in pet_shop["pets"]:
        if del_name == pet["name"]:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash_amount):
    customer["cash"] -= cash_amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, purchase):
    customer["pets"].append(purchase)

def customer_can_afford_pet(customer, purchase):
    if customer["cash"] >= purchase["price"]:
        can_buy_pet = True
    else:
        can_buy_pet = False
    return can_buy_pet

def sell_pet_to_customer(pet_shop, purchase, customer):
    if customer_can_afford_pet(customer, purchase) == True:
    # pdb.set_trace()
        add_pet_to_customer(customer, purchase)
        remove_customer_cash(customer, purchase["price"])
        increase_pets_sold(pet_shop, 1)
        add_or_remove_cash(purchase["price"])
        remove_pet_by_name(purchase["name"])

