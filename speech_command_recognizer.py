import speech_recognition as sr

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio)
        return command.lower()
    except sr.UnknownValueError:
        return "Could not understand audio."
    except sr.RequestError as e:
        return f"Recognition error: {e}"

if __name__ == "__main__":
    print("Say a command (e.g., 'start', 'stop', 'exit'):")
    command = listen_for_command()
    print("Recognized Command:", command)

    # Basic action based on recognized command
    if "start" in command:
        print("Starting the process...")
    elif "stop" in command:
        print("Stopping the process...")
    elif "exit" in command:
        print("Exiting...")
    else:
        print("Command not recognized.")
