"""
(incomplete) Tests for SongList class
"""
from songlist import SongList
from song import Song

# test empty SongList
song_list = SongList()
print(song_list)
assert len(song_list.song) == 0

# test loading songs
song_list.load_song()
print(song_list)
assert len(song_list.song) > 0  # assuming CSV file is not empty

# TODO: add tests below to show the various required methods work as expected
# test sorting songs
print("Sorting by year")
assert song_list.sort('year')
print("Sorting by title")
assert song_list.sort('title')

# test adding a new Song
song3 = Song('Hero', 'Enrique Iglesias', 2008, 'y')
assert song_list.add_song(song3)

# test get_song()
assert song_list.get_song('Hero')

# test getting the number of required and learned songs (separately)
assert song_list.count_learned()
assert song_list.count_require()

# test saving songs (check CSV file manually to see results)
song_list.save_song()