from pydub import AudioSegment
import audioop

FILENAME = "spookyscaryskeletons.mp3"
CUTOFF = 400 # RECOMMENDED: 400
THRESHOLD = 4000 # RECOMMENDED: 2000-4000

AudioSegment.converter = "C:\\tools\\ffmpeg\\bin\\ffmpeg.exe" # FFMPEG path
a = AudioSegment.from_mp3(FILENAME) # FILENAME

a = a.low_pass_filter(CUTOFF)

raw_data = a._data

rms = []
INTERVAL = 8820 # assume 44100 samples per second
for i in xrange(len(raw_data)/INTERVAL):
    rms.append(audioop.rms(raw_data[INTERVAL*i:INTERVAL*(i+1)],2))
rms.append(audioop.rms(raw_data[INTERVAL*(i+1):],2))

##for data in rms:
##    print data

diff = [j-i for i,j in zip(rms[:-1], rms[1:])]
diff.append(0)

index = 0
triggers = []

for e in diff:
    # print e
    if e > THRESHOLD:
        triggers.append(index)
    index += 1

print "length:", len(diff) # DIFFLENGTH
print "# triggers:", len(triggers) # TRIGGERSLENGTH
print "time:", a.duration_seconds
print "triggers/sec:", len(triggers)/a.duration_seconds
print triggers
