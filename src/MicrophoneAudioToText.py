import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Talk")
    r.adjust_for_ambient_noise(source)
    audio_text = r.listen(source)
    print("Time over, thanks edede")

    try:
        print("Text: "+r.recognize_google(audio_text, language='cs'))
    except:
        print("Sorry, I did not get that")











