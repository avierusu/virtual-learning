# When we have our modules in a package,
# we import them like this:
from museum.artwork import get_artworks
from museum.artists import get_artists

def main():
    # Prompt for user input and store it
    art = input("Artwork: ")
    # Get 3 artworks
    artworks = get_artworks(query=art, limit=3)
    
    # Display the artworks
    for art in artworks:
        print(f"* {art}")
    
    # Prompt for user input and store it
    name = input("Artist: ")
    # Get 3 artists
    artists = get_artists(query=name, limit=3)
    
    # Display the artists
    for artist in artists:
        print(f"* {artist}")


main()