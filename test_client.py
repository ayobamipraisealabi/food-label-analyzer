from classes.openfoodfacts_client import OpenFoodFactsClient

test_client = OpenFoodFactsClient()

test_barcode = "3017620422003"  #nutella barcode

print(test_client.fetch_by_barcode(test_barcode))

print(test_client.validate_barcode(test_barcode))

print(test_client.fetch_by_barcode("12345678"))