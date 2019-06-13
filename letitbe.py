import numpy,os
from pydub import AudioSegment

def main():
    final_length = 60*1000
    file_base = './samples/'
    audiofiles = [AudioSegment.from_mp3(os.path.join(file_base,str(x)+".mp3")) for x in range(1,5)]
    clip_length = numpy.mean([len(x) for x in audiofiles])
    repititions = int((final_length/clip_length) - 7)
    print("About to loop %s times" % repititions)
    final_audio = audiofiles[0] + audiofiles[1] + audiofiles[2] + audiofiles[3] 
    for rep in range(repititions):
        final_audio = final_audio + audiofiles[numpy.random.randint(0,3)]
    final_audio = final_audio + audiofiles[3]
    final_audio = final_audio + AudioSegment.from_mp3(os.path.join(file_base,"end.mp3"))
    final_audio.export(os.path.join(file_base,"final.mp3"), format="mp3")



if __name__ == '__main__': main()