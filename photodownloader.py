from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

dir = "aamir khan images"
loc_for_folder = r"C:\Users\justi\downloads"
path = os.path.join(loc_for_folder, dir)
os.mkdir(path)
os.chdir(path)

page = urlopen('https://www.indiaglitz.com/aamir-khan-photos-hindi-actor-2628998-7950')
soup = BeautifulSoup(urlopen('https://www.indiaglitz.com/aamir-khan-photos-hindi-actor-2628998-7950'))
counter = 0


for img in soup.find_all(title="Aamir Khan"):    #since the images of amir will be given title ,we can find out by inspecting in the page
    with open("image" + str(counter)+".jpg",'wb') as f:   
        f.write(urlopen(img['src']).read())
    counter += 1


