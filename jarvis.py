import pyttsx3   # python library which converts text to speech
import speech_recognition as sr    #It is a python module which converts speech to text
import datetime    # This library provides us the actual date and time
import os , sys  # It is a python libraries for graphical user interface / It allows operating on the interpreter as it provides access to the 
                 #variables and functions that usually interact strongly with the interpreter.
import random
import wikipedia   #It is a python module for searching anything on  Wikipedia
import requests,webbrowser    #Simple mail transfer protocol that allows us to send mails and to route mails between mail servers.
import time 
import pyautogui as py    # It is a python libraries for graphical user interface 
from gtts import gTTS      #a Python library and CLI tool to interface with Google Translate’s text-to-speech API
import smtplib              #Simple mail transfer protocol that allows us to send mails and to route mails between mail servers.
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import psutil     #Psutil is a Python cross-platform library used to access system details and process utilities
import requests   #The requests library is the de facto standard for making HTTP requests in Python
from bs4 import BeautifulSoup   #Beautiful Soup is a Python library that is used for web scraping purposes to pull the data out of HTML and XML files
from pywikihow import search_wikihow   #unofficial wikihow python api

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

# text ko speech me
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def mailsend():
    email = 'sender email'
    password = 'email password'
    send_to_mail = 'recevivers email'
    speak("okey sir, what is the subject for this email")
    query = takecommand()
    subject = query
    speak("and sir , what is the message for this email")
    query2 = takecommand()
    messagess = query2
    speak("sir please enter the correct path of the attachment file with one extra slash")
    file_location = input("please enter the path here: ")

    speak("sending email this will take few seconds,please wait...")


    msg = MIMEMultipart()
    msg['from'] = email
    msg['to'] = send_to_mail
    msg['subject'] = subject

    msg.attach(MIMEText(messagess,'plain'))


    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application','octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('content-Disposition',"attachment; filename= %s" % filename)


    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()
    server.login(email,password)
    text1 = msg.as_string()
    server.sendmail(email,send_to_mail,text1)
    server.quit()
    speak("email has been sent ")

def tellTime():
    strtime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"sir the time is {strtime}")


def location(): #to get location 
    res = requests.get('https://ipinfo.io/')
    data = res.json()
    city = data['city']
    location = data['loc'].split(',')
    latitude = location[0]
    longitude = location[1]
    print("latitude : ", latitude)
    print("longitude :",longitude)
    print("city :",city)
    speak(f" i think we are in {city} city")


def news(): #to get mews from API
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=77caacf8cab84a0dba6d6cf31ce1df4b'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["fist","second","third","forth","fifth","sixth","seventh","eight","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is : {head[i]}")

def takecommand(): #to take command
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=4,phrase_time_limit=7)
    try:
        print("recognizing")
        query = r.recognize_google(audio,language='en-us')
        print(f'user said : {query}')
    except Exception as e:
        return "none"
        query = query.lower()
    return query

def wish(): #for wish and tell time 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    tellTime()
    speak("hello my name is jarvis i am your personal assistant how may i help you")
    
def taskexe(): #task executer
    wish()
    while True:
        query = takecommand().lower() #take user query
        if "open notepad" in query:
            speak("opening notepad")
            path = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(path)
            time.sleep(3)

        elif "close notepad" in query:
            speak("okey.. sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "play some music" in query:
            speak("hope you like it..")
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            n = len(songs)
            indexx = random.randint(1,n)
            os.startfile(os.path.join(music_dir, songs[indexx]))

        elif "open android studio" in query:
            speak("ohk.. wait a second i am starting android studio")
            apath = "C:\\Program Files\\Android\Android Studio\\bin\\studio64.exe"
            os.startfile(apath)
            time.sleep(5)

        elif "close android studio" in query:
            speak("okey.. sir, closing android studio")
            os.system("taskkill /f /im studio64.exe")

        elif "open vs code" in query:
            speak("opening vs code")
            vpath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(vpath)
            time.sleep(3)

        elif "close vs code " in query:
            speak("okey.. sir, closing vs code")
            os.system("taskkill /f /im code.exe")

        elif "open chrome" in query:
            speak("opening chrome")
            cpath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(cpath)
            time.sleep(3)
    

        elif "close chrome" in query:
            speak("okey.. sir, closing chrome")
            os.system("taskkill /f /im chrome.exe")

        elif "send email" in query:
            mailsend()

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            speak("opening youtube..")
            webbrowser.open("www.youtube.com")
            time.sleep(3)

        elif "open facebook" in query:
            speak("opening facebook..")
            webbrowser.open("www.facebook.com")
            time.sleep(3)

        elif "which wi-fi is connected" in query:
            wifiicon = 1674,1056
            py.click(wifiicon)
            speak("this is your current wifi connected to your machine..")
            time.sleep(2)
            py.click(wifiicon)

        elif "where i am" in query or "where i am right now" in query or "tell me current location" in query:
            location()

        elif "who made you" in query:
            speak("i am developed by python programmer")

        elif "open google" in query:
            speak("sir... what should i serch on google...")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")


        elif "volume up" in query:
            py.press("volumeup")

        elif "volume down" in query:
            py.press("volumedown")

        elif "volume mute" in query or "mute system" in query or "mute" in query:
            py.press("volumemute")

        elif "volume unmute" in query or "unmute system" in query or "unmute" in query:
            py.press("volumemute")
            
        elif " tell me the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"sir the time is {strtime}")

        elif "tell me the latest news" in query:
            speak("please wait sir , fetching the latest news")
            news()

        elif "close the system" in query:
            speak("turn off the machine..")
            os.system("shutdown /s /t 5")

        elif "how are you" in query :
            speak("i am fine sir, what about you.")


        elif "also good" in query or "fine" in query:
            speak("that's great to hear from you")

        elif "open camera" in query:
            speak("opening camera please wait... ")
            winlogo = 27,1055
            py.click(winlogo)
            time.sleep(1)
            a = "camera"
            py.write(a)
            py.press('enter')

        elif "how much battery we left" in query or "how much power we have" in query or "battery" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system have {percentage} percent battery")

        elif "temperature" in query:
            serch = "temprature in rajasthan"
            url = f"https://www.google.com/search?q={serch}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {serch} is {temp}")

        elif "activate how to do mode" in query or "activate how to do mood" in query:
            speak("how to do mod is activated")
            while True:
                speak("pleae tell me what you want to know")
                how = takecommand()
                try:
                    if "exit" in how or "close" in how or "deactivate this mode" in how:
                        speak("okey sir, mode is closed")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir, i am not able to find this")


        elif "you can sleep now" in query or "go to sleep" in query:
            speak("okey sir, i am going to sleep you call me anytime.")
            break


if __name__ == "__main__":
    while True:
        permission = takecommand()
        if "wake up" in permission:
                taskexe()
        elif "goodbye jarvis" in permission or "goodbye" in permission:
            speak("thanks for using me sir, have a good day")
            sys.exit()
