def printer(album):
    file = open("song_list.txt", "w+")
    counter = 1

    for music in album.songs:
        artist = music.artist
        title = music.title
        length = music.length

        if title is not None:
            if length is None:
                file.write(str(counter) + " " + title + " - " + artist + "\n")
            else:
                file.write(str(counter) + " " + title + " - " + artist + " (" + length + ")" + "\n")

            counter += 1
