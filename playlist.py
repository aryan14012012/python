class Playlist:
    
    
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.songs = []
        print(f"Playlist '{self.name}' ({self.genre}) is ready.")
        
    def add_song(self, song):
        self.songs.append(song)
        print(f"{song}' added to {self.name}.")
        
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"{song} removed.")
        else:
            print(f"{song} not found in the playlist.")
            
    def display(self):
        print(f"\n---{self.name} ({self.genre})---")
        if self.songs:
            for i, song in enumerate(self.songs,1):
                print(f"   {i}. {song}")
        else:
            print(" no songs yet. add some!")
            
            
    def _del__(self):
        print(f"Playlist '{self.name}'has been deleted.Good bye!")
        
        
my_playlist = Playlist("My Playlist", "Pop")


while True:
    print("\n1. Add song 2. Remove song 3. View playlist 4. Exit")
    choice = input("Enter your choice: ")
    
    
    if choice == '1':
        song = input("Enter the song name to add: ")
        my_playlist.add_song(song)
    elif choice == '2':
        song = input("Enter the song name to remove: ")
        my_playlist.remove_song(song)
    elif choice == '3':
        my_playlist.display()
    elif choice == '4':
        del my_playlist
        break
    else:
        print("Invalid choice. Enter 1,2,3,or 4.")