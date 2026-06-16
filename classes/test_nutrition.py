from nutrition_analyzer import NutritionAnalyzer
sample_nutrients = {
    "sugar": 80,
    "salt": 0.5,
    "saturated_fat": 2,
    "fat": 5,
    "calories": 150
}

analysis = NutritionAnalyzer().analyze_nutrition(sample_nutrients)
print(analysis)
warnings = NutritionAnalyzer().get_warning(analysis)
print(warnings)