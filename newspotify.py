import requests, sys, time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
import json
from PIL import Image
from io import BytesIO
from client import CLIENT_ID, CLIENT_SECRET

'''
GET ACCESS TOKEN (*)
'''
def get_token():
    token = SpotifyClientCredentials(client_id = CLIENT_ID, client_secret = CLIENT_SECRET)
    access_token = token.get_access_token()
    #print(token.token_info)
    return access_token
    #print(access_token)


'''
GET PLAYLISTS (no auth)
'''
def get_playlists(username):
    client_credentials_manager = SpotifyClientCredentials(client_id = CLIENT_ID, client_secret = CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    playlists = sp.user_playlists(username)

    while playlists:
        for i, playlist in enumerate(playlists['items']):
            print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None

'''
GET AUDIO ANALYSIS (no auth)

samples track at multiple time intervals
'''
def track_analysis(uri):
    client_credentials_manager = SpotifyClientCredentials(client_id = CLIENT_ID, client_secret = CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    if len(sys.argv) > 1:
        tid = sys.argv[1]
    else:
        tid = uri

    start = time.time()
    analysis = sp.audio_analysis(tid)
    delta = time.time() - start
    print(json.dumps(analysis, indent=4))
    print ("analysis retrieved in %.2f seconds" % (delta,))

'''
GET AUDIO FEATURES (no auth) (*)
'''
def track_features(uri):
    client_credentials_manager = SpotifyClientCredentials(client_id = CLIENT_ID, client_secret = CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    if len(sys.argv) > 1:
        tid = sys.argv[1]
    else:
        tid = uri

    start = time.time()
    analysis = sp.audio_features(tid)
    delta = time.time() - start
    data_str = json.dumps(analysis, indent=3)
    data_list = json.loads(data_str)
    data_dict = data_list[0]
    return data_dict
    #print ("features retrieved in %.2f seconds" % (delta,))

'''
GET RELATED ARTISTS (auth) (*)
'''
def get_related(artist):
    if len(sys.argv) > 1:
        artist_name = sys.argv[1]
    else:
        artist_name = artist

    sp = spotipy.Spotify(auth = get_token())
    result = sp.search(q='artist:' + artist_name, type='artist')
    try:
        name = result['artists']['items'][0]['name']
        uri = result['artists']['items'][0]['uri']

        related = sp.artist_related_artists(uri)
        print('Related artists for', name)
        for artist in related['artists']:
            print('  ', artist['name'])
    except:
        print("usage show_related.py [artist-name]")

'''
GET SONG URI FROM SEARCH FUNCTION (*)
'''
def get_song_info(search, type='track'):
    if len(sys.argv) > 1:
        search_str = sys.argv[1]
    else:
        search_str = search

    sp = spotipy.Spotify(auth= get_token())
    result = sp.search(search_str)
    #pprint.pprint(result)

    song_dict = {}
    song_dict["song_uri"] = result['tracks']['items'][0]['uri']
    song_dict["song_name"] = result['tracks']['items'][0]['name']
    song_dict["song_link"] = result['tracks']['items'][0]['external_urls']
    song_dict["song_popularity"] = result['tracks']['items'][0]['popularity']
    song_dict["album_name"] = result['tracks']['items'][0]['album']['name']
    song_dict["release_date"] = result['tracks']['items'][0]['album']['release_date']
    song_dict["album_uri"] = result['tracks']['items'][0]['album']['uri']
    song_dict["album_image"] = result['tracks']['items'][0]['album']['images'][0]['url']

    song_dict["artist"] = result['tracks']['items'][0]['artists'][0]['name']
    #pprint.pprint(song_dict)

    return song_dict
'''
GET ALBUM INFO (auth)
'''
def get_album_info(uri):
    if len(sys.argv) > 1:
        urn = sys.argv[1]
    else:
        urn = uri


    sp = spotipy.Spotify(auth = get_token())
    album = sp.album(urn)
    pprint.pprint(album)
