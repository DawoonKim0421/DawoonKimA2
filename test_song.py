"""(Incomplete) Tests for Song class."""
from song import Song

# test empty song (defaults)
song = Song()
print(song)
assert song.artist == ""
assert song.title == ""
assert song.year == ""
assert song.require == ""

# test initial-value song
song2 = Song("Amazing Grace", "John Newton", 1779, 'y')
assert song2.title == "Amazing Grace"
assert song2.artist == "John Newton"
assert song2.year == 1779
assert song2.require == 'y'

# TODO: write tests to show this initialisation works
print("{} by {} in {}".format(song2.title, song2.artist, song2.year))

# test mark_learned()
# TODO: write tests to show the mark_learned() method works
song2.marked_learn()
print(song2)