# exporting facebook comments with https://socialfy.pw/facebook-export-comments
# place csv-file in program directory

import pandas as pd

df = pd.read_csv("comments_10157361185048044.csv")

#print (df.head(n=5))
#print (df.describe())
#print (df.Comments.head())
print (df.loc[0:500,['Message','Likes']])