import os
import pyttsx3

engine = pyttsx3.init()

if __name__ == "__main__":
    print("Welcome to Robo speaker")
    while True:
        x = input("Enter what you want me to speak: ")
        if x.lower() == "end":
            engine.say("Bye bye sir")
            engine.runAndWait()
            break
        # command = x
        engine.say(x)
        engine.runAndWait()
