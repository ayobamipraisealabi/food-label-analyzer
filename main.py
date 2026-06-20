import streamlit as st
import pandas as pd
from classes.openfoodfacts_client import OpenFoodFactsClient
from classes.food_product import FoodProduct
from classes.nutrition_analyzer import NutritionAnalyzer
from classes.meal_suggestion_generator import MealSuggestionGenerator
from classes.food_log import FoodLog

st.title("🍎 Food Label Analyzer")

client = OpenFoodFactsClient()
analyzer = NutritionAnalyzer()
log = FoodLog()

search_input = st.text_input("Enter a barcode (numbers only) or product name:")

if st.button("Search"):
    try:
        if search_input.isdigit():
            # st.write(f"DEBUG: searching for '{search_input}'")  i encountered a problem so i used this for debugging
            raw_data = client.fetch_by_barcode(search_input)
        else:
            result = client.search_by_name(search_input)
            raw_data = result["product"]

        product = FoodProduct(raw_data)

        st.success(f"Found: {product.name} ({product.brand})")

        # Show nutrients table
        df = pd.DataFrame(product.nutrients.items(), columns=["Nutrient", "Value (per 100g)"])
        st.dataframe(df)

        # Show analysis
        analysis = analyzer.analyze_nutrition(product.nutrients)
        warnings = analyzer.get_warning(analysis)
        if warnings:
            st.warning(warnings)
        else:
            st.success("No major nutrition concerns detected.")

        # Show allergens
        if product.allergens:
            st.error(f"Allergens detected: {', '.join(product.allergens)}")

        # AI explanation
        with st.spinner("Getting AI explanation..."):
            generator = MealSuggestionGenerator()
            explanation = generator.explain_label(product.name, product.nutrients, analysis)
            st.write("### What This Means")
            st.write(explanation)

            alternatives = generator.suggest_alternatives(product.name, product.ingredients_text.split(","))
            st.write("### Healthier Alternatives")
            st.write(alternatives)

        # Save button
        if st.button("Save to Food Log"):
            log.save_product(product.to_dict())
            st.success("Saved!")

    except ValueError as e:
        st.error(f"Error: {e}")
    except Exception as e:
        st.error(f"Something went wrong: {e}")

# Show saved log
st.write("---")
st.write("## Your Food Log")
saved = log.load_all()
if saved:
    log_df = pd.DataFrame(saved)
    st.dataframe(log_df)
else:
    st.write("No products saved yet.")