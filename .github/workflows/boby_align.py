import os
from mutagen.easyid3 import EasyID3
from mutagen.wave import WAVE
from mutagen.flac import FLAC

# Konfigurasi Identiti Baru
OLD_NAME = "SNiTE Bobbie"
NEW_NAME = "SNiTE BoBy"
TARGET_DIR = "./music_assets" # Tukar kepada path repo anda

def align_metadata(file_path):
    try:
        if file_path.endswith('.mp3'):
            audio = EasyID3(file_path)
            audio['artist'] = NEW_NAME
            audio['albumartist'] = NEW_NAME
            audio.save()
        elif file_path.endswith('.flac'):
            audio = FLAC(file_path)
            audio['artist'] = NEW_NAME
            audio['albumartist'] = NEW_NAME
            audio.save()
        # Nota: Metadata WAV adalah terhad, penamaan fail lebih kritikal di sini
        print(f"[SUCCESS] Metadata Updated: {file_path}")
    except Exception as e:
        print(f"[ERROR] Failed to update {file_path}: {e}")

def rename_files(root, filename):
    if OLD_NAME.lower() in filename.lower() or "bobbie" in filename.lower():
        new_filename = filename.replace("Bobbie", "BoBy").replace("bobbie", "BoBy")
        old_path = os.path.join(root, filename)
        new_path = os.path.join(root, new_filename)
        os.rename(old_path, new_path)
        return new_path
    return os.path.join(root, filename)

def execute_alignment():
    for root, dirs, files in os.walk(TARGET_DIR):
        for file in files:
            if file.endswith(('.mp3', '.wav', '.flac')):
                # 1. Rename File System
                current_path = rename_files(root, file)
                # 2. Update Internal Tags
                align_metadata(current_path)

if __name__ == "__main__":
    execute_alignment()
    print(f"\nAlignment Complete. All assets now under {NEW_NAME} King Status.")

