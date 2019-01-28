import os
import random
import sys
import wget
import datetime
import time 

# Config elements -> TODO: Move to/load from Config file
collections = { 
                'abstract': 789734,
                'aerials': 1166960,
                'autumn': 311028,
                'beach': 329879,
                'castles': 3112387,
                'earth_from_above': 162468,
                'gradients': 540518,
                'landscape': 827743,
                'long_exposure': 162213,
                'pyro': 1254524,
                'winter': 3178572,
                'sea_life': 1262111,
                'micro_worlds': 573009,
                'minimal_1': 325867,
                'rain': 1410320,
                'neon': 2411320,
                'milkyway': 1538150,
                'slice_of_sky': 2203755,
                'nature_1': 357786,
                'sand': 997,
                'flood': 869015,
                'waves': 794627,
                'waves_2': 3811774,
                'tropical': 173355,
                'tropical_2': 1127861,
                'mountians': 452289,
                'mountains_2': 2292472,
                'future': 1460022,
                'stars': 795671,
                'space': 1111575,
              }
rez = '1920x1080'

# Default values and temp variables 
maxNumPhotos = 15
minNumPhotos = 6
currNumberOfPhotos = 0

# Limit the number of photos to the max value

while currNumberOfPhotos < minNumPhotos  and currNumberOfPhotos < maxNumPhotos:

  # Chose the collection
  collection_name = random.sample(collections.keys(), 1)[0]
  collection_value = collections[collection_name]

  # Write to log file
  now = datetime.datetime.now()
  f = open('./collection_key_log.txt', 'a')
  f.write(now.strftime('%m/%d/%Y @ %H:%M') + ': Collection "' + collection_name + '" selected' + '\n')
  f.close()
  
  # Create picture directory if it does not exist
  if not os.path.exists('./pics'):
    os.makedirs('./pics')

  # Replace old photos with photos from the new collection
  for x in range(maxNumPhotos):
    if os.path.exists('./pics/pic' + str((x + 1)) + '.jpeg'):
      os.unlink('./pics/pic' + str((x + 1)) + '.jpeg')

    url = 'https://source.unsplash.com/collection/' + str(collection_value) + '/'+ rez +'.jpeg'
    filename = wget.download(url, out = "./pics/pic" + str((x + 1)) + ".jpeg")
    currNumberOfPhotos = currNumberOfPhotos + 1
    # Wait 3 seconds between getting new photos to prevent downloading cashed duplicates
    time.sleep(3)
    print('')
  
  # Compare size of pictures to prevent duplicates. 
  sizeCheckList = []
  for x in range(maxNumPhotos):
    size = os.path.getsize('./pics/pic' + str((x + 1)) + '.jpeg')
    if size in sizeCheckList:
      os.unlink('./pics/pic' + str((x + 1)) + '.jpeg')
      currNumberOfPhotos = currNumberOfPhotos - 1
    sizeCheckList.append(size)
