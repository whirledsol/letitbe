import numpy,os
from pydub import AudioSegment
import argparse

def main():


    parser = argparse.ArgumentParser(description='Let it Be.',add_help=True)
    parser.add_argument('-d','--duration',action='store',dest='final_length',type=int,default=1,help='duration in minutes')
    parser.add_argument('-f','--faster',action='store_true',dest='faster_mode',default=False,help='mode to increase speed over time')
    args = parser.parse_args()

    final_length = args.final_length*60*1000
    crossfade=50
    faster_increase=15
    file_base = './samples/'
    audiofiles = [AudioSegment.from_mp3(os.path.join(file_base,str(x)+".mp3")) for x in range(1,5)]
    clip_length = numpy.mean([len(x) for x in audiofiles])
    min_clip_length = numpy.min([len(x) for x in audiofiles])
    repititions = int((final_length/clip_length) - 7)
    print("About to loop %s times" % repititions)
    final_audio = audiofiles[0] + audiofiles[1] + audiofiles[2] + audiofiles[3] 
    i=3
    for rep in range(repititions):
        i = numpy.random.choice([x for x in range(0,4) if x != i])
        final_audio = final_audio.append(audiofiles[i],crossfade=crossfade)
        if args.faster_mode and (crossfade + faster_increase) < min_clip_length:
            crossfade = crossfade + faster_increase
    final_audio = final_audio.append(audiofiles[3],crossfade=crossfade)
    final_audio = final_audio.append(AudioSegment.from_mp3(os.path.join(file_base,"end.mp3")),crossfade=50)
    final_audio.export(os.path.join(file_base,"final.mp3"), format="mp3")


if __name__ == '__main__': main()
