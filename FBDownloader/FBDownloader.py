import pandas as pd
import json
import requests
import os
import time
import datetime

# source = full path (double back slashed) to the "photos.json" file created in the InitialPull
# dump = the folder location into which you'd like to dump the image files

def fbdownloader(source,dump):
    df = pd.read_json(source)
    os.chdir(dump)
    # JSON to JPEG
    for i, row in df.iterrows():
        url = df['cdn_url'].iloc[i]
        filename = str(df['filename'].iloc[i])
        r = requests.get(url, allow_redirects=True)
        open(filename, 'wb').write(r.content)
    # Replace modified date with df['timestamp']
    for filename in os.listdir(dump):
        year = int(filename[:4])
        if int(filename[5]) == 0:
            month = int(filename[6])
        else:
            month = int(filename[5:7])
        if int(filename[8]) == 0:
            day = int(filename[9])
        else:
            day = int(filename[8:10])
    
        hour = 0#int(filename[11:13])
        minute = 0#int(filename[13:15])
        second = 0#int(filename[15:17])
        date = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
        modTime = time.mktime(date.timetuple())

        os.utime(dump+'\\'+filename, (modTime, modTime))

fbdownloader('#C:\\Source\\insert-path-to\\photos.json' , #'C:\\insert-path-to\\Dump\\')
