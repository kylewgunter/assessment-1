import decimal
import math
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

def optimal_change (item_cost, amount_paid):
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
        'pennie': 1
    }
    remainder_whole = int(amount_paid - item_cost) # remainder value whole number
    
    remainder_float = str(amount_paid - item_cost)[2:]
    change_list = remainder_float.split('.')
    change_int = int(change_list[1])

    print(remainder_whole, change_int) # 37, 88


    money_currency_list = [] # target list for appended dict.keys
    money_value_list = [] # target list for appended dict.values


     # iterate over dict using items -- appends list vars with iterable list of keys and values
    for money_strs, money_value in dict_money_values.items(): # 
            money_currency_list.append(money_strs) 
            money_value_list.append(money_value)        

    print(money_currency_list, money_value_list)

    change_currency_list = []
    change_value_list = []

    for change_strs, change_value in dict_change_values.items(): # 
            change_currency_list.append(change_strs) 
            change_value_list.append(change_value) 
    
    print(change_currency_list, change_value_list)


    
   
    
    

    # i = 0
    # while amount_paid > 0:
    #     for x in range(amount_paid /money_value_list[i]): 
            
            
            #Iterate through the range of number / index at value list
            # answer_str += money_currency_list[i] # roman string adds I
            # # print(roman_str, roman_char_list[index])
            # amount_paid -= money_value_list[i] # num param decrements to 0 and breaks out
            # print(roman_value_list[index])
        # index += 1 # add 1 to index value to iterate through lists

    # return roman_str








optimal_change(62.12, 100)

    # optimal_change(62.13, 100)
    # > "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."

    # optimal_change(31.51, 50)
    # > "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies."