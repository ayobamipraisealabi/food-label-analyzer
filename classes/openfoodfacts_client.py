import requests
import re

class OpenFoodFactsClient:
    BASE_URL = "https://world.openfoodfacts.org/api/v2/product/"
    SEARCH_URL = "https://world.openfoodfacts.org/cgi/search.pl"
    HEADERS = {
        "User-Agent": "FoodLabelAnalyzer/1.0 (student project)"
    }

    def validate_barcode(self, barcode) -> bool:
        return bool(re.fullmatch(r'\d{8,14}', barcode))
    
    def fetch_by_barcode(self, barcode):
        if not self.validate_barcode(barcode):
            raise ValueError("Invalid barcode format. Barcode must be 8 to 14 digits long.")
        try:
            response = requests.get(f"{self.BASE_URL}{barcode}", headers=self.HEADERS, timeout=10)
            data = response.json()
            if response.status_code == 200 and data.get("status") == 1:
                return data.get("product")
            else:
                raise ValueError(f"Product not found for barcode: {barcode}")
        except requests.RequestException as e:
            raise ValueError(f"Error fetching product data: {e}")
        
    def search_by_name(self, name):
        try:
            params = {
                'search_terms': name,
                'search_simple': 1,
                'pagesize': 1,
                'json': 1
            }
            response = requests.get(self.SEARCH_URL, params=params, headers=self.HEADERS, timeout=10)
            data = response.json()
            if response.status_code == 200 and data.get("products"):
                return {"status": 1, "product": data["products"][0]}
            else:
                raise ValueError(f"Product not found for name: {name}")
        except requests.RequestException as e:
            raise ValueError(f"Error searching for products: {e}")