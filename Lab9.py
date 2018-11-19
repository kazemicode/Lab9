# Sara Kazemi
# CST 205
# Lab 9

# Run the main method and load the wav files in the input folder
# Use the order specified, 0-4.
def main():
  
  # Assemble all sounds for the collage
  target = blend(getSnd(), getSnd(), 0) # blend song and main clip together
  johnny = clip(getSnd(), 35113, 47012) # Get clip of Johnny Mneumonic saying "computer"
  scotty = clip(getSnd(), 4688, 10224)  # Get clip of Scotty saying "computer"
  error = clip(getSnd(), 0, 10000)      # Get clip of "There was an error"

  # Keys are the sounds to dub over in the target clip
  # Values are where (sample) to begin dubbing over in the target clip
  soundDict = {
   johnny : 46536,
   scotty : 61399,
   error: 167735
   }
  
  # Create and write collage to file
  collage = soundCollage(soundDict, target)
  maxVolume(collage)
  explore(collage)
  writeSound(collage, "/collage.wav")
  
  reverse = reverseSound(collage)
  writeSound(reverse, "/reverseCollage.wav")

##############################################################################     
# getSnd()  
# Returns a Sound object given a file path
def getSnd():
  return makeSound(pickAFile())

##############################################################################     
# writeSound(sound, name)
# Writes a Sound to  file  
def writeSound(sound,name):
  file=getMediaPath(name)
  writeSoundTo(sound,file)


##############################################################################          
# maxSample(sound)
# Finds a multiplier that will give us the loudest volume 
# that we can get based on a maximum sound sample and then boosts 
# the sound values by that amount. 
def maxSample(sound):
  largest = 0
  for sample in getSamples(sound):
    largest = max(largest,getSampleValue(sample))
  return largest
  
  
##############################################################################     
# maxVolume(sound)
# increases the volume of each sample by the factor 
# (factor=float(maxPossibleSampleValue)/largest)
# where largest is the value returned by your maxSample function.
def maxVolume(sound):
  print "Applying normalization on: ", sound
  largest = maxSample(sound)
  factor = 127.0/largest # highest value in 8 bit depth is 127
  print "Largest sample value in original sound was: ", largest
  print "Multiplying by a factor of: ", factor
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSample(sample, value * factor) 
  return sound
  
##############################################################################       
# copySound(sound)
# Makes a direct copy of a sound into a new Sound object
def copySound(sound):   
  newSound = makeEmptySound(getLength(sound), int(getSamplingRate(sound)))
  for index in range(0, getLength(sound)):
    value = getSampleValueAt(sound, index)
    setSampleValueAt(newSound, index, value)
  changeVolume(newSound, 100)
  explore(newSound)
  #explore(sound)
  return newSound
 
##############################################################################     
# blend(sound1, sound2, start)   
# EXPERIMENTAL:
# Blends two sounds together at the sample specified by start
# so you can hear both sounds at the same time
def blend(sound1, sound2, start):
  #print start, getLength(sound1)
  #canvas = makeEmptySound(getLength(sound1), int(getSamplingRate(sound1)))
  for index in range(start, start + getLength(sound2)):
    if index < getLength(sound1):
      #print index
      newSample = getSampleValueAt(sound1, index) * 0.5 + getSampleValueAt(sound2, index - start) * 0.5
      setSampleValueAt(sound1, index, newSample) 
  return sound1
    
##############################################################################      
# Problem 1: clip
# Clip the source sound at start sample to end sample
# Return clipped sound
def clip(source, start, end):
  target = makeEmptySound(end - start, int(getSamplingRate(source)))
  for index in range(start, end): 
    if index < getLength(source):
      value = getSampleValueAt(source, index)
      setSampleValueAt(target, index - start, value)
  return target

##############################################################################     
# Problem 2: copy 
# Copy a source sound to the target sound at the start sample
# Return resulting sound
def copy(source, target, start):
  source = clip(source, 0, 10000)
  for index in range(0, getLength(source)): 
    value = getSampleValueAt(source, index)
    setSampleValueAt(target, index + start, value)
  return target
  
# Problem 3: soundCollage
# Uses copy function to copy sounds to the  target
# at specifying start points.
# Sounds are clipped in main method using the clip method
# before being copied.
def soundCollage(soundDictionary, target):
  for sound in soundDictionary:
    print sound
    copy(sound, target, soundDictionary[sound])

  #explore(target)
  return target
  
# Problem 4: reverseSound
# Takes a source sound, creates an empty sound of the same length
# Then, copies the samples from the source in reverse to this new target sound
# The reversed sound is returned
def reverseSound(source):
  length = getLength(source)
  target = makeEmptySound(length, int(getSamplingRate(source)))
  for index in range(1, length):
    value = getSampleValueAt(source, length - index)
    setSampleValueAt(target, index, value)
  # normalize volume
  maxVolume(target)
  return target
  
