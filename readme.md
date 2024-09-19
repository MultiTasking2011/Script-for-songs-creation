To use this script, you have to upload a midi file with the basic tune as treble and the chords as bass cleff
Using infmidi

What it should be
Idea 1:
First there will be inputs in the python script that will display the different parts of the song and will take an input t or f which will indicate their presence. t means yes, f means no they should not be created;
Beginning 1:
Beginning mid 1:
Prechorus:
Chorus:
Chorus super:
Chorus end:
Beginning 2:
Beginning mid 2:
Prechorus:
Chorus:
Chorus Super:
Chorus end:
Bridge:
Beginning 3:
Beginning mid 3:
Prechorus:
Chorus:
Chorus super:
Chorus end:
End:
End real:
Chorus super means a more hard chorus, Beginnind mid means if there is a second paragraph to the beginning, and the intensity of beginning mid is higher that means there are more notes. End real is basically the beginning mid of the end.
You'll have to provide a midi file for each of the things you marked true with the exact same name, along with a "bass cleff" and a "treble cleff" in a folder named "resources".
Then there will be another input known as impossibility which will have 1, 2, 3 on it. 1 means least, 2 means mid and 3 means super.
Finally, there will be another input that specifies files not to edit and overlap regularly. this means that the treble and bass cleff files will be overlapped without any editing in either of them. Here, in this input, you will have to specify which all files are not to be edited.

Actual code thats supposed to be there:
First, each of the midi files will be converted into abc music notation files. The beginnings will be less intense, the beginnings mid will be slightly more intense, the prechorus will be slightly more intense as the beginnings mid and the chorus will be most intense. But, super chorus will be completely impossible to play. Chorus end will be as intense as prechorus. End will be as intense as beginning and end real will be very slow. each different type of track will be a different abc file. in the end, the files will be transformed into midi and get combined and overlapped into one output file. 

Idea 2:
More advanced to code btw
Enter treble cleff notes and make a script that checks for each note in treble cleff and the scale it's in, based on that it makes chords for bass cleff, it asks how many notes per chord, octave chords or regular chords and if you want to arpeggiate the chords, if yes in what count
then it will make double octaves for treble notes, and duets for treble notes using the scals, it will mke bass notes every 4 counts and chords the rest of the 3 counts, and in the start it will ask the time signature and the tempo
More covenient, easier and faster to use, full automation possible but extremely timetaking to code
Add a feature where humming can be turned to midi, to make it more covenient rather than to record midi on producer thing and then input it into the thing