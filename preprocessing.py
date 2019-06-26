# exporting facebook comments with https://socialfy.pw/facebook-export-comments
# place csv-file in original inputs

import pandas as pd
import numpy as np
import string

printable = set(string.printable)

# function to remove non-ASCII
def remove_non_ascii(text):
 return ''.join(i for i in text if ord(i) < 128)
 #return text.replace(

# take file to process from input destination and copy it into filetrain
inputFile = pd.read_csv("original inputs/file0.csv")
file1 = inputFile
file1.to_csv("filetrain/file1.csv", index=False)

# remove unnecessary columns
keep_col = ['Message','Likes','Comments']
file2 = file1[keep_col]
file2.to_csv("filetrain/file2.csv", index=False)

# remove unnecessary rows
file3 = file2
file3['Message'].replace('',np.nan, inplace=True)
file3.dropna(subset=['Message'], inplace=False)
file3.to_csv("filetrain/file3.csv", index=False)

# remove unwanted characters
file4 = file3
for i in range (0, file4.shape[0]):
 s = str((file4.at[i,'Message']))
 s = ''.join(filter(lambda x: x in printable, s))
 charsToReplace = ['!','?','/']
 for ch in charsToReplace:
  if ch in s:
   s = s.replace(ch,' ')
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
 print(s)
 file4.at[i,'Message'] = s
file4.to_csv("filetrain/file4.csv", index=False)

















