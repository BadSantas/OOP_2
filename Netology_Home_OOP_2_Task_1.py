import os

def read_recipes(file_path):
    if not os.path.exists(file_path):
        print(f"File '{file_path}' not found.")
        return []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

def parse_recipes(lines):
    recipes = {}
    index = 0
    while index < len(lines):
        dish_name = lines[index].strip()
        if not dish_name:
            index += 1
            continue
        index += 1
        if index >= len(lines):
            print(f"Error: Missing ingredient count for dish '{dish_name}'")
            break
        try:
            ingredient_count = int(lines[index].strip())
        except ValueError:
            print(f"Error: Invalid ingredient count for dish '{dish_name}' at line {index + 1}")
            break
        index += 1
        ingredients = []
        for _ in range(ingredient_count):
            if index >= len(lines):
                print(f"Error: Missing ingredient data for dish '{dish_name}'")
                break
            ingredient_data = lines[index].strip().split(' | ')
            if len(ingredient_data) != 3:
                print(f"Error: Invalid ingredient format for dish '{dish_name}' at line {index + 1}")
                break
            ingredient_name = ingredient_data[0]
            try:
                quantity = int(ingredient_data[1])
            except ValueError:
                print(f"Error: Invalid quantity for ingredient '{ingredient_name}' in dish '{dish_name}' at line {index + 1}")
                break
            measure = ingredient_data[2]
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
            index += 1
        recipes[dish_name] = ingredients
    return recipes

def get_shop_list_by_dishes(dishes, person_count, recipes):
    shop_list = {}
    for dish in dishes:
        if dish in recipes:
            for ingredient in recipes[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                else:
                    shop_list[ingredient_name] = {
                        'quantity': quantity,
                        'measure': measure
                    }
        else:
            print(f"Dish '{dish}' not found in recipes.")
    return shop_list

def print_shop_list(shop_list):
    for ingredient, details in shop_list.items():
        print(f"{ingredient}: {details['quantity']} {details['measure']}")

def print_recipes(recipes):
    for dish_name, ingredients in recipes.items():
        print(f"Название блюда: {dish_name}")
        print(f"Количество ингредиентов: {len(ingredients)}")
        for ingredient in ingredients:
            print(f"{ingredient['ingredient_name']} | {ingredient['quantity']} | {ingredient['measure']}")
        print()

def main():
    print("Current Working Directory:", os.getcwd())
    file_path = 'recipes.txt'
    lines = read_recipes(file_path)
    if lines:
        recipes = parse_recipes(lines)
        print_recipes(recipes)
        dishes = ['Омлет', 'Фахитос'] # Пример списка блюд
        person_count = 3 # Пример количества персон
        shop_list = get_shop_list_by_dishes(dishes, person_count, recipes)
        print_shop_list(shop_list)

if __name__ == "__main__":
    main()