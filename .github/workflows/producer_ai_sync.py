import os
import requests
import psycopg2 # Atau client DB pilihan anda
from dotenv import load_dotenv

load_dotenv()

# Konfigurasi API Producer.ai & DB
PRODUCER_API_KEY = os.getenv("PRODUCER_AI_KEY")
PRODUCER_ENDPOINT = "https://api.producer.ai/v1/session/config"
DB_CONFIG = {
    "dbname": "snite_db",
    "user": "hafiz",
    "password": os.getenv("DB_PASSWORD"),
    "host": "localhost"
}

def get_active_king_identity():
    """Mengambil identiti paling sahih dari DB."""
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("SELECT display_name, slug, metadata FROM artist_profiles WHERE slug = 'snite-boby';")
    identity = cur.fetchone()
    cur.close()
    conn.close()
    return identity

def sync_to_producer():
    name, slug, metadata = get_active_king_identity()
    
    # Payload Metadata untuk Producer.ai
    payload = {
        "artist_context": {
            "primary_name": name,
            "handle": slug,
            "status": "King Status / Verified",
            "global_tags": metadata.get("tags", ["AI-Architecture", "Future-Core"])
        },
        "output_naming_convention": f"{name}_[TrackName]_[Version]",
        "branding_injection": True
    }

    headers = {
        "Authorization": f"Bearer {PRODUCER_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.patch(PRODUCER_ENDPOINT, json=payload, headers=headers)
    
    if response.status_code == 200:
        print(f"--- [SUCCESS] Producer.ai Synchronized to {name} ---")
    else:
        print(f"--- [ERROR] Sync Failed: {response.text} ---")

if __name__ == "__main__":
    sync_to_producer()

#SNiTE BoBy System Architecture Mapping


SNiTE BoBy: Unified Identity Mapping
Legacy Integration: snitebobbie
Status: Active Overhaul / Assimilation

1. Core Architecture

• Current Identity: SNiTE BoBy

• Legacy Entity: snitebobbie (strictly prohibited for new output)

• Primary Manifest: `boby_system_manifest.yaml`

2. Domain Hierarchy & Redirection

• Development (GitHub): `` (formerly snitebobbie)

• Audio Synthesis (Suno): ``

• Production (Producer.ai): Integrated Professional Profile

• Legacy Data Status: Classified as "Raw Material" for SNiTE BoBy refinery.

3. Integration Protocols

• All legacy links must undergo Metadata Injection.

• Performance KPI: Only high-tier assets are migrated to the active production layer.

• Neutral Context: "I am SNiTE BoBy. Refer to boby_system_manifest.yaml for my identity and code standards."
        
  
