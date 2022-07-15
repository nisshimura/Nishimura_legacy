num = "1110010011010010101101001010110010110010110011001100110011001100"
audio_data = num[8:56]
audio2 = ""
for i in range(0,48,2):
    x = int(audio_data[i])^int(audio_data[i+1])
    audio2=audio2+str(x)

print(audio2)

audio2_reverse = audio2[::-1]
print(audio2_reverse)
audio2_reverse = str(bin(int(audio2_reverse,2)-1))
print(audio2_reverse)



