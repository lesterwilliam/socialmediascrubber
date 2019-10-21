# exporting facebook comments with https://socialfy.pw/facebook-export-comments
# place csv-file in original inputs
# eclipse test

import time
import preprocessing as pre
#import getbands as gb

startTime = time.time()

pre.preproc()
pre.getbands()

endTime = time.time()
print("Finished in " + str('{:.3f}'.format(endTime - startTime)) + " seconds.")
