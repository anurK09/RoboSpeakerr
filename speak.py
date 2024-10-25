import pyttsx3
if __name__=='__main__':
    print("Welcome to RoboSpeaker 0.1 Created by Anu !!")
    while True:
        x=input("Enter what you want me to pronounce: ")
        if x == "quit":
            
            break
        command=pyttsx3.init()
        command.setProperty('rate',150)
        command.say(x)
        command.runAndWait()