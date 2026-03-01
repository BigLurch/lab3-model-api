from pydantic import BaseModel, Field


class PredictRequest(BaseModel):
    image_b64: str = Field(..., description="Base64-encoded image (jpg/png)")


class PredictResponse(BaseModel):
    class_id: int
    class_name: str
    confidence: float
