import pyttsx3
import speech_recognition as sr
import wikipedia 
import webbrowser
import smtplib


engine = pyttsx3.init('sapi5')
engine.setProperty("rate", 178)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    speak("I am Migo, Sir Please tell me how may I help you")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Your Response: {query}\n")

    except Exception as e:
           
        print("Can you say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('maolarabana@gmail.com', 'Rabana2me')
    server.sendmail('maolarabana@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'open ' in query:
            web = query.split()
            webname = web[1]
            webbrowser.open(webname+'.com')
            speak(f"Opening {webname}")

      
        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("Please input the receivers email ")
                to = input()    
                sendEmail(to, content)
                speak("Email has been successfully sent")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send this email")   

        else:

            try:
                
                speak('Searching for result...')
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak("I'm afraid i do not know the answer to that sir.") 
