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
winsound.Beep(scale['G'], eighthNote)
winsound.Beep(scale['F'], quarterNote)
winsound.Beep(scale['E'], quarterNote)
winsound.Beep(scale['D'], quarterNote)
winsound.Beep(scale['E'], quarterNote)
winsound.Beep(scale['F'], halfNote)
winsound.Beep(scale['C1'], quarterNote)
winsound.Beep(scale['D'], quarterNote)
winsound.Beep(scale['E'], halfNote)
winsound.Beep(scale['D'], quarterNote)
winsound.Beep(scale['E'], quarterNote)
winsound.Beep(scale['F'], halfNote)
winsound.Beep(scale['F'], quarterNote)
winsound.Beep(scale['G'], quarterNote)
winsound.Beep(scale['F'], quarterNote)
winsound.Beep(scale['E'], quarterNote)
winsound.Beep(scale['D'], quarterNote)
winsound.Beep(scale['E'], quarterNote)
winsound.Beep(scale['F'], halfNote)
winsound.Beep(scale['D'], halfNote)
winsound.Beep(scale['G'], halfNote)
winsound.Beep(scale['E'], quarterNote)
winsound.Beep(scale['C1'], halfNote)
