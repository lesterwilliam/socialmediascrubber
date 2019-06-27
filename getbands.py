# exporting facebook comments with https://socialfy.pw/facebook-export-comments
# place csv-file in original inputs
import pandas as pd

def getbands():
 print("Start gathering band names.")
 # take file to process from input destination and copy it into filetrain
 file6 = pd.read_csv("filetrain/preprocessing/file5.csv")
 bandList = []
 for i in range (0, 30):
  t = str((file6.at[i,'Message']))
  print(t)
  
  found_a_string = False
  for item in bandList:
   if item in t:
    found_a_string = True
  if found_a_string:
   print("Not added.")
  else:
   bandList.append(t)
   print("Added band.")
   
 print(bandList)
 #print(len(bandList))