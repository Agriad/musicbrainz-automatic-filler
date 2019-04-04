def printer(album):
    file = open("song_list.txt", "w+")

    for music in album.songs:
        artist = music.artist
        title = music.title
        length = music.length

        file.write(title + " - " + artist + " (" + length + ")")
