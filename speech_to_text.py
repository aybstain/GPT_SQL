#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import speech_recognition as sr
from pydub import AudioSegment

def speech_to_text():

    # Create a recognizer object
    recognizer = sr.Recognizer()

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Speak something...")

        # Adjust the ambient noise level (optional)
        recognizer.adjust_for_ambient_noise(source)

        # Record audio until 3 seconds of silence or a phrase is detected
        audio_data = recognizer.listen(source, timeout=3)

    try:
        # Recognize speech using the Google Speech Recognition API
        text = recognizer.recognize_google(audio_data)
        print(f"Speech recognized: {text}")
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    # Print the recognized speech after recording
    return text
    

