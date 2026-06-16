class NutritionAnalyzer:
    THRESHOLDS={
        "sugar": {"low": 5, "high": 22.5},
        "salt": {"low": 0.3, "high": 1.5},
        "saturated_fat": {"low": 1.5, "high": 5},
        "fat": {"low": 3, "high": 17.5},
        "calories": {"low": 100, "high": 400}
    }

    def analyze_nutrition(self, nutrients) -> dict:
        analysis = {}
        for nutrient, value in nutrients.items():
            if nutrient in self.THRESHOLDS:
                thresholds = self.THRESHOLDS[nutrient]
                if value == None:
                    analysis[nutrient] = 'unknown'
                elif value < thresholds['low']:
                    analysis[nutrient] = 'low'
                elif value > thresholds['high']:
                    analysis[nutrient] = 'high'
                else:
                    analysis[nutrient] = 'medium'
        return analysis
    
    def get_warning(self, analysis) -> str:
        warnings = []
        for nutrient, level in analysis.items():
            if level == 'high':
                warnings.append(f"This product is high in {nutrient}")
            elif level == 'low':
                warnings.append(f"This product is low in {nutrient}")
        return ', '.join(warnings)

    def check_allergens(self, allergens, user_allergens) -> list:
        found_allergens = []
        for allergen in allergens:
            if allergen.lower() in [a.lower() for a in user_allergens]:
                found_allergens.append(allergen)
        return found_allergens