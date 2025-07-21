with open("gemini_chat.py", "w") as f:
    f.write('''
import google.generativeai as genai

class GeminiChat:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name="gemini-2.5-pro")
        self.chat = self.model.start_chat()

    def send_message(self, prompt):
        response = self.chat.send_message(prompt)
        return response.text
''')
