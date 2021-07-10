import math
import re

# Pseudo Code
# 1. If- item cost and amount paid == 0 return 0 and "No transaction"

# 2.
# Elif- item cost is greater than amount paid 
# return "Item too expensive"

# 3.
# Else - construct a dictonary of money currency values * 100 to elimnate floats.
# remainder = 100 * amount paid - Item cost to eliminate decimals.
# construct answer string variable
# construct a change dictionary for the answer.

# while remainder is greater than 0, iterate over currency keys, values.
# change dictionary equals to result var
# Remainder var uses math round of remainder minus the result and multiplied by the current value and force it to two decimal places to eliminate decimals. returns the result to remainder value in the while loop.

# ***Run answer string function that takes in change dict, amount paid, item cost and output string
# create initial output string of optimal change and amount paid
# iterate over change dict for keys and values
# import re for regex search
# create change string to find the values of change types- quarter, dime, nickle, penn
# create search for change string
# construct output string if value is greater than 1 and no match for regex search... make dollar values output "bills"
# construct output string if value is equal to 1 and no match for regex search... make dollar values output "bill"
# construct output string if value is greater than 1 and match for regex search... make change values add "s"
# construct output string if value is equal to 1 and match for regex search... return singular change values
# Nested elif statement for "penn"... if value is equal to 1 - add 'y', if value is greater than 1, add 'ies'.



def optimal_change (item_cost, amount_paid):
    # 1.
    if item_cost == 0 and amount_paid == 0:
        return "No transaction"
    # 2.
    if item_cost > amount_paid:
        return "Item too expensive!"
    # 3.
    else:
        dict_currency = {
            '$100': 10000,
            '$50': 5000,
            '$20': 2000,
            '$10': 1000,
            '$5': 500,
            '$1': 100,
            'quarter': 25,
            'dime': 10,
            'nickle': 5,
            'penn': 1
            }
        # eliminate possible float issues by multiplying by 100.
        remainder = 100 * (amount_paid - item_cost)        
        
        
        answer = ""
        change_dict = {
        }
 
        # loop through remainder value until value is zero
        while remainder > 0:
            
            for key in dict_currency:
                value = dict_currency[key]      
                result = math.floor(remainder/value)

                if result > 0:
                    change_dict[key] = result 
                    remainder = round(remainder - (result * value), 2)
                
        answer = answer_output(item_cost, amount_paid, change_dict, answer)
        return answer

def answer_output(item_cost, amount_paid, change_dict, output):
    
    output += f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is "

    for key in change_dict:
        value = change_dict[key]
        num_entries = len(change_dict)

        change_str = 'quarter, dime, penn'
        change_search = re.search(key, change_str)
    
        if key == "penn":
            if value > 1:
                output += "and " + f"{value}" + " " + f"{key}ies."
            elif value == 1:
                output += "and " + f"{value}" + f"{key}y." 

        elif num_entries > 2:
            if change_search == None:
                if value > 1:
                    output += f"{value}" + " " + f"{key}" + " bills, "
                elif value == 1:
                    output += f"{value}" + " " + f"{key}" + " bill, "
            elif key != "penn":
                if value > 1:
                    output += f"{value}" + " " + f"{key}s" + ", "
                elif value == 1:
                    output += f"{value}" + " " + f"{key}" + ", "
        
        elif num_entries == 2:
            if change_search == None:
                if value > 1:
                    output += f"{value}" + " " + f"{key}" + " bills" + ", "
                elif value == 1:
                    output += f"{value}" + " " + f"{key}" + " bill" + ", "
            elif key != "penn" and num_entries > 1:
                if value > 1:
                    output += "and " f"{value}" + " " + f"{key}s" + "."
                elif value == 1:
                    output += "and " f"{value}" + " " + f"{key}" + "."

        elif num_entries == 1:
            if change_search == None:
                if value > 1:
                    output += f"{value}" + " " + f"{key}" + " bills" + "."
                elif value == 1:
                    output += f"{value}" + " " + f"{key}" + " bill" + "."
            elif key != "penn" and num_entries > 1:
                if value > 1:
                    output += "and " f"{value}" + " " + f"{key}s" + "."
                elif value == 1:
                    output += "and " f"{value}" + " " + f"{key}" + "."
                    
    return output

# optimal_change(62.13, 100)
# optimal_change(31.51, 50)
# optimal_change(49, 50)
# optimal_change(48.50, 50)