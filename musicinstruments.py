from abc import ABC, abstractmethod

# Abstract parent class
class Instrument(ABC):
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
    
    @abstractmethod
    def make_sound(self):
        pass
    
    def get_info(self):
        return f"{self.brand} {self.name}"

# Child class: Guitar
class Guitar(Instrument):
    def __init__(self, name, brand, strings=6):
        super().__init__(name, brand)
        self.strings = strings
    
    def make_sound(self):
        return f"[GUITAR] {self.get_info()} plays: Strum strum strum! (Guitar with {self.strings} strings)"

# Child class: Piano
class Piano(Instrument):
    def __init__(self, name, brand, keys=88):
        super().__init__(name, brand)
        self.keys = keys
    
    def make_sound(self):
        return f"[PIANO] {self.get_info()} plays: Do Re Mi Fa Sol La Ti Do! (Piano with {self.keys} keys)"

# Child class: Drum
class Drum(Instrument):
    def __init__(self, name, brand, size="medium"):
        super().__init__(name, brand)
        self.size = size
    
    def make_sound(self):
        return f"[DRUM] {self.get_info()} plays: Boom boom bang bang! ({self.size.capitalize()} drum)"

# Child class: Violin
class Violin(Instrument):
    def __init__(self, name, brand, bow=True):
        super().__init__(name, brand)
        self.bow = bow
    
    def make_sound(self):
        bow_status = "with bow" if self.bow else "without bow"
        return f"[VIOLIN] {self.get_info()} plays: Screech screech... (Violin {bow_status})"

# Child class: Trumpet
class Trumpet(Instrument):
    def __init__(self, name, brand, valves=3):
        super().__init__(name, brand)
        self.valves = valves
    
    def make_sound(self):
        return f"[TRUMPET] {self.get_info()} plays: Toot toot! (Trumpet with {self.valves} valves)"

# Music Show class to manage instruments
class MusicShow:
    def __init__(self, show_name):
        self.show_name = show_name
        self.instruments = []
    
    def add_instrument(self, instrument):
        self.instruments.append(instrument)
    
    def start_show(self):
        print(f"\n{'='*60}")
        print(f"Welcome to {self.show_name}")
        print(f"{'='*60}\n")
        
        if not self.instruments:
            print("No instruments in the show yet!")
            return
        
        for i, instrument in enumerate(self.instruments, 1):
            print(f"{i}. {instrument.make_sound()}")
        
        print(f"\n{'='*60}")
        print(f"Thank you for watching {self.show_name}!")
        print(f"{'='*60}\n")

# Main program
if __name__ == "__main__":
    # Create a music show
    show = MusicShow("Amazing Music Instrument Show")
    
    # Create different instruments
    guitar = Guitar("Acoustic Guitar", "Fender", strings=6)
    piano = Piano("Grand Piano", "Steinway", keys=88)
    drum = Drum("Snare Drum", "Ludwig", size="small")
    violin = Violin("Stradivarius", "Antonio", bow=True)
    trumpet = Trumpet("Brass Trumpet", "Bach", valves=3)
    
    # Add instruments to the show
    show.add_instrument(guitar)
    show.add_instrument(piano)
    show.add_instrument(drum)
    show.add_instrument(violin)
    show.add_instrument(trumpet)
    
    # Start the music show
    show.start_show()
    
    # Demonstrate individual instrument sounds
    print("\n--- Individual Instrument Demonstrations ---")
    print(guitar.make_sound())
    print(piano.make_sound())
    print(drum.make_sound())