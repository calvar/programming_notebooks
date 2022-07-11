#Stateful example
current_speaker = None #global variable

def register(name):
    global curent_speaker
    current_speaker = name

def speak(text):
    global current_speaker
    print("[%s] %s" % (current_speaker, text))
    
register("John")
speak("Hello world!")
register("Carlos")
speak("Foobar!")
