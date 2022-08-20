from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr
recog=sr.Recognizer()

def soundAndAnalysis():
    with sr.Microphone() as source:
        print("Starting")
        # Supressing background noice
        recog.adjust_for_ambient_noise(source)
        print("Recording")
        # Recording
        recorded = recog.listen(source)
        print("Recorded")

    try:
        text = recog.recognize_google(recorded, language="en-US")
        print("The recorded sentence is: ","'",text,"'")
    except Exception as e:
        print(e)

    sentence = [str(text)]
    analyzer = SentimentIntensityAnalyzer()
    return sentence,analyzer




