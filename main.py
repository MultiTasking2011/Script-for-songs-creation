import infmidi
from infmidi import *

class scriptdetection():
    def __init__(self) -> None:
        self.timesignature = float()
        self.tempo = int()
        self.arpeggiation = bool()
        self.octavechords = bool()
        self.arpeggiationtempo = int()
        self.notesperchord = int()
        self.treblenotesinput = list()
        self.scalepertreblenote = list() #find
        self.bassnotes = list() #create
        self.duetsinchorus = bool()
        self.basseffect = int()
        self.basseffectchords = int()
        
    def findscale(self):
        pass
    
    def createchords(self):
        pass
    
    def arpeggiationfunc(self):
        pass
    
    def doubleoctavetreble(self):
        pass
    
    def sectionslicing(self):
        pass
        #to differentiate the chorus, prechorus n all