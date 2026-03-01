import base64

import requests

with open("scripts/test.jpg", "rb") as f:
    b64 = base64.b64encode(f.read()).decode("utf-8")

resp = requests.post(
    "http://localhost:8000/predict",
    json={"image_b64": b64},
    timeout=30,
)

print(resp.status_code)
print(resp.json())
