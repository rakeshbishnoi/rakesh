import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source,duration=5)
    r.dynamic_energy_threshold=True
    print("say something please!!")
    audio = r.listen(source)


try:
    print("you said: "+r.recognize_google(audio))
except sr.unknownValueError:
    print("Google speech Recogniyion Could not understand audio")
except sr.RequestError as e:
    print("could not request results from google speech Recognition service; {0}".form)
