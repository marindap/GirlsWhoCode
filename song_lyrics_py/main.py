""" Song Lyrics Guessing Game """

print("Let's guess the song!")

song = "We Will Rock You"
artist = "Queen"

lyrics = [
    "Buddy, you're a boy, make a big noise",
    "Playing in the street, gonna be a big man someday"
]

print("Let's guess the artist or song title: ")
song_correct = False
artist_correct = False

want_to_guess_song = ''
want_to_guess_artist = ''


def artist_check(artist_guess):
    if artist_guess.lower() == artist.lower():
        return True
    else:
        return False


def song_check(song_guess):
    if song_guess.lower() == song.lower():
        return True
    else:
        return False


for index in range(len(lyrics)):
    print(lyrics[index])
    want_to_guess_song = input("Do you know the song?")

    if want_to_guess_song == 'yes':
        guess = input("What is the the song title? /n")
        if song_check(guess):
            song_correct = True
            print(f'You got it right! The song is {song}')
        else:
            print('Nice try!')

    want_to_guess_artist = input("Do you know the artist?")

    if want_to_guess_artist == 'yes':
        guess = input("Who is the artist? /n")
        if artist_check(guess):
            artist_correct = True
            print(f'Way to go! The artist is {artist}')
        else:
            print("That's not who I was looking for...")

    tries = len(lyrics) - (index + 1)

    if not song_correct and not artist_correct and tries != 0:
        print(f'You have {tries} tries left')
    else:
        print('end')
        break



