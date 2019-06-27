# exporting facebook comments with https://socialfy.pw/facebook-export-comments
# place csv-file in original inputs
import pandas as pd
import collections as cl

def file_len(fname):
 with open(fname) as f:
  for i, l in enumerate(f):
   pass
 return i + 1

def getbands():
 print("Start gathering band names.")
 # take file to process from input destination and copy it into filetrain
 file6 = pd.read_csv("filetrain/preprocessing/file5.csv")
 bandList = []
 for i in range (0, file6.shape[0]):
  t = str((file6.at[i,'Message']))
  bandList.append(t)
 output = open("filetrain/output.txt", "w")
 print("Counting bands.")
 for word, cnt in cl.Counter(bandList).most_common():
  s = str((repr(word), '-', cnt)) + "\n"
  output.write(s)
 print("Sorting ", len(bandList), " bands.")
 print(file_len("filetrain/output.txt"), "different bands registred.")
 output.close()

