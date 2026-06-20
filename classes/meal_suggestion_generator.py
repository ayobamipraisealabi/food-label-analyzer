import os
from google import genai
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class MealSuggestionGenerator:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")
        self.client = genai.Client(api_key=self.api_key)
        self.model_name = "gemini-3.5-flash"

    def explain_label(self, product_name, nutrients: dict, analysis: dict) -> str:
        prompt = f"In 2-3 short sentences, explain this food label for {product_name} in simple terms for a general audience. Nutrients: {nutrients}. Analysis: {analysis}. Mention anything rated 'high'., also provide healthier alternatives or recipe suggestions using similar ingredients, "
        try:
            response = self.client.models.generate_content(
                model = self.model_name,
                contents = prompt
            )
            return response.text.strip()
        except Exception as e:
            return f"could not generate an explanation: {e}"


    def suggest_alternatives(self, product_name, ingredients):
        prompt = f"A user scanned '{product_name}' with these main ingredients: {', '.join(ingredients[:10])}. In 3-4 short sentences, suggest 2 healthier alternative products and 1 simple recipe idea using similar ingredients but healthier."
        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt
            )
            return response.text.strip()
        except Exception as e:
            return f"Could not generate suggestions: {e}"