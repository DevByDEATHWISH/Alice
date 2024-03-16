import datetime
import config
import character
import google.generativeai as genai

api_key = config.GOOGLE_API_KEY
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.0-pro-latest")
safety_settings = {
    "HARM_CATEGORY_SEXUALLY_EXPLICIT": "block_none",
    "HARM_CATEGORY_HATE_SPEECH": "block_none",
    "HARM_CATEGORY_HARASSMENT": "block_none",
    "HARM_CATEGORY_DANGEROUS_CONTENT": "block_none",
}

chat = model.start_chat(history=[])


def startup():
    message = character.character
    print(message)
    try:
        output = chat.send_message(message, safety_settings=safety_settings)
        character.answer = output.text
    except Exception as e:
        print(f"An error occurred: {e}, trying again.")
        startup()

startup()


def get_character():
    character.timestamp = " ["+str(datetime.datetime.now())+"]"
    message = character.input + character.timestamp
    print(message)
    try:
        output = chat.send_message(message, safety_settings=safety_settings)
        character.answer = output.text
        print(character.answer)
    except Exception as e:
        print(f"An error occurred: {e}")
        character.answer = "Desculpe, encontrei um erro, poderia repetir por favor?"
    return character.answer
