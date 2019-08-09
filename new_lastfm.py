from bs4 import BeautifulSoup
import requests
from pickle import dump,load
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
# from songanalysis import general_track_info

# Pickled data imported from pickle_music.py
input_file = open('thesong.pickle', 'rb')
reloaded_copy_of_texts = load(input_file)
soup = BeautifulSoup(reloaded_copy_of_texts)

groovy_links = soup.find_all("a")
groovy_link_source = soup.find_all('', class_ = 'link-block-target')
third_tile = str(groovy_link_source[4])

smooth_groovy = re.sub(r'</a>', '', third_tile)
# rifty_groovy = re.sub(r'<a    >', '', smooth_groovy)
funky_groovy = re.sub(r'class="link-block-target"', '', smooth_groovy)
shwifty =  re.sub(r'< >', '', funky_groovy)
# print (shwifty)
# regex  = re.compile("<>")
# result = re.findall(regex,shwifty)

def cleanr(text):
    start = text.find('<')
    end = text.find('>')
    result = ""
    if start != -1 and end != -1 and end < len(text)-1:
        result = text[end+1:]
    return result

print(cleanr(shwifty))
