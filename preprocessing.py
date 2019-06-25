# exporting facebook comments with https://socialfy.pw/facebook-export-comments
# place csv-file in program directory

import pandas as pd
import string

printable = set(string.printable)

df = pd.read_csv("comments_10157361185048044.csv")


#print (df.head(n=5))
#print (df.describe())
#print (df.Comments.head())
#print (df.loc[0:500,['Message','Likes']])
#print (df.at[1,'Message'])
#s = (df.at[1,'Message'])
#print (s.replace('?',''))
#print (s.translate({ord(i): None for i in 'Rms'}))
#print (filter(lambda x: x in printable, s))

# remove empty columns
df.dropna(axis=1, how='all', inplace=False)

# drop rows with empty cells
df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

for i in range (1, 30):
 s = (df.at[i,'Message'])
 #if s != '':
 print (s.translate({ord(w): None for w in '!?'}))
 #print (s.encode('ascii',errors='ignore'))