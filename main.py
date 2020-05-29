"""
Name: Da Woon Kim
Date: 20th May 2020
Brief Project Description: This program displays songs in the CSV file, indicating that you have completed learning
                            or need to learn from any song. Users can also add new songs to the list and learn them.
GitHub URL: https://github.com/DawoonKim0421/DawoonKimA2.git
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from song import Song
from songlist import SongList

# Create your main program in this file, using the SongsToLearnApp class
ERROR_COLOUR = [0, 1, 1, 1]
ANNOUNCEMENT = [1, 1, 0, 1]


class SongsToLearnApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.song_list = SongList()
        self.requireSong = 0
        self.learnedSong = 0

    def build(self):
        self.title = "Song To learn 2.0"    # Add the title of the program
        self.root = Builder.load_file('app.kv')     # Reference kivy file
        self.song_list.load_song()      # Using class method to load CSV
        self.show_song()
        self.sorting(self.root.ids.sort_option.text)
        return self.root

    def show_song(self):  # Display Songs in GUI
        self.requireSong = 0
        self.learnedSong = 0
        for i in self.song_list.song:
            if i.require == 'y':    # y means need to learn song
                song_button = Button(text='' + '"' + i.title + '"' + " by " + i.artist + " (" + i.year + ")",
                                     id=i.title)        # Display format for need to learn song
                song_button.background_color = [0, 88, 88, 0.3]     # Button background colour
                self.requireSong += 1
            else:
                song_button = Button(text='' + '"' + i.title + '"' + " by " + i.artist + " (" + i.year + ") (learned)",
                                     id=i.title)        # Display format for learned song
                song_button.background_color = [88, 89, 0, 0.3]     # Button background colour
                self.learnedSong += 1
            song_button.bind(on_release=self.select)
            self.root.ids.all_song.add_widget(song_button)
            # Display learned and to learn song
            self.root.ids.title_learned.text = "To learn: {}, Learned: {}".format(self.requireSong,
                                                                                  self.learnedSong)

    def select(self, button):     # Display selected song
        if self.song_list.get_song(button.id).require == 'y':       # Mark song as learned
            self.song_list.get_song(button.id).require = 'n'
            self.root.ids.program_detail.text = "{} is learned.".format(button.id)
        else:
            self.song_list.get_song(button.id).require = 'y'        # Mark song as unlearn
            self.root.ids.program_detail.text = "{} need to learn.".format(button.id)   # Display selected song format
        self.root.ids.program_detail.color = ANNOUNCEMENT      # Set label colour
        self.sorting(self.root.ids.sort_option.text)
        self.root.ids.all_song.clear_widgets()      # Clear widgets
        self.show_song()

    def sorting(self, chosen):      # Sort song function
        available_choice = chosen
        if available_choice == 'Title':     # Sort the song by Title
            self.song_list.sort(0)
        elif available_choice == 'Artist':      # Sort the song by Artist
            self.song_list.sort(1)
        elif available_choice == 'Year':    # Sort the song by Year
            self.song_list.sort(2)
        else:
            self.song_list.sort(3)          # Sort the song by Require
        self.root.ids.sort_option.clear_widgets()
        self.root.ids.all_song.clear_widgets()
        self.show_song()

    def add_song(self):     # Add new song to the list
        title = self.root.ids.title_fill.text
        artist = self.root.ids.artist_fill.text
        year = self.year_check()
        if title == '' or artist == '' or year == '':  # No input validation
            self.root.ids.program_detail.color = ERROR_COLOUR
            self.root.ids.program_detail.text = 'Please fill every box'
        elif year == "string":          # Year validation
            self.root.ids.program_detail.color = ERROR_COLOUR
            self.root.ids.program_detail.text = 'Please enter a valid number'
        elif year < 0:                  # Year validation
            self.root.ids.program_detail.color = ERROR_COLOUR
            self.root.ids.program_detail.text = 'Year must be >= 0'
        else:
            song_title = self.root.ids.title_fill.text
            song_artist = self.root.ids.artist_fill.text
            song_year = self.root.ids.year_fill.text
            song_input = Song(song_title, song_artist, song_year, 'y')
            self.song_list.add_song(song_input)     # Add new song to song list
            self.root.ids.all_song.clear_widgets()
            self.clear_all()
            self.root.ids.program_detail.color = ANNOUNCEMENT
            self.root.ids.program_detail.text = 'A song have added to the song list'
            self.show_song()

    def year_check(self):   # Validate the song year input
        try:
            year = int(self.root.ids.year_fill.text)
            return year
        except ValueError:
            year = 'string'
            return year

    def clear_all(self):    # Clear input in text input function
        self.root.ids.title_fill.text = ''
        self.root.ids.artist_fill.text = ''
        self.root.ids.year_fill.text = ''
        self.root.ids.program_detail.text = ''

    def stop(self):
        self.song_list.save_song()      # Update CSV file after the user close the program


SongsToLearnApp().run()
