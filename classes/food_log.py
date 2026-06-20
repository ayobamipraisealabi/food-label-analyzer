import json
import os


class FoodLog:
    def __init__(self):
        self.filepath = "data/food_log.json"
        self.ensure_path_exists()


    def ensure_path_exists(self):
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w') as f:
                json.dump([], f)  # Initialize with an empty list

    def load_all(self):
        try :
            with open(self.filepath, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        
    def save_product(self, product_dict):
        self.ensure_path_exists()
        all_products = self.load_all()
        all_products.append(product_dict)
        with open(self.filepath, 'w') as f:
            json.dump(all_products, f, indent=4)

        