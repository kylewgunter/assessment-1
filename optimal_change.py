import math
import re

# Pseudo Code
# 1. If- item cost and amount paid == 0 return 0 and "No transaction"

# 2.
# Elif- item cost is greater than amount paid 
# return "Item too expensive"

# 3. Create change dicitionay from change maker function
# change string calls string builder function
# answer string produces initial input of item cost and amount paid and adds change string builder
# return answer

# 4. change maker function takes in remainder
# creates a dictionary from currency values
# construct change dictionary from key and values while remainder is greater than 0
# result == math.floor divide remainder by value
# if result is greater than 0 construct change dict key and value == result
# remainder = round to two decimal places to fixed float and minus from remainder
# return change dict

# 5. 
# string builder function takes in parameter of change dictionary
# create string var of ''
# for index and the key, enumerate over change dictionary
# dictionary length var = length of dict
# if index plus 1 == next entry == dict length and length is greater > 1, add "and"
# if index plus 1 == next entry == the last entry of dict add "."
# else change string calls plural or singular function
# return  change string

# 6. plural or singular for keys and values of change dict
# if value == 1 return the value and the key
# if value is > 1 and the key == "penny", change key to "pennies"
# if value is > 1, return key and value, add "s" for plural.




def optimal_change (item_cost, amount_paid):
    # 1.
    if item_cost == 0:
        return "No transaction"
    # 2.
    if item_cost > amount_paid:
        return "Item too expensive!"
    # 3.
    else:
        change_dictionary = change_maker(100 * (amount_paid - item_cost))
        change_string = string_builder(change_dictionary)
        answer = f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is " + change_string
        return answer
# 4.
def change_maker(remainder):
    dict_currency = {
        '$100 bill': 10000,
        '$50 bill': 5000,
        '$20 bill': 2000,
        '$10 bill': 1000,
        '$5 bill': 500,
        '$1 bill': 100,
        'quarter': 25,
        'dime': 10,
        'nickel': 5,
        'penny': 1
    }
    change_dict = {}
    while remainder > 0:
        for key in dict_currency:
            value = dict_currency[key]
            result = math.floor(remainder/value)
            if result > 0:
                change_dict[key] = result
                remainder = round(remainder - (result * value), 2)
    return change_dict

# 5.

def string_builder(change_dictionary):
    change_string = ''
    for i, key in enumerate(change_dictionary):
        dictionary_length = len(change_dictionary)
        value = change_dictionary[key]
        if i + 1 == dictionary_length and dictionary_length > 1:
            change_string += 'and '
        if i + 1 == dictionary_length:
            change_string += f"{plural_or_singular(value, key)}."
        else:
            change_string += f"{plural_or_singular(value, key)}, "
    return change_string

# 6.
def plural_or_singular(value, key):
    print(value, key)
    if value == 1:
        return f"{value} {key}"
    if value > 1 and key == "penny":
        return f"{value} pennies"
    if value > 1:
        return f"{value} {key}s"