from bs4 import BeautifulSoup
import requests
from pickle import dump,load
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

analyzer = SentimentIntensityAnalyzer()

# Pickled data imported from pickle_music.py
input_file = open('groovy_lyrics.pickle', 'rb')
reloaded_copy_of_texts = load(input_file)
soup = BeautifulSoup(reloaded_copy_of_texts)

# LOL 
groovy_links = soup.find_all("a")
groovy_link_source = soup.find_all('', class_ = 'grid-items-item-details')
print (groovy_link_source)
groovy_raw_lyric_urls = []

base_url = 'https://www.last.fm/music/'

#
# for i in range(0,20, 1):
#     href_groovy = groovy_link_source[i]['href']
#     groovy_raw_lyric_urls.append(href_groovy)

groovy_song_lyrics_only = []
# sixnine_song_lyrics_only = []

for xx in range (0,20,1):
    lyric_links = requests.get(base_url + groovy_raw_lyric_urls[xx])
    # rap_links = requests.get(base_url + sixnine_raw_lyric_urls[xx])

    groovy_src = lyric_links.content
    # rap_src = rap_links.content

    nuts_and_bolts_soup = BeautifulSoup(groovy_src)
    # rap_rappy_soup = BeautifulSoup(rap_src)

    funky_links = nuts_and_bolts_soup.find_all("a")
    # rap_linksss = rap_rappy_soup.find_all('a')

    funky_link_source = str(nuts_and_bolts_soup.find_all('', class_ = 'grid-items-item-details'))
    # rap_link_source = str(rap_rappy_soup.find_all('', class_ = 'lyrictxt'))
    #
    # cleaned_funk = funky_link_source.replace('<br>','')
    # cleanner_metal = cleaned_metal.replace('<br/>','')
    # the_cleannest_metal = cleanner_metal.replace('...','')

    # cleaned_rap = rap_link_source.replace('<br>','')
    # cleanner_rap = cleaned_rap.replace('<br/>','')
    # the_cleannest_rap = cleanner_rap.replace('...','')

    s = the_cleannest_metal
    x = re.sub(r'<[^>]+>?' ,' ',s)
    y = re.sub(r'[?]', ' ', x)
    z = re.sub(r'/n',' ', y)
    ss = re.sub(r'\n',' ', z)
    xx = re.sub(r'\r', ' ', ss)
    slipknot_song_lyrics_only.append(xx)

    qq = the_cleannest_rap
    tt = re.sub(r'<[^>]+>?' ,' ',qq)
    nn = re.sub(r'[?]', ' ',tt)
    mm = re.sub(r'[?]', ' ',nn)
    ll = re.sub(r'\n',' ',mm)
    yy = re.sub(r'\r', ' ',ll)

    sixnine_song_lyrics_only.append(yy)

# print(slipknot_song_lyrics_only)
all_metal = ' '.join(slipknot_song_lyrics_only)
all_rap = ' '.join(sixnine_song_lyrics_only)
# print(all_metal)
# print(all_rap)

# rap_genre = requests.get('https://www.lyricsfreak.com/search.php?q=post+malone')
# rap_src = rap_genre.content
# rap_soup = BeautifulSoup(rap_src)
# rap_links = rap_soup.find_all('a')
# rap_link_source = soup.find_all('', class_ = 'song')
#
# raw_rap_lyrics = []
# raw_rap_lyric_urls = []
#
# for i in range(0,15, 1):
#     href_rap = raw_rap_lyrics[i]['href']
#     raw_rap_lyric_urls.append(href_metal)
# print (slipknot_raw_lyric_urls)
analyzer.polarity_scores(all_metal)
print (analyzer.polarity_scores(all_metal))

analyzer.polarity_scores(all_rap)
print (analyzer.polarity_scores(all_rap))

# {'neg': 0.203, 'neu': 0.68, 'pos': 0.117, 'compound': -1.0}
# {'neg': 0.185, 'neu': 0.657, 'pos': 0.158, 'compound': -0.9998}


 # This is the delete function to remove and clean the data -----------------
    # def delete():
# start = '<'
# end = '>'
# while i < len(heavy_link_source):
#     if heavy_link_source[i] == start:
#         start_place = i
#     if heavy_link_source[i]== end:
#         end_place = i

    # return(heavy_link_source[start_place:end_place])

""" A natural way to approach this in Python would be to use a dictionary
where the keys are words that appear and the values are frequencies of
words in the text"""
