import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Text-to-Speech setup
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Speech Recognizer
r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print("You:", command)
        return command
    except:
        speak("Sorry, I didn't catch that.")
        return ""

def main():
    speak("Hello! How can I help you?")
    while True:
        command = listen()

        if "time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time}")

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        elif "search" in command:
            query = command.replace("search", "").strip()
            speak(f"Searching for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")

        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break

        else:
            speak("I can tell the time, open Google, or search. Try saying one of those.")

if __name__ == "__main__":
    main()


