import os
import random
import sys
import wget
import datetime
import time 
import yaml

# Load config file
config_file = open('config.yml', 'r')
config = yaml.load(config_file)
config_file.close()

current_number_of_photos = 0

while current_number_of_photos < config['min_number_of_photos']:

  # Chose the collection
  collection_name = random.sample(config['collections'].keys(), 1)[0]
  collection_value = config['collections'][collection_name]

  # Write to log file
  now = datetime.datetime.now()
  f = open('./collection_key_log.txt', 'a')
  f.write(now.strftime('%m/%d/%Y @ %H:%M') + ': Collection "' + collection_name + '" selected' + '\n')
  f.close()
  
  # Create picture directory if it does not exist
  if not os.path.exists('./pics'):
    os.makedirs('./pics')

  # Replace old photos with photos from the new collection
  for x in range(config['max_number_of_photos']):
    if os.path.exists('./pics/pic' + str((x + 1)) + '.jpeg'):
      os.unlink('./pics/pic' + str((x + 1)) + '.jpeg')

    url = 'https://source.unsplash.com/collection/' + str(collection_value) + '/' + config['resolution'] + '.jpeg'
    filename = wget.download(url, out = "./pics/pic" + str((x + 1)) + ".jpeg")
    current_number_of_photos = current_number_of_photos + 1
    # Wait 3 seconds between getting new photos to prevent downloading cashed duplicates
    time.sleep(3)
    print('')
  
  # Compare size of pictures to prevent duplicates. 
  sizeCheckList = []
  for x in range(config['max_number_of_photos']):
    size = os.path.getsize('./pics/pic' + str((x + 1)) + '.jpeg')
    if size in sizeCheckList:
      os.unlink('./pics/pic' + str((x + 1)) + '.jpeg')
      current_number_of_photos = current_number_of_photos - 1
    sizeCheckList.append(size)
