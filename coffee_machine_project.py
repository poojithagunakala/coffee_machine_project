# Coffee Machine Project
requirements = {
    "milk" : 500,
    "coffee" : 100,
    "water" : 100,
    "sugar" : 600,
    
    
}

Menu = {
    "latte" : {"ingredients":{
        "water" : 20,
        "coffee" : 25,
        "sugar" : 10,
        "milk" :40
      },
        "cost": 150
    },
    "expresso" : {"ingredients":{
       "water" : 15,
        "coffee" : 35,
        "sugar" : 20,
        "milk" :50 
    },
       "cost":100
    },
    "cappuccino":{
        "ingredients":{
        "water" : 25,
        "coffee" : 45,
        "sugar" : 35,
        "milk" :60
        },
         "cost":250
    }
}
profit = 0
def check_resources(order_ingredients):
    for items in order_ingredients:
        if order_ingredients[items] > requirements[items]:
            print(f" sorry there is not sufficient {items}")
            return False
    return True
def make_coffee(coffee_name,coffee_ingredients):
    for item in coffee_ingredients:
        requirements[item] -= coffee_ingredients[item]
    print(f"Here is your {coffee_name} Enjoy it!!")
is_on = True
def process_coins():
    print("please insert coins:")
    total = 0
    coins_five = int(input("How many 5rs coins?"))
    coins_ten = int(input("How many 10Rs coins?"))
    coins_twenty = int(input("How many 20Rs coins?"))
    total = coins_five*5 + coins_ten*10 +coins_twenty*20
    return total
def payment_successful(money_recieved,coffee_cost):
    if money_recieved >= coffee_cost:
        global profit
        profit = profit + coffee_cost
        change = money_recieved - coffee_cost
        print(f"Here is your remaining change {change}")
        return True
    else:
        print("Sorry that's not enough money. money will be refunded")
while is_on:
    customer_choice = input("enter your choice latte/expresso/cappuccino:\n")
    if customer_choice == "off":
        is_on = False
    elif customer_choice == "report":
        print(requirements)
    else:
        coffee_type = Menu[customer_choice]
        print(coffee_type)
        if check_resources(coffee_type["ingredients"]):
            payment = process_coins()
            if payment_successful(payment,coffee_type["cost"]):
               make_coffee(customer_choice,coffee_type["ingredients"])
               