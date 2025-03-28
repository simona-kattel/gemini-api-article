import google.generativeai as genai
import json

#  API key from config file
with open("config.json") as config_file:
    config = json.load(config_file)

API_KEY = config["GEMINI_API_KEY"]
client = genai.configure(api_key=API_KEY)

#  the Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")  

def generate_article():
    # user inputs
    topic = input("Enter the topic for the article: ")
    language = input("Enter the language for the article: ")
    description = input("Enter a brief description of the article: ")
    
    # Defining the prompt with user inputs
    prompt = f"""
    Write a detailed article on '{topic}'.
    - Language: {language}
    - Description: {description}
    
    """
    
    # content generation
    response = model.generate_content(prompt)
    
    # Extracting the article
    article = {
        "title": f"The Future of {topic}",
        "language": language,
        "description": description,
        "content": response.text
    }
    
    #  JSON file
    file_name = f"{topic.replace(' ', '_').lower()}_article.json"
    with open(file_name, "w") as file:
        json.dump(article, file, indent=4)
    
    print(f"Article generated and saved as '{file_name}'!")
    print("\n--- Article Preview ---\n")
    print(response.text)


if __name__ == "__main__":
    generate_article()
