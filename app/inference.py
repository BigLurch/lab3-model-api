import base64
import io
from typing import List, Tuple

import torch
from PIL import Image
from torchvision import transforms

CIFAR10_CLASSES: List[str] = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck",
]

_preprocess = transforms.Compose(
    [
        transforms.Resize((32, 32)),
        transforms.ToTensor(),
        transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2470, 0.2435, 0.2616)),
    ]
)


def decode_image_b64(image_b64: str) -> Image.Image:
    raw = base64.b64decode(image_b64)
    img = Image.open(io.BytesIO(raw)).convert("RGB")
    return img


@torch.no_grad()
def predict_image(
    model: torch.jit.ScriptModule, image: Image.Image
) -> Tuple[int, str, float]:
    x = _preprocess(image).unsqueeze(0)
    logits = model(x)
    probs = torch.softmax(logits, dim=1)
    conf, pred = torch.max(probs, dim=1)

    class_id = int(pred.item())
    confidence = float(conf.item())
    class_name = CIFAR10_CLASSES[class_id]
    return class_id, class_name, confidence
