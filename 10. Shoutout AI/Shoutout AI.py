import pyttsx3
print("\nWelcome to Shoutout AI!!!")
TotalNo = int(input("\nPlease Enter the No of Shouts you want to Give: "))
print()
NameOfPeople = []
for i in range(TotalNo):
    People = input(f"Please Enter the name for shoutout {i+1} : ")
    NameOfPeople.append(People)

Speak = pyttsx3.init()
voices = Speak.getProperty('voices')
Speak.setProperty('voice', voices[1].id)
Speak.setProperty('rate', 150)
for Names in NameOfPeople:
    Speak.say(f"Shout out to {Names}")
    Speak.runAndWait()