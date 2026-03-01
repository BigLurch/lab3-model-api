from pathlib import Path

import torch
from fastapi import FastAPI, HTTPException

from app.inference import decode_image_b64, predict_image
from app.schemas import PredictRequest, PredictResponse

REPO_ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = (REPO_ROOT / "model_store" / "model.ts").resolve()

app = FastAPI(title="Lab3 Model API", version="0.1.0")


def load_model() -> torch.jit.ScriptModule:
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model file not found at: {MODEL_PATH}")
    with open(MODEL_PATH, "rb") as f:
        model = torch.jit.load(f, map_location="cpu")

    model.eval()
    return model


model = load_model()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    try:
        img = decode_image_b64(req.image_b64)
        class_id, class_name, confidence = predict_image(model, img)
        return PredictResponse(
            class_id=class_id, class_name=class_name, confidence=confidence
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
