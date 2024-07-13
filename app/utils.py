import speech_recognition as sr
from pydub import AudioSegment

def convert_audio_to_text(audio_file_path):
    recognizer = sr.Recognizer()
    audio = AudioSegment.from_file(audio_file_path)
    audio.export("temp.wav", format="wav")

    with sr.AudioFile("temp.wav") as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    return text

    import random
import speech_recognition as sr
from pydub import AudioSegment

def convert_audio_to_text(audio_file_path):
    recognizer = sr.Recognizer()
    audio = AudioSegment.from_file(audio_file_path)
    audio.export("temp.wav", format="wav")

    with sr.AudioFile("temp.wav") as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    return text

def convert_to_funny_statement(text):
    statements = [
        "Why did the chicken cross the road? To learn about {}!".format(text),
        "Knock knock. Who's there? {}. {} who? Just {}!".format(text, text, text),
    ]
    return random.choice(statements)

def convert_to_simple_code(text):
    return "print('{}')".format(text)

def convert_to_song(text):
    return "Twinkle, twinkle, little {}, How I wonder what you {}.".format(text, text)

def convert_to_story(text):
    return "Once upon a time, there was a {} who loved to {}.".format(text, text)

def convert_to_rhyme(text):
    return "{} in a boat, trying to stay afloat.".format(text)

