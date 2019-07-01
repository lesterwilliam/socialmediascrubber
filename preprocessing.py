# exporting facebook comments with https://socialfy.pw/facebook-export-comments
# place csv-file in original inputs

import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import numpy as np
import string
import csv
import os
import collections as cl
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

printable = set(string.printable)

def preproc():
 inputFile = pd.read_csv("original inputs/file0.csv")

 # remove unnecessary columns
 keep_col = ['Message']
 file2 = inputFile[keep_col]
 file2['Message'].replace('',np.nan, inplace=True)
 file2.dropna(subset=['Message'], inplace=False)
 file2.to_csv("filetrain/preprocessing/file2.csv", index=False)
 print("Import input file.")
 
 file4 = pd.read_csv("filetrain/preprocessing/file2.csv")
 for i in range (0, file4.shape[0]):
  s = str(file4.at[i,'Message'])
  s = s.lower()
  
  charsToReplace = ['!','?','/','\n','...','   ']
  for ch in charsToReplace:
   if ch in s:
    s = s.replace(ch,',')
  
  charsToReplace = ['ä','Ä']
  for ch in charsToReplace:
   if ch in s:
    s = s.replace(ch,'ae')
  
  charsToReplace = ['ö','Ö']
  for ch in charsToReplace:
   if ch in s:
    s = s.replace(ch,'oe')
  
  charsToReplace = ['ü','Ü']
  for ch in charsToReplace:
   if ch in s:
    s = s.replace(ch,'ue')
  
  charsToReplace = ['ffdp','5fdp']
  for ch in charsToReplace:
   if ch in s:
    s = s.replace(ch,'five finger death punch')
  
  file4.at[i,'Message'] = ''.join(filter(lambda x: x in printable, s))
 file4.to_csv("filetrain/preprocessing/file4.csv", index=False)
 print("Replaced unwanted characters and forced lower case.")
 
 # create new list
 bandList = []
 file5 = pd.read_csv("filetrain/preprocessing/file4.csv")
 for i in range (0, file5.shape[0]):
  s = str((file5.at[i,'Message']))
  bandList.extend(s.split(","))
 print("Split multi-comments.")
 for i in range (0, len(bandList)):
  bandList[i] = bandList[i].strip()
  bandList[i] = bandList[i].rstrip()
 print("Strip unwanted characters.")
 with open("filetrain/preprocessing/file5.csv",'w') as resultFile:
  wr = csv.writer(resultFile, dialect='excel')
  wr.writerow(bandList)
 bandList = [x for x in bandList if x != '']
 for i in range (0, len(bandList)):
  file5.at[i,'Message'] = bandList[i]
 file5.to_csv("filetrain/preprocessing/file5.csv", index=False)
 print("Save file.")


def getbands():
 print("Start gathering band names.")
 # take file to process from input destination and copy it into filetrain
 file6 = pd.read_csv("filetrain/preprocessing/file5.csv")
 bandList = []
 bandCounts = []
 
 workload = 500#file6.shape[0]
 
 for i in range (0, workload):
  #t = str((file6.at[i,'Message']))
  bandList.append(str((file6.at[i,'Message'])))
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
   if fuzz.partial_ratio(betterBandList[i], betterBandList[j]) > 80:
    bandCounts[i] = bandCounts[i] + bandCounts[j]
    bandCounts[j] = 0
    betterBandList[j] = 'thisbandhasbeenmerged'
   progress = progress + 1
   itterationCount = int(workload*workload/2)
   progPerc = progress / (itterationCount/100)
   if progress % 1000 == 0:
    print("Progress: " + str('{:.2f}'.format((progPerc))) + "% \t(" + str(progress) + "/" + str(itterationCount) + ")")
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
