
from pprint import pprint

def convert_in_cook_book():
    keys = ['ingridient_name', 'quantity', 'measure', ]
    global cook_book
    cook_book = {}

    with open('file.txt') as text_file:
        lines = []
        for line in text_file:
            line = line.strip()
            if line:
                lines.append(line)
        lines = iter(lines)

        for name in lines:
            cook_book[name] = []
            num = next(lines)

            for _ in range(int(num)):
                sostav_line = next(lines)
                ingrid = sostav_line.split(' | ')
                zip_object = zip(keys, ingrid)
                sostav_dict = {keys: ingrid for (keys, ingrid) in zip_object}
                cook_book[name].append(sostav_dict)
    return pprint(cook_book)
convert_in_cook_book()


def get_shop_list_by_dishes(dishes, person_count):
    convert_in_cook_book()
    # dishes = ['Омлет', 'Фахитос']
    # person_count = 2
    cook_list = {}
    for el in dishes:
        for ingr in cook_book[el]:
            ingr['quantity'] = int(ingr['quantity'])
            cook_list[ingr['ingridient_name']] = {'measure': ingr['measure'], 'quantity': ingr['quantity'] * person_count}

    pprint(cook_list)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)