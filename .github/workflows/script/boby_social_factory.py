import json

# Mengambil rujukan dari Manifest
ARTIST_NAME = "SNiTE BoBy"
PROTOCOL = "King Status v2026"

def generate_launch_kit(track_name, link):
    platforms = {
        "X_Twitter": {
            "content": f"Entry: {track_name}\nArtist: {ARTIST_NAME}\nProtocol: {PROTOCOL}\n\nDecoding the future of AI-Architecture. 🌐\n\nListen here: {link}\n#SNiTEBoBy #AIArchitecture #FutureCore #KingStatus",
            "limit": 280
        },
        "Instagram": {
            "content": f"🎨 {track_name} by {ARTIST_NAME}\n\nIdentity locked. Metadata verified under {PROTOCOL}. This is the first evolution of the SNiTE BoBy era. \n\nCheck the link in bio for the full experience. 👑\n\n#SNiTEBoBy #AIArtist #MusicProducer #ProducerAI #SunoV5 #DigitalSovereignty",
            "limit": 2200
        },
        "Discord_Dev": {
            "content": f"```\n[SYSTEM UPDATE]\nEntity: {ARTIST_NAME}\nRelease: {track_name}\nStatus: DEPLOYED\nLink: {link}\n```\nAll assets verified. Check GitHub for source metadata.",
            "limit": 2000
        }
    }
    
    print(f"--- [SOCIAL MEDIA KIT: {track_name}] ---")
    for platform, data in platforms.items():
        print(f"\n[{platform}]:\n{data['content']}\n{'-'*20}")

# Contoh Penggunaan
# generate_launch_kit("Neon Architecture", "https://spotify.link/sniteboby")
