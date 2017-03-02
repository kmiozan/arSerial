import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:                # use the default microphone as the audio source

    while True:
        print("dinliyorum...")
        audio = r.listen(source, timeout=1, phrase_time_limit=4)                   # listen for the first phrase and extract it into audio data

        try:
            print("Ses taniniyor...")
            print("You said " + r.recognize_google(audio, language="tr-TR"))  # recognize speech using Google Speech Recognition
        except LookupError:  # speech is unintelligible
            print("Could not understand audio")
