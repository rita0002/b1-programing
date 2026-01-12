# This program lets any user enter songs and their genres, counts how many songs are in each genre, and displays the library.

# Create data structures
songs = []        # List to store song info as tuples
genre_count = {}  # Dictionary to count number of songs per genre

print("Welcome to my Personal Best Music Library Manager!\n")

# Collect multiple songs details
for i in range(1, 6):
    print(f"Enter Song {i}:")
    song_name = input("  Song name: ")
    genre = input("  Genre: ")
    print()
    
    # Store song as a tuple
    song_tuple = (song_name, genre)
    songs.append(song_tuple)
    
    # Count the genre in the dictionary
    genre_count[genre] = genre_count.get(genre, 0) + 1

# Display the full music library
print("=== MY MUSIC LIBRARY ===")
for index, (name, genre) in enumerate(songs, 1):
    print(f"{index}. {name} ({genre})")

# Display genre statistics
print("\n=== GENRE STATISTICS ===")
for genre, count in genre_count.items():
    print(f"{genre}: {count} song(s)")

# Finding and displaying the most popular genre from the list
most_popular = max(genre_count, key=genre_count.get)
print(f"\nMost popular genre: {most_popular}")
