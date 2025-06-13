def make_album(artist_name, album_title, number_of_songs=None):
    """Describing a music album."""
    album = {"artist_name": artist_name, "album_title": album_title}
    if number_of_songs:
        album["number of songs"] = number_of_songs
    print(album)
    return album


while True:
    print(f"\nPlease enter album artist and title: ")
    print(f"(Enter 'q' to quit.)")
    artist = input("Artist name: ")
    if artist.lower() == "q":
        break
    if artist == "":
        print(f"Artist cannot be blank!")
        break
    title = input("Album title: ")
    if title.lower() == "q":
        break
    if title == "":
        print(f"Album title cannot be blank!")
        break
    songs = input("Number of songs: ")
    if str(songs).lower() == "q":
        break
    if songs:
        songs = int(songs)

    make_album(artist, title, songs)
