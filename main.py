import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
my_id = ''  # client ID
my_secret = ''  # client secret
ccm = SpotifyClientCredentials(client_id=my_id, client_secret=my_secret)
spotify = spotipy.Spotify(client_credentials_manager=ccm)
# 入力
input = input("URLを入れてください：")
# アーティストURL処理
if 'https://open.spotify.com/artist/' in input:
    input = input[32:54]
    url = 'spotify:artist:' + input
    results = spotify.artist_related_artists(url)

    # print( repr(変数名) ) 配列内がわかる関数
    for artist in results['artists']:
        print("アーティスト名..." + artist['name'])
        print("人気度..." + str(artist['popularity']))
        if not len(artist['genres']) == 0:
            print("ジャンル..." + artist['genres'][0])
        print("アーティストurl..." + artist['external_urls']['spotify'])
        popular_track = spotify.artist_top_tracks(artist['id'])
        if not len(popular_track['tracks']) == 0:
            print('人気曲...' + popular_track['tracks'][0]['name'])
            print('人気曲URL...' + popular_track['tracks'][0]['external_urls']['spotify'])
        print("\n")
# 曲URL処理
elif 'https://open.spotify.com/track/' in input:
    input = input[31:53]
    results = spotify.audio_features(input)
    print('BPM...' + str(round(results[0]['tempo'])))