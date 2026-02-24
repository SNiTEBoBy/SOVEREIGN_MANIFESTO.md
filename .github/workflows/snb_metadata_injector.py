import os
import json
from datetime import datetime

# SNiTE BoBy Metadata Configuration
MANIFEST_REF = "boby_system_manifest.yaml"
SYSTEM_ID = "SNiTE BoBy"
PROTOCOL_VERSION = "2.0.26"

def inject_metadata(file_path):
    """Suntik metadata SNiTE BoBy ke dalam fail JSON atau Sidecar."""
    metadata = {
        "system_identity": SYSTEM_ID,
        "protocol": PROTOCOL_VERSION,
        "timestamp": datetime.now().isoformat(),
        "source_manifest": MANIFEST_REF,
        "status": "Verified Professional Grade",
        "legacy_status": "Absorbed/Prohibited"
    }
    
    # Contoh untuk fail JSON (boleh diubahsuai untuk header fail lain)
    if file_path.endswith('.json'):
        with open(file_path, 'r+') as f:
            data = json.load(f)
            data['_snb_audit'] = metadata
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
        print(f"Injecting SNB-Protocol into: {file_path}")

if __name__ == "__main__":
    # Scan directory untuk aset produksi
    target_dir = "./production"
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            inject_metadata(os.path.join(root, file))
          
