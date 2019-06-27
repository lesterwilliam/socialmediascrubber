# exporting facebook comments with https://socialfy.pw/facebook-export-comments
# place csv-file in original inputs

import pandas as pd
import numpy as np
import string
import csv
import os

printable = set(string.printable)

def preproc():
 # take file to process from input destination and copy it into filetrain
 inputFile = pd.read_csv("original inputs/file0.csv")
 file1 = inputFile
 file1.to_csv("filetrain/preprocessing/file1.csv", index=False)

 # remove unnecessary columns
 keep_col = ['Message']
 file2 = file1[keep_col]
 file2.to_csv("filetrain/preprocessing/file2.csv", index=False)

 # remove unnecessary rows
 file3 = file2
 file3['Message'].replace('',np.nan, inplace=True)
 file3.dropna(subset=['Message'], inplace=False)
 file3.to_csv("filetrain/preprocessing/file3.csv", index=False)

 # remove unwanted characters
 file4 = file3
 for i in range (0, file4.shape[0]):
  s = str((file4.at[i,'Message']))
  charsToReplace = ['!','?','/','\n']
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
  s = ''.join(filter(lambda x: x in printable, s))
  file4.at[i,'Message'] = s.lower()
 file4.to_csv("filetrain/preprocessing/file4.csv", index=False)
 
 # create new list
 bandList = []
 file5 = file4
 for i in range (0, file4.shape[0]):
  s = str((file4.at[i,'Message']))
  bandList.extend(s.split(","))
  #print(bandList[i])
 for i in range (0, len(bandList)):
  bandList[i] = bandList[i].strip()
  bandList[i] = bandList[i].rstrip()
  #print(bandList[i])
 with open("filetrain/preprocessing/file5.csv",'w') as resultFile:
  wr = csv.writer(resultFile, dialect='excel')
  wr.writerow(bandList)
 print("\nPreprocessing done.")
 bandList = [x for x in bandList if x != '']
 for i in range (0, len(bandList)):
  file5.at[i,'Message'] = bandList[i]
 file5.to_csv("filetrain/preprocessing/file5.csv", index=False)
 
 file6 = file5
 for i in range (0, file6.shape[0]):
  if file6.at[i,'Message']:
   file6.at[i,'Message'] = file6.at[i,'Message']
  if not file6.at[i,'Message']:
   file6.at[i,'Message'] = file6.at[i+1,'Message']
   file6.at[i+1,'Message'] = ''
 file6.to_csv("filetrain/preprocessing/file6.csv", index=False)


# file6 ist langsam brauchbar
# nächste schritte:
# gleiche strings mit erhöhter anzahlt (schwellwerte) zählen und speichern
# daraus liste aus beliebten namen erstellen
# via fuzzywords gesamte vorkommnisse dieser namen abchecken