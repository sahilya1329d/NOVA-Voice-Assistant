from speech import speak, listen
from command import process_command



speak("Hello, I am Nova. How can I help you?")

while True:

    command = listen()

    if command == "":
        continue

    if "exit" in command.lower():
        speak("thanks! call me anytime if you need help ")
        break

    process_command(command)