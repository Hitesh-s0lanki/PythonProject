import pyttsx3

text_converted=pyttsx3.init()
text=input("Enter what you want in speech\n")
text_converted.say(text)
text_converted.runAndWait()