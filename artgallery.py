class ArtGallery:
    def __init__(self, name, location, curator):
        self.name = name
        self.location = location
        self.curator = curator
        self.artworks = []
        print(f"\nGallery '{name}' created at {location}")
    
    def add_artwork(self, title, artist, year, medium, price):
        self.artworks.append({'title': title, 'artist': artist, 'year': year, 
                             'medium': medium, 'price': price})
        print(f"✓ '{title}' added!")
    
    def view_all(self):
        if not self.artworks:
            print("\nNo artworks yet!")
            return
        print(f"\n{'='*60}\nARTWORKS IN {self.name.upper()}\n{'='*60}")
        for i, art in enumerate(self.artworks, 1):
            print(f"\n{i}. {art['title']} by {art['artist']}")
            print(f"   Year: {art['year']} | Medium: {art['medium']}")
            print(f"   Price: ${art['price']:,.2f}")
        print(f"\nTotal: {len(self.artworks)} artworks")
    
    def search(self, keyword):
        results = [a for a in self.artworks 
                   if keyword.lower() in a['title'].lower() or keyword.lower() in a['artist'].lower()]
        if results:
            print(f"\nFound {len(results)} result(s):")
            for art in results:
                print(f"  - {art['title']} by {art['artist']}")
        else:
            print(f"\nNo results for '{keyword}'")
    
    def delete_artwork(self, title):
        for i, art in enumerate(self.artworks):
            if art['title'].lower() == title.lower():
                self.artworks.pop(i)
                print(f"✓ '{title}' deleted!")
                return True
        print(f"✗ '{title}' not found!")
        return False
    
    def total_value(self):
        total = sum(a['price'] for a in self.artworks)
        print(f"\nTotal Collection Value: ${total:,.2f}")
        return total
    
    def __del__(self):
        print(f"\n{'='*60}")
        print(f"Destructor: Gallery '{self.name}' closed")
        print(f"Managed {len(self.artworks)} artworks")
        print(f"{'='*60}")

def main():
    print("="*60)
    print("    ART GALLERY COLLECTION MANAGER")
    print("="*60)
    
    name = input("Gallery Name: ").strip()
    loc = input("Location: ").strip()
    cur = input("Curator: ").strip()
    gallery = ArtGallery(name, loc, cur)
    
    while True:
        print("\n" + "="*60)
        print("MENU:\n1. Add Artwork\n2. View All\n3. Search\n4. Delete\n5. Total Value\n6. Gallery Info\n7. Exit")
        print("="*60)
        
        try:
            choice = int(input("Choice (1-7): "))
        except:
            print("Invalid input!")
            continue
        
        if choice == 1:
            t = input("Title: ").strip()
            a = input("Artist: ").strip()
            y = int(input("Year: "))
            m = input("Medium: ").strip()
            p = float(input("Price: $"))
            gallery.add_artwork(t, a, y, m, p)
        elif choice == 2:
            gallery.view_all()
        elif choice == 3:
            gallery.search(input("Search keyword: ").strip())
        elif choice == 4:
            gallery.delete_artwork(input("Title to delete: ").strip())
        elif choice == 5:
            gallery.total_value()
        elif choice == 6:
            print(f"\n{gallery.name} | {gallery.location} | Curator: {gallery.curator}")
        elif choice == 7:
            print("\nExiting...")
            break
    
    del gallery

if __name__ == "__main__":
    main()