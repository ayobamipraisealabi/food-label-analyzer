from classes.openfoodfacts_client import OpenFoodFactsClient

client = OpenFoodFactsClient()
result = client.search_by_name("Nutella")
print(result["product"]["product_name"])