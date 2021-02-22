import requests
import os

path = os.getcwd()

os.mkdir(path+"/Naruto_Shippuden")

##Enter the Starting episode number
episodeStartNumber = 389

##Enter the End episode number
episodeEndNumber = 500

for episodeNumber in range(episodeStartNumber, episodeEndNumber+1):
    
    ## URL constructed to point the episodes ( some episodes may not be available )
    url = f"http://nt.manga47.net/Naruto_Shippuuden_Dub/{episodeNumber}.mp4"
    print(url)
    response = requests.get(url, stream=True)
    
    fileName = "Naruto_Shipudden " + url.split('/')[-1]
    
    with open("Naruto_shippuden/"+fileName,'wb') as downloadFile:
        
        for i in response.iter_content(chunk_size = 1024*1024):
            if i:
                print("writing...")
                downloadFile.write(i)
            
    print(fileName + " downloaded")
