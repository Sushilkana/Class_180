from tkinter import*
import speech_recognition as sr

root = Tk()
root.title("Speech to Text || Class 180")
root.geometry("500x500")
root.configure(bg="lightgreen")

def r_audio():
    speech_recognition = sr.Recognizer()
    with sr.Microphone() as source:
        audio = speech_recognition.listen(source)
        voice = ""
    try:
        voice = speech_recognition.recognize_google(audio,language='en-in')
    except sr.UnknownValueError:
        print("Sorry, please say that can I didn't got that..")
    print(voice)

r_audio()
root.mainloop()