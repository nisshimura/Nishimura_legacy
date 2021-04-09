import glob 
import os  
import subprocess 
import sys
from pydub import AudioSegment
import pathlib
##HandBrakeでVFRからCFRに変換する
class Tuner():
    ext_dict = {
                'mp4': ['/mp4/', '*.mp4', '.mp4'],
                'mp3': ['/mp3/', '*.mp3', '.mp3'],
                'mts': ['/mts/', '*.mts', '.MTS'],
                'wav': ['/wav/', '*.wav', '.wav'],
                'flac': ['/flac/', '*.flac', '.flac']
                }

    filename = 'C:/Users/ntaka/workspace/jobcan_autotool/code_videoediter'
    def __init__(self):
        os.chdir(pathlib.Path(
            "./ffmpeg/ffmpeg-N-100411-g32586a42da-win64-gpl-shared-vulkan/bin"))
    
    def convert(self, in_ext, out_ext):
        filename = self.filename
        num = os.listdir(pathlib.Path(filename + self.ext_dict[in_ext][0]))
        for index in range(len(num)):
            dir = glob.glob(filename + self.ext_dict[in_ext][0] + self.ext_dict[in_ext][1])
            name = [n.split('.')[0] for n in dir]

        if in_ext == 'mp4' or in_ext == 'mp3':
            for index in name:
                cmd = 'ffmpeg.exe -i \"{0}\"'.format(
                    index) + self.ext_dict[in_ext][2] + ' -r 60 ' + filename + self.ext_dict[out_ext][0] + os.path.basename(index) + self.ext_dict[out_ext][2]
                subprocess.call(cmd)
        else:
            for index in name:
                cmd = 'ffmpeg.exe -i \"{0}\"'.format(
                    index) + self.ext_dict[in_ext][2] + ' -r 60 ' + filename + self.ext_dict[out_ext][0] + os.path.basename(index) + self.ext_dict[out_ext][2]
                subprocess.call(cmd)
#ffmpeg -i input.mp4 -r 60 cfr.mp4
     #
    def wavtoflac(self):
        filename = self.filename
        num = os.listdir(pathlib.Path(filename + self.ext_dict['mp3'][0]))
        for index in range(len(num)):
            dir = glob.glob(
                filename + self.ext_dict['wav'][0] + self.ext_dict['wav'][1])
            name = [n.split('.')[0] for n in dir]

        for index in name:
            song = AudioSegment.from_wav(
                pathlib.Path(filename + self.ext_dict['wav'][0] + os.path.basename(index) + self.ext_dict['wav'][2]))
        
            song.export(filename + self.ext_dict['flac'][0] +
                        os.path.basename(index) + self.ext_dict['flac'][2], format='flac')

def main(in_ext, out_ext):
    Job = Tuner()
    if in_ext == 'mts' and out_ext == 'flac':
        Job.convert('mts','mp4')
        Job.convert('mp4', 'mp3')
        Job.convert('mp3', 'wav')
        Job.wavtoflac()
    elif in_ext == 'mp4' and out_ext == 'flac':
        Job.convert('mp4', 'mp3')
        Job.convert('mp3', 'wav')
        Job.wavtoflac()
    elif in_ext == 'mts' and out_ext == 'mp4':
        Job.convert('mts', 'mp4')
    elif in_ext == 'mp4' and out_ext == 'wav':
        Job.convert('mp4', 'mp3')
        Job.convert('mp3', 'wav')
    else:
        print('CHECK THE CODE')
    
if __name__ == "__main__":
    main('mp4', 'wav')



