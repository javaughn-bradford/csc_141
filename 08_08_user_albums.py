#08_08_user_albums

def make_album(artist, title, num_songs=None):
    """Create a dictionary containing album information."""
    album = {
        'artist': artist,
        'Album': title
    }
    
    if num_songs is not None:
        album['num_songs'] = num_songs
        
    return album

# Predefined albums
album1 = make_album('Rod Wave', 'Hard Times')
album2 = make_album('Lil Uzi Vert', 'Eternal Atake', num_songs=18)
album3 = make_album('Polo G', 'THE GOAT', num_songs=16)

# Print predefined albums
print(album1)
print(album2)
print(album3)


while True:
    print("Album information:")
    

    artist = input("Artist (or 'quit' to exit): ")
    if artist.lower() == 'quit':
        break
    
    title = input("Album title (or 'quit' to exit): ")
    if title.lower() == 'quit':
        break
    
    num_songs_input = input("Number of songs (or press enter to skip): ")
    num_songs = int(num_songs_input) if num_songs_input else None
    
    album = make_album(artist, title, num_songs)
    
    print("Album created:", album)
