from misc_data import AlbumData


def song_compressor(album_list, combined_album):
    boolean = True
    counter = 0

    for album in album_list.album:
        if boolean:
            combined_album.add_song_list(album.songs)
        for songs in album.songs:
            if combined_album.songs[counter].length is None and songs.length is not None:
                combined_album.modify_song_date(counter, songs.length)
            counter += 1
        counter = 0
        boolean = False


def compressor(album_list):
    combined_album = AlbumData()
    for album in album_list.album:
        if combined_album.artist is None:
            combined_album.artist = album.artist
        if combined_album.title is None:
            combined_album.title = album.title
        if combined_album.label is None:
            combined_album.label = album.label
        if combined_album.cat_no is None:
            combined_album.cat_no = album.cat_no
        if combined_album.country is None:
            combined_album.country = album.country
        if combined_album.date is None or len(combined_album.date) < len(album.date):
            combined_album.date = album.date

    song_compressor(album_list, combined_album)

    return combined_album
