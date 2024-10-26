#08_07_album 

def make_album(artist, title, num_songs=None):
    album = {
        'artist': artist,
        'Album': title
    }
    
    if num_songs is not None:
        album['num_songs'] = num_songs
        
    return album

album1 = make_album('Rod wave', 'Hard times')


album2 = make_album('Lil uzi vert', 'eternal etake', num_songs=18)


album3 = make_album('Polo G', 'THE GOAT', num_songs=16)

print(album1)


print(album2)


print(album3)
