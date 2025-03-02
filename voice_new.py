import speech_recognition as sr
import pyttsx3
import pyautogui
import webbrowser
import os
from gesture6 import GestureMediaControl

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 175)

gesture = GestureMediaControl()

def speak(text):

    engine.say(text)
    engine.runAndWait()


def listen():
                    
    recognizer = sr.Recognizer()

    while True:

        print("Listening...")

        with sr.Microphone() as source:

            try:

                audio = recognizer.listen(source, timeout=10)
                text = recognizer.recognize_google(audio)

                print(f"You said: {text}")
                return text.lower()
                                
            except sr.UnknownValueError:

                print("Sorry, I could not understand.")
                #speak("Sorry, I could not understand.")
                return None
                                
            except sr.RequestError:

                print("Could not request results. Check your internet connection.")
                speak("Please Check your internet connection.")
                return None
                                
            except sr.WaitTimeoutError:

                print('Listening timed out')
                return None
                            
            


def open_application(app_name):

    if app_name:

        speak(f"Opening {app_name}")
        print(f"Opening {app_name}")

        try:
            os.system(f"start {app_name}")

        except Exception as e:

            speak(f"Sorry, I couldn't open {app_name}")
            print(f"Error: {e}")

def execute_command(command):
    
    if "youtube" in command:
        speak("Opening Youtube")
        print("Opening Youtube")
        webbrowser.open("https://www.youtube.com")
    
    elif "gesture" in command:
        gesture.start()

    elif "spotify web" in command:
        speak("Opening Spotify")
        print("Opening Spotify")
        webbrowser.open("https://open.spotify.com")

    elif "open" in command:
        app_name = command.replace("open", "").strip()
        open_application(app_name)
        print(f'Opening {app_name}')

    if "play" in command or "resume" in command:
        pyautogui.press("space")  # Play or resume

    elif "stop" in command:
        pyautogui.press("space")  # Pause

    elif "increase volume" in command:
        print('Increasing Volume')
        pyautogui.press("volumeup", presses=5)

    elif "decrease volume" in command:
        print('Decreasing Volume')
        pyautogui.press("volumedown", presses=5)

    elif "mute" in command:
        print('Volume muted')
        pyautogui.press("volumemute")
    
    elif "next" in command:
        print('Switching to next track')
        pyautogui.hotkey('ctrl', 'right')

    elif "previous" in command:
        print('Switching to previous track')
        pyautogui.hotkey('ctrl', 'left')
        pyautogui.hotkey('ctrl', 'left')

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "search" in command:
        search_query = command.replace("search", "").strip()
        if search_query:
            speak(f"Searching for {search_query}")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
        else:
            speak("What do you want to search for?")

    elif "exit" in command or "quit" in command or "stop" in command:
        speak("Goodbye!")
        exit()
    
    
def voice_assistant():

    wake_word = "hello media"
    flag = False

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening for wake word...")
        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)
        text = recognizer.recognize_google(audio)

        try:
                
            if text == wake_word:

                print("Wake word Detected! Activating the assisstant...")

                speak("Hello, I am your assistant. How can I help you?")
                flag = True

        except sr.UnknownValueError:
                print("Wake word not detected. Exiting...")

        except sr.RequestError:
                print("Error processing wake word.")

    while flag:
        command = listen()
        if command:
            execute_command(command)

if __name__ == "__main__":
    voice_assistant()
