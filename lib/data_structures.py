spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    food_name_list = [spicy_foods["name"] for spicy_foods in spicy_foods]
    return food_name_list


def get_spiciest_foods(spicy_foods):
    speciest_food_list = [
        spicy_food for spicy_food in spicy_foods if spicy_food["heat_level"] > 5
    ]
    return speciest_food_list


def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        name = spicy_food["name"]
        cuisine = spicy_food["cuisine"]
        heat = "🌶" * spicy_food["heat_level"]
        print(f"{name} ({cuisine}) | Heat Level: {heat}")



def get_spicy_food_by_cuisine(spicy_foods, cuisine):
        for spicy_food in spicy_foods:
            if spicy_food['cuisine'] == cuisine:
                return spicy_food
        return None

def print_spiciest_foods(spicy_foods):
       for spicy_food in spicy_foods:
        if spicy_food["heat_level"] > 5:
            name = spicy_food["name"]
            cuisine = spicy_food["cuisine"]
            heat = "🌶" * spicy_food["heat_level"]
            print(f"{name} ({cuisine}) | Heat Level: {heat}")


def get_average_heat_level(spicy_foods):
    total_heat = sum(spicy_food['heat_level'] for spicy_food in spicy_foods)
    count = len(spicy_foods)
    heat_avarage_level = total_heat/ count
    return heat_avarage_level


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
