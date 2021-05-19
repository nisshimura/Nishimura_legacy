import speech_recognition as sr 
import os 

r = sr.Recognizer()
file_path = './cut_sounds/'

ALL_text = ''

for i in os.listdir(file_path):
    with sr.AudioFile(file_path + str(i)) as source:
        audio = r.listen(source)

        try:

            # using google speech recognition
            text = r.recognize_google(audio, language='ja-JP')
            ALL_text += text

        except:
            print('Sorry.. run again...')

print(ALL_text)