import google.generativeai as genai
import json

# Load API key from config file
with open("config.json") as config_file:
    config = json.load(config_file)

API_KEY = config["GEMINI_API_KEY"]
client = genai.configure(api_key=API_KEY)

# Select the Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")  # Use "gemini-pro" for longer responses

def generate_article():
    # Get user inputs
    topic = input("Enter the topic for the article: ")
    language = input("Enter the language for the article: ")
    description = input("Enter a brief description of the article: ")
    
    # Define the prompt with user inputs
    prompt = f"""
    Write a detailed article on '{topic}'.
    - Language: {language}
    - Description: {description}
    
    """
    
    # Generate content using the Gemini model
    response = model.generate_content(prompt)
    
    # Extract and structure the article
    article = {
        "title": f"The Future of {topic}",
        "language": language,
        "description": description,
        "content": response.text
    }
    
    # Save the article as a JSON file
    file_name = f"{topic.replace(' ', '_').lower()}_article.json"
    with open(file_name, "w") as file:
        json.dump(article, file, indent=4)
    
    print(f"Article generated and saved as '{file_name}'!")
    print("\n--- Article Preview ---\n")
    print(response.text)

# Run the script
if __name__ == "__main__":
    generate_article()
