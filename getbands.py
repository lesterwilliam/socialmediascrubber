# exporting facebook comments with https://socialfy.pw/facebook-export-comments
# place csv-file in original inputs
import pandas as pd
import collections as cl
import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def getbands():
 print("Start gathering band names.")
 # take file to process from input destination and copy it into filetrain
 file6 = pd.read_csv("filetrain/preprocessing/file5.csv")
 bandList = []
 bandCounts = []
 
 workload = 500
 
 #for i in range (0, file6.shape[0]):
 for i in range (0, workload):
  t = str((file6.at[i,'Message']))
  bandList.append(t)
  bandCounts.append(0)
 
 output = open("filetrain/output.txt", "w")
 print("Counting bands.")
 counter = 0
 newBandList = bandList
 for word, cnt in cl.Counter(bandList).most_common():
  s = str((repr(word), '-', cnt)) + "\n"
  newBandList[counter] = repr(word)
  bandCounts[counter] = cnt
  counter = counter + 1
  output.write(s)
 print("Sorting ", len(bandList), " bands.")
 output.close()
 
 progress = 0
 betterBandList = bandList
 for i in range (0, len(betterBandList)):
  for j in range (i+1, len(betterBandList)):
   progress = progress + 1
   print("Progress: " + str(progress / (workload*workload/200)) + "%")
   if fuzz.partial_ratio(betterBandList[i], betterBandList[j]) > 70:
    betterBandList[j] = betterBandList[i]
    bandCounts[i] = bandCounts[i] + bandCounts[j]
    bandCounts[j] = 0
    betterBandList[j] = str(betterBandList[j]) + 'thisbandhasbeenmerged'
 bandList = betterBandList
 
 for i in range (0, len(betterBandList)):
  for j in range (i+1, len(betterBandList)):
   if bandCounts[i] < bandCounts[j]:
    tempBand = bandList[i]
    tempCount = bandCounts[i]
    bandList[i] = bandList[j]
    bandCounts[i] = bandCounts[j]
    bandList[j] = tempBand
    bandCounts[j] = tempCount
    
 
 
 
 for i in range(50):
  print(betterBandList[i], bandCounts[i])