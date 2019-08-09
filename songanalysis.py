'''
MAKING SONG CLASS

passing dictionary from track_features() into class
'''
import requests
import re
#import new_lastfm as nlf
import testspotify as tspot
from pickle import dump,load
from bs4 import BeautifulSoup


class Song:
    def __init__(self, dictionary):
        for key, value in dictionary.items():
            setattr(self, key, value)
    def get_s_mode(self):
        s_mode = ''
        if self.mode == 0:
            s_mode = 'major'
        if self.mode == 1:
            s_mode = 'minor'
        return s_mode
    def get_s_key(self):
        s_key = ''
        if self.key == 0: s_key = 'C'
        if self.key == 1: s_key = 'C#/Db'
        if self.key == 2: s_key = 'D'
        if self.key == 3: s_key = 'D#/Eb'
        if self.key == 4: s_key = 'E'
        if self.key == 5: s_key = 'F'
        if self.key == 6: s_key = 'F#/Gb'
        if self.key == 7: s_key = 'G'
        if self.key == 8: s_key = 'G#/Ab'
        if self.key == 9: s_key = 'A'
        if self.key == 10: s_key = 'A#/Bb'
        if self.key == 11: s_key = 'B'
        if self.key == -1: s_key = 'no key detected'
        return s_key
    def get_s_danceability(self):
        s_dance = ''
        if self.danceability >= 0 and self.danceability <= 0.2: s_dance = 'not danceable'
        if self.danceability > 0.2 and self.danceability <= 0.4: s_dance = 'kinda danceable'
        if self.danceability > 0.4 and self.danceability <= 0.6: s_dance = 'pretty danceable'
        if self.danceability > 0.6 and self.danceability <= 0.8: s_dance = 'very danceable'
        if self.danceability > 0.8 and self.danceability <= 1: s_dance = 'extremely danceable'
        return s_dance
    def get_s_energy(self):
        s_energy = ''
        if self.energy >= 0 and self.energy <= 0.33: s_energy = 'low energy'
        if self.energy > 0.33 and self.energy <= 0.67: s_energy = 'mid energy'
        if self.energy > 0.67 and self.energy <= 1: s_energy = 'high energy'
        return s_energy
    def get_s_bpm(self):
        s_bpm = int(self.tempo)
        return s_bpm
    def get_s_valence(self):
        s_valence = ''
        if self.valence >= 0 and self.valence <= 0.2: s_valence = 'very negative vibes'
        if self.valence > 0.2 and self.valence <= 0.4: s_valence = 'negative vibes'
        if self.valence > 0.4 and self.valence <= 0.6: s_valence = 'neutral vibes'
        if self.valence > 0.6 and self.valence <= 0.8: s_valence = 'positive vibes'
        if self.valence > 0.8 and self.valence <= 1: s_valence = 'very positive vibes'
        return s_valence
    def return_important(self):
        important = []
        important.append(self.get_s_mode())
        important.append(self.get_s_key())
        important.append(self.get_s_danceability())
        important.append(self.get_s_energy())
        important.append(self.get_s_bpm())
        important.append(self.get_s_valence())
        return important

#putting important track info for a song into a list
def general_track_info(song_name):
    song_dict = tspot.get_song_info(song_name)
    track_info_list = []

    track_name = song_dict["song_name"]
    # TRACK_NAME = song_dict["X"]
    #print("Track: " + track_name)

    artist_name = song_dict["artist"]
    # ARTIST_NAME = song_dict["Y"]
    #print("Artist: " + artist_name)

    album_name = song_dict["album_name"]
    # print("Album: " + album_name)
    release_date = song_dict["release_date"]
    # print("Year: " + release_date[0:4])
    track_info_list.append(track_name)
    track_info_list.append(artist_name)
    track_info_list.append(album_name)
    track_info_list.append(release_date[0:4])
    # print(track_info_list[0])
    # print(track_info_list[1])
    return track_info_list

#putting important track features for a song into a list
def analysis_track_features(song_name):
    #getting song ID
    song_dict = tspot.get_song_info(song_name)
    song_uri = song_dict["song_uri"]

    #getting track features
    features_dict = tspot.track_features(song_uri)

    #track feature dictionary into song class
    song = Song(features_dict)
    t_feat = song.return_important()
    return t_feat

#building url based on user input song to prepare for pickling
def build_url(track):
    list = general_track_info(track)
    base_url = 'https://www.last.fm/music/'
    added_artist = list[1]
    slash = added_artist + '/_/'
    added_track = re.sub(' ', '+', list[0])
    new_url = base_url + slash + added_track
    yeet = requests.get(new_url)
    anotha_yeet = yeet.text
    return anotha_yeet

#asking for user input
input = input("What song? ")

#pickling based on track input: returns url for the generated similar song
def pickle(track):
    song_tfile = build_url(track)
    filename = open(input + '.pickle', 'wb')
    dump(song_tfile, filename)
    filename.close()

    input_file = open(input + '.pickle', 'rb')
    reloaded_copy_of_texts = load(input_file)
    soup = BeautifulSoup(reloaded_copy_of_texts)

    groovy_links = soup.find_all("a")
    groovy_link_source = soup.find_all('', class_ = 'link-block-target')
    third_tile = str(groovy_link_source[4])

    smooth_groovy = re.sub(r'</a>', '', third_tile)
    funky_groovy = re.sub(r'class="link-block-target"', '', smooth_groovy)
    shwifty =  re.sub(r'< >', '', funky_groovy)
    return shwifty

#cleans up url for similar song and extracts the similar track name
def cleanr(text):
    start = text.find('<')
    end = text.find('>')
    result = ""
    if start != -1 and end != -1 and end < len(text)-1:
        result = text[end+1:]
    return result

# includes entire process of outputting track info and track features for the initial song input
def final_process_i(song_name):
    viz_info = []
    trackinfo = general_track_info(song_name)
    featureinfo = analysis_track_features(song_name)
    build_url(song_name)
    viz_info.append(trackinfo)
    viz_info.append(featureinfo)
    return viz_info

#includes entire process for outputting track info and track features the similar song generated
def final_process_o(song_name):
    viz_info = []
    trackinfo = general_track_info(song_name)
    featureinfo = analysis_track_features(song_name)
    viz_info.append(trackinfo)
    viz_info.append(featureinfo)
    return viz_info

the_second_yeet = cleanr(pickle(input))

'''
print("-------------------")
final_process_o(the_second_yeet)
'''
