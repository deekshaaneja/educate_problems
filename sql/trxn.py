import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

number_of_days = int(input())
number_of_ingredients = int(input())

for i in range(number_of_days):
    try:
        ingredient_id = input()
    except:
        pass


def len_map(ingredients_map):
    total = 0
    for elem in ingredients_map:
        total = total + len(ingredients_map[elem])
    return total

ingredients_map = {"FAT":[], "FIBER":[], "CARB":[]}
output = ["-"]*number_of_days


for i in range(number_of_days):
    try:
        ingredient_id = input()
    except:
        pass

    if ingredient_id.startswith("FAT"):
        ingredients_map['FAT'].append((ingredient_id,i))
    elif ingredient_id.startswith("CARB"):
        ingredients_map['CARB'].append((ingredient_id,i))
    elif ingredient_id.startswith("FIBER"):
        ingredients_map['FIBER'].append((ingredient_id,i))

    if len_map(ingredients_map) < number_of_ingredients:
        pass
    else:
        sixty_percent = math.ceil(number_of_ingredients*.6)
        category_exists = None
        for elem in ingredients_map:
            ingred_list = ingredients_map[elem]
            if len(ingred_list) >= sixty_percent:
                category_exists = elem
        if category_exists is None:
            continue
        else:
            list_of_all_ingreds = []
            out_ingreds = []
            for elem in ingredients_map:
                list_of_all_ingreds = list_of_all_ingreds + ingredients_map[elem]

            list_of_all_ingreds.sort(key=lambda x:x[1])
            count = sixty_percent
            for ingred in list_of_all_ingreds:
                if ingred[0].startswith(category_exists) and count > 0:
                    list_of_all_ingreds.remove(ingred)
                    out_ingreds.append(ingred)
                    count -= 1
            remaining_items = number_of_ingredients-sixty_percent
            while (remaining_items > 0):
                out_ingreds.append(list_of_all_ingreds[0])
                list_of_all_ingreds.pop(0)
                remaining_items -= 1
            
            out_ingreds.sort(key=lambda x:x[1])
            out_string = ":".join([elem[0] for elem in out_ingreds])
            output[i] = out_string

            ingredients_map = {"FAT":[], "FIBER":[], "CARB":[]}

            for elem in list_of_all_ingreds:
                if elem[0].startswith('FAT'):
                    ingredients_map['FAT'].append(elem)
                if elem[0].startswith('FIBER'):
                    ingredients_map['FIBER'].append(elem)
                if elem[0].startswith('CARB'):
                    ingredients_map['CARB'].append(elem)


o = ''.join(output)
print(str(o), file=sys.stdout)