import json

# deprecated

def createTrack(id, artist, track_position, song, release_date, lyrics):
    value = {
        "id":id, 
        "artist":artist,
        "track_psition":track_position,
        "song":song,
        "release_date":release_date,
        "lyrics":lyrics
        }
    return value

def createJson(filename, trackList):

    data = {'data': trackList}

    with open(f'{filename}.json', 'w') as outfile:
        json.dump(data, outfile)