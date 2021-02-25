import requests
import os
import sys
from rich.progress import (
    BarColumn,
    DownloadColumn,
    TextColumn,
    TransferSpeedColumn,
    TimeRemainingColumn,
    Progress,
    TaskID,
    track
)
from rich import print

path = os.path.dirname(__file__)


try:
    os.mkdir(path+"/Naruto_Shippuden")
except:
    print('folder found!')

episodeStartNumber = 388

prog = Progress(
    BarColumn(bar_width=30),
    "[progress.percentage]{task.percentage:>3.1f}%",
    "•",
    DownloadColumn(),
    "•",
    TimeRemainingColumn(),
)

for episodeNumber in range(episodeStartNumber, 501):
    url = f"http://nt.manga47.net/Naruto_Shippuuden_Dub/{episodeNumber}.mp4"

    print(url)

    response = requests.get(url, stream=True)
    
    fileName = "Naruto_Shipudden_" + url.split('/')[-1]

    contentLength = int(response.headers['Content-length'])

    taskId = prog.add_task("download", total=contentLength)
    
    with open(path+"/Naruto_Shippuden/"+fileName,'wb') as downloadFile:
        prog.start()
        for i in response.iter_content(chunk_size = 512):
            if i:
                downloadFile.write(i)
                prog.update(taskId, advance = len(i))
            
    print(fileName + " downloaded")



