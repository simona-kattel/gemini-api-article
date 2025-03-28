
import json
import google.generativeai as genai

# Load the configuration file and configure the API
config = json.load(open("config.json", "r"))
api = genai.configure(api_key=config["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini_2.0_flash")


class Response:
    def __init__(self, topic, description, language):
        self.topic = topic
        self.description = description
        self.language = language
        self.response = self.generate_response()

    def generate_response(self):
        # Construct the prompt
        prompt = f"Write an article on {self.topic} {self.description} in {self.language}."
        # Use the generative model to generate a response
        response = model.generate_response(prompt)
        return response.text

    def get_article(self):
        # Create the article content as a dictionary
        article = {
            "title": f"The Future of {self.topic}",
            "language": self.language,
            "description": self.description,
            "content": self.response,
        }
        return article


class JSONResponse(Response):
    def __init__(self, topic, description, language):
        # initializer
        super().__init__(topic, description, language)

    def save_to_file(self):
       
        file_name = f"{self.topic.replace(' ', '_').upper()}_ARTICLE.json"
        #  article to a JSON file
        article = self.get_article()
        with open(file_name, "w") as file:
            json.dump(article, file, indent=4)
       
        print(f"File saved as: {file_name}")
        print(f"Generated Content:\n{self.response}")


if __name__ == "__main__":
   #user input
    topic = input("Enter topic: ")
    description = input("Enter description: ")
    language = input("Enter language: ")

    json_response = JSONResponse(topic, description, language)
    json_response.save_to_file()
