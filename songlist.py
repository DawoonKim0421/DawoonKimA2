# create your SongList class in this file
import csv
from operator import attrgetter
from song import Song


class SongList:

    def __init__(self):
        self.song = []

    # Loading the song from CSV file
    def load_song(self):
        with open('songs.csv', 'r') as file:
            song_file = csv.reader(file)
            for i in song_file:
                complete_song = Song(i[0], i[1], i[2], i[3])
                self.song.append(complete_song)
        return self.song

    # Sorting the song list by Title, Artist, Year and Learn
    def sort(self, sort_id):
        # sorting the song base on the title, artist, and year released
        if sort_id == 0:
            attr_sort = 'title'
        elif sort_id == 1:
            attr_sort = 'artist'
        elif sort_id == 2:
            attr_sort = 'year'
        else:
            attr_sort = 'require'
        self.song.sort(key=attrgetter(attr_sort))
        return self.song

    # Adding new song to the song list
    def add_song(self, added_song):
        self.song.append(added_song)
        return self.song

    # Count learned song
    def count_learned(self):
        count = 0
        for j in self.song:
            if j.require == 'n':
                count += 1
        return count

    # Count require song
    def count_require(self):
        count = 0
        for j in self.song:
            if j.require == 'y':
                count += 1
        return count

    def get_song(self, title):
        for song in self.song:
            if song.title == title:
                return song

    def save_song(self):
        with open('songs.csv', 'w') as output_file:
            for song in self.song:
                output_string = [song.title, song.artist, str(song.year), song.require]
                write_csv = ','.join(output_string)
                output_file.write(str(write_csv)+'\n')