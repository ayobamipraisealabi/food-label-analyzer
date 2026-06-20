from classes.food_log import FoodLog

food_log = FoodLog()

test_dict = {
    "name": "Test Product",
    "brand": "Test Brand",
    "barcode": "1234567890123",
    "ingredients_text": "Test ingredients",
    "nutrients": {
        "energy_kcal": 100,
        "fat": 10,
        "saturated_fat": 5,
        "carbohydrates": 20,
        "sugars": 15,
        "fiber": 2,
        "proteins": 3,
        "salt": 1
    },
    "allergens": ["peanuts", "soy"]
}


food_log.save_product(test_dict)
food_log.save_product(test_dict)

print(food_log.load_all())