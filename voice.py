import tkinter as tk
import speech_recognition as sr
import pyttsx3
import openai

# Add your OpenAI API key here
openai.api_key = "your_openai_api_key_here"

# Setup voice engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except:
            return "Sorry, I didn't catch that."

def get_ai_response(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}]
    )
    return response['choices'][0]['message']['content']

def start_voice_assistant():
    user_input = listen()
    response = get_ai_response(user_input)
    print("AI:", response)
    speak(response)

# GUI
app = tk.Tk()
app.title("Voice AI Assistant")

btn = tk.Button(app, text="Ask Me Something", command=start_voice_assistant, font=("Arial", 16), padx=20, pady=10)
btn.pack(pady=40)

app.mainloop()