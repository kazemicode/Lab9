# Lab 9


def getSnd():
  return makeSound(pickAFile())

      
def changeVolume(sound,n):
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value * n)
   return sound

def copySound(sound):   
  newSound = makeEmptySound(getLength(sound), int(getSamplingRate(sound)))
  for index in range(0, getLength(sound)):
    value = getSampleValueAt(sound, index)
    setSampleValueAt(newSound, index, value)
  changeVolume(newSound, 100)
  explore(newSound)
  #explore(sound)
  return newSound
# Problem 1: clip
def clip(source, start, end):
  target = makeEmptySound(end - start, int(getSamplingRate(source)))
  for index in range(start, end): 
    value = getSampleValueAt(source, index)
    setSampleValueAt(target, index - start, value)
  #changeVolume(target, 100)
  return target

 # Problem 2: copy 
def copy(source, target, start):
  source = clip(source, 0, 23862)
  for index in range(0, getLength(source)): 
    value = getSampleValueAt(source, index)
    setSampleValueAt(target, index + start, value)
  #changeVolume(target, 10)
  explore(target)