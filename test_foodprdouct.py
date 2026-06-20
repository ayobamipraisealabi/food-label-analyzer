from classes.food_product import FoodProduct
from classes.openfoodfacts_client import OpenFoodFactsClient

test_client = OpenFoodFactsClient()

test_barcode = "3017620422003"  #nutella barcode

sorted_data = FoodProduct(test_client.fetch_by_barcode(test_barcode))
print()
print(sorted_data.to_dict())
print()
print(sorted_data.extract_nutrient(sorted_data.nutrients))
print()
print(sorted_data.parse_allergens(sorted_data.allergens))