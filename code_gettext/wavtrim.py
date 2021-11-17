from pydub import AudioSegment
import os 
import math
import pathlib
import re 

file_path = './sounds/speech.wav'

root, ext = os.path.split(file_path)
ext = re.sub('.wav', '', ext)

sound = AudioSegment.from_wav(file_path)

for i in range(math.ceil(sound.duration_seconds / 60)):
    out_path = pathlib.Path('./cut_sounds' + '//' + ext + str(i) + '.wav')
    if i == math.ceil(sound.duration_seconds / 60):
        target = sound[60000*i:sound.duration_second*100]
    target = sound[60000*i:60000*(i+1)]
    target.export(out_path, format='wav')

