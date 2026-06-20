class FoodProduct:
    def __init__(self, raw_data):
        self.name = raw_data.get("product_name", "Unknown Product")
        self.brand = raw_data.get("brands", "unknown Brand")
        self.barcode = raw_data.get("code", "unknown Barcode")
        self.ingredients_text = raw_data.get("ingredients_text", "")
        self.nutrients = self.extract_nutrient(raw_data.get("nutriments", {})) #the api returns the nutrients data in a nutriment dictionary
        self.allergens = self.parse_allergens(raw_data.get("allergens_tags", [])) #allergen as allergen_tags

    def extract_nutrient(self, nutriments):
        return {
            "energy_kcal": nutriments.get("energy-kcal_100g"),
            "fat": nutriments.get("fat_100g"),
            "saturated_fat": nutriments.get("saturated-fat_100g"),
            "carbohydrates": nutriments.get("carbohydrates_100g"),
            "sugars": nutriments.get("sugars_100g"),
            "fiber": nutriments.get("fiber_100g"),
            "proteins": nutriments.get("proteins_100g"),
            "salt": nutriments.get("salt_100g"),
        }   

    def parse_allergens(self, allergens_tag):
        if allergens_tag:
            return [tag.split(":")[-1] for tag in allergens_tag]
        else:
            return []

    def to_dict(self):
        return {
            "name": self.name,
            "brand": self.brand,
            "barcode": self.barcode,
            "ingredients_text": self.ingredients_text,
            "nutrients": self.nutrients,
            "allergens": self.allergens
        }