import google.generativeai as genai
import json

with open("config.json") as config_file:
    config = json.load(config_file)

API_KEY = config["GEMINI_API_KEY"]
client = genai.configure(api_key=API_KEY)
# Initialize the client


# Select the Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")  # Or "gemini-pro" for longer responses

# Define the article prompt
prompt = """
Write a detailed article on 'The Future of Artificial Intelligence'.
- Word count: 500-600 words
- Tone: Professional and informative
- Sections: Introduction, Current Trends, Future Predictions, Conclusion
- Include real-world examples
"""

# Generate content
response = model.generate_content(prompt)

# Print the article
print(response.text)