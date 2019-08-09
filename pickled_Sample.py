from bs4 import BeautifulSoup
import requests
from pickle import dump,load
import re


groovy_music = requests.get('https://www.last.fm/music/Bill+Withers/_/Ain%27t+No+Sunshine')

groovy_data = groovy_music.text

filename = open('groovy_lyrics.pickle','wb')
dump(groovy_data,filename)
filename.close()

# rap_filename = open('rap_lyrics.pickle', 'wb')
# dump(rap_data, rap_filename)
# rap_filename.close()


# Load data from a file (will be part of your data processing script)
