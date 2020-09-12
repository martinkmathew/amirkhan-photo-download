from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

page = urlopen('https://www.indiaglitz.com/aamir-khan-photos-hindi-actor-2628998-7950')
soup = BeautifulSoup(urlopen('https://www.indiaglitz.com/aamir-khan-photos-hindi-actor-2628998-7950'))
counter = 0


for img in soup.find_all(title="Aamir Khan"):
    with open("image" + str(counter)+".jpg",'wb') as f:
        m=f.write(urlopen(img['src']).read())
    counter += 1


