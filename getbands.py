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
 
 workload = file6.shape[0]
 
 for i in range (0, workload):
  t = str((file6.at[i,'Message']))
  bandList.append(t)
  bandCounts.append(0)
 
 preoutput = open("filetrain/preoutput.txt", "w")
 print("Counting bands.")
 counter = 0
 newBandList = bandList
 for word, cnt in cl.Counter(bandList).most_common():
  s = str((repr(word), '-', cnt)) + "\n"
  newBandList[counter] = repr(word)
  bandCounts[counter] = cnt
  counter = counter + 1
  preoutput.write(s)
 print("Sorting ", len(bandList), " bands.")
 preoutput.close()
 
 progress = 0
 betterBandList = bandList
 for i in range (0, len(betterBandList)):
  for j in range (i+1, len(betterBandList)):
   progress = progress + 1
   itterationCount = int(workload*workload/2)
   progPerc = progress / (itterationCount/100)
   if progress % 1000 == 0:
    print("Progress: " + str('{:.2f}'.format((progPerc))) + "% \t(" + str(progress) + "/" + str(itterationCount) + ")")
   if fuzz.partial_ratio(betterBandList[i], betterBandList[j]) > 80:
    betterBandList[j] = betterBandList[i]
    bandCounts[i] = bandCounts[i] + bandCounts[j]
    bandCounts[j] = 0
    #betterBandList[j] = str(betterBandList[j]) + 'thisbandhasbeenmerged'
    betterBandList[j] = 'thisbandhasbeenmerged'
 bandList = betterBandList
 
 print("Done with fuzzy part.")
 
 # Bubble sort algorythm
 for i in range (0, len(betterBandList)):
  for j in range (i+1, len(betterBandList)):
   if bandCounts[i] < bandCounts[j]:
    tempBand = bandList[i]
    tempCount = bandCounts[i]
    bandList[i] = bandList[j]
    bandCounts[i] = bandCounts[j]
    bandList[j] = tempBand
    bandCounts[j] = tempCount
 
 print("\nDone sorting list.")
 
 output = open("filetrain/output.txt", "w")
 for i in range(len(bandList)):
  s = str(bandCounts[i]) + "\t" + str(bandList[i])[1:-1] + "\n"
  output.write(s)
 print("Sorting ", len(bandList), " bands.")
 output.close()
 
 showBands = 10
 print("\nThe top " + str(showBands) + " bands are:\n") 
 for i in range(showBands):
  print(str(betterBandList[i])[1:-1], bandCounts[i])
 print("\nWorkload:\t" + str(workload))