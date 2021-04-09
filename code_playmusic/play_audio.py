import pyaudio
import wave

def main():
    wf = wave.open("C:\\\\sound\\fanfare.wav", "rb")

    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True)


    data = wf.readframes(1024)
    while(data != ''):
        stream.write(data)
        data = wf.readframes(1024)
    stream.close()
    p.terminate()



if __name__ == '__main__':
   main()
