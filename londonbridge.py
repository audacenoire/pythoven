import winsound

wholeNote = 2000
halfNote = 1000
quarterNote = 500
eighthNote = 250
 
scale = {'C1': 261,
         'D': 293,
         'E': 329,
         'F': 349,
         'G': 391,
         'A': 440,
         'B': 493,
         'C2': 523
         }
          
winsound.Beep(scale['F'], quarterNote)
