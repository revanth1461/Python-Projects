import random
# Album recommendations based on mood
recommendations = {
    "happy": [
        {
            "album": "Future Nostalgia",
            "artist": "Dua Lipa",
            "link": "https://open.spotify.com/search/Future%20Nostalgia%20Dua%20Lipa"
        },
        {
            "album": "24K Magic",
            "artist": "Bruno Mars",
            "link": "https://open.spotify.com/search/24K%20Magic%20Bruno%20Mars"
        },
        {
            "album": "Divide",
            "artist": "Ed Sheeran",
            "link": "https://open.spotify.com/search/Divide%20Ed%20Sheeran"
        },
        {
            "album": "Good Girl Gone Bad",
            "artist": "Rihanna",
            "link": "https://open.spotify.com/search/Good%20Girl%20Gone%20Bad%20Rihanna"
        },
        {
            "album": "Random Access Memories",
            "artist": "Daft Punk",
            "link": "https://open.spotify.com/search/Random%20Access%20Memories%20Daft%20Punk"
        }
    ],

    "sad": [
        {
            "album": "Ghost Stories",
            "artist": "Coldplay",
            "link": "https://open.spotify.com/search/Ghost%20Stories%20Coldplay"
        },
        {
            "album": "Divide",
            "artist": "Ed Sheeran",
            "link": "https://open.spotify.com/search/Divide%20Ed%20Sheeran"
        },
        {
            "album": "Folklore",
            "artist": "Taylor Swift",
            "link": "https://open.spotify.com/search/Folklore%20Taylor%20Swift"
        },
        {
            "album": "Melodrama",
            "artist": "Lorde",
            "link": "https://open.spotify.com/search/Melodrama%20Lorde"
        }
    ],
    "stressed": [
        {
            "album": "In a Time Lapse",
            "artist": "Ludovico Einaudi",
            "link": "https://open.spotify.com/search/In%20a%20Time%20Lapse%20Ludovico%20Einaudi"
        },
        {
            "album": "A Moment Apart",
            "artist": "ODESZA",
            "link": "https://open.spotify.com/search/A%20Moment%20Apart%20ODESZA"
        },
        {
            "album": "Bloom",
            "artist": "Beach House",
            "link": "https://open.spotify.com/search/Bloom%20Beach%20House"
        }
    ],
    "excited": [
        {
            "album": "After Hours",
            "artist": "The Weeknd",
            "link": "https://open.spotify.com/search/After%20Hours%20The%20Weeknd"
        },
        {
            "album": "24K Magic",
            "artist": "Bruno Mars",
            "link": "https://open.spotify.com/search/24K%20Magic%20Bruno%20Mars"
        },
        {
            "album": "Future Nostalgia",
            "artist": "Dua Lipa",
            "link": "https://open.spotify.com/search/Future%20Nostalgia%20Dua%20Lipa"
        }
    ]
}
def get_mood():
    print("\n" + "=" * 45)
    print("              🎵 MOODMATE 🎵")
    print("          Music for your mood")
    print("=" * 45)
    print("\nAvailable moods:")
    print("😊 Happy")
    print("😢 Sad")
    print("😰 Stressed")
    print("🤩 Excited")
    mood = input("\n🎯 Enter your mood: ").lower().strip()
    return mood
def recommend_albums(mood):
    if mood not in recommendations:
        print("\n⚠️ Sorry! That mood is not supported.")
        print("Please choose: happy, sad, stressed, or excited.")
        return
    albums = recommendations[mood]
    selected_albums = random.sample(
        albums,
        min(3, len(albums))
    )
    print("\n" + "=" * 45)
    print("          🎧 YOUR ALBUM RECOMMENDATIONS")
    print("=" * 45)
    for number, album in enumerate(selected_albums, start=1):
        print(f"\n{number}. 💿 {album['album']}")
        print(f"   👤 Artist: {album['artist']}")
        print(f"   🔗 Spotify: {album['link']}")
    print("\n" + "=" * 45)
    print("        🎵 Enjoy your music! 🎵")
    print("=" * 45)
def main():
    mood = get_mood()
    recommend_albums(mood)
main()