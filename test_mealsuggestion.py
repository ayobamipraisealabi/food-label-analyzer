from classes.meal_suggestion_generator import MealSuggestionGenerator

meal_generator= MealSuggestionGenerator()

explanation=meal_generator.explain_label(
    "Nutella",
    {"energy_kcal": 539, "sugars": 56.3, "salt": 0.107, "fat": 30.9},
    {"energy_kcal": "high", "sugars": "high", "salt": "low", "fat": "high"}
)

print(explanation)

alternative=meal_generator.suggest_alternatives(
    "Nutella",
    ["sugar", "palm oil", "hazelnuts", "skimmed milk powder", "cocoa"]
)
print(alternative)