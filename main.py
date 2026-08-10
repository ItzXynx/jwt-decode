import sys
import base64
import json
from datetime import datetime, timezone

def decode_part(p):
    try:
        return json.loads(base64.urlsafe_b64decode(p + "=="))
    except:
        return {}

if __name__ == "__main__":
    token = sys.argv[1]
    parts = token.split(".")
    if len(parts) != 3:
        print("not a valid jwt")
        sys.exit()
    
    header = decode_part(parts[0])
    payload = decode_part(parts[1])
    
    print("header:", json.dumps(header, indent=2))
    print("payload:", json.dumps(payload, indent=2))
    
    exp = payload.get("exp")
    if exp:
        expired = datetime.now(timezone.utc).timestamp() > exp
        print(f"expired: {expired}")
# updated
