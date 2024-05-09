import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('dummy')
engine.say("Hello, this is a test.")
engine.runAndWait()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("It is a fine morning.")

    elif 12 <= hour < 18:
        speak("Hope you had your brunch, Good Afternoon!")

    else:
        speak("The wind is lovely, Good Evening!")

    speak("Hello, How are you? I am your personal AI Assistant! How can I be of service?")


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:

        print("I could not get you, please speak again")
        return "None"
    return query


if __name__ == "__main__":
    greet()

    if 1:
        query = command().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(f'{query}', sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open code website' in query:
            webbrowser.open("codexcue.online")

        elif 'the weather' in query:
            webbrowser.open("weather.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {strTime}")
