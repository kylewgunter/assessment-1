import decimal
import math
from typing import KeysView
# branch Kyle-Solution

# Problem set
# > "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."

# optimal_change(31.51, 50)
# > "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies."


# Pseudo Code
# import math for float int/ math.floor/ math fixed/decimal?
# item_cost = 1st arg
# Create a dict obj that equals key and values of '$20' : 20
# Create empty lists for key and values
# iterate over dict and output to iterable lists
# 


def optimal_change (item_cost, amount_paid, ):
    # print(item_cost, amount_paid)

    dict_money_values = {
        '$100': 100,
        '$50': 50,
        '$20': 20,
        '$10': 10,
        '$5': 5,
        '$1': 1,
        }
    
    dict_change_values = {
        'quarter': 25,
        'dime': 10,
        'nickle': 5,
        'penny': 1
    }
    
    remainder_int = math.floor(amount_paid - item_cost) # remainder value whole number
    remainder_float = str(amount_paid - item_cost)[2:]
    
    change_decimal_list = remainder_float.split('.')
    change_int = int(change_decimal_list[1])

    print(remainder_int, change_int) # 37, 88

    money_currency_list = [] # target list for appended dict.keys
    money_value_list = [] # target list for appended dict.values


     # iterate over dict using items -- appends list vars with iterable list of keys and values
    for money_strs, money_value in dict_money_values.items(): # 
            money_currency_list.append(money_strs) 
            money_value_list.append(money_value)        

    # print(money_currency_list, money_value_list)

    change_currency_list = []
    change_value_list = []

    for change_strs, change_value in dict_change_values.items(): # 
            change_currency_list.append(change_strs) 
            change_value_list.append(change_value) 
    
    # print(change_currency_list, change_value_list)

    dollar_list = []

    i = 0
    while remainder_int > 0:
        for x in range(math.floor(remainder_int /money_value_list[i])): 
            dollar_list.append(money_currency_list[i])
            remainder_int -= money_value_list[i]
        i += 1 

    change_list = []
    change_dict = {}
    
    
    j = 0
    while change_int > 0:
        for x in range(math.floor(change_int/change_value_list[j])): 
            change_list.append(change_currency_list[j])
            change_int -= change_value_list[j]
            print(change_value_list[j])
            x + 1
        j += 1 
    
    change_dict = dict.fromkeys(change_list)

    # print(change_list, change_dict)

optimal_change(62.12, 100)

    # optimal_change(62.13, 100)
    # > "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."

    # optimal_change(31.51, 50)
    # > "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies."