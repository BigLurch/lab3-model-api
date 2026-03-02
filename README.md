# Lab3 - Model API (FastAPI + Docker)

Det här repot innehåller en deploybar ML-tjänst som laddar en exporterad PyTorch-modell (TorchScript) och exponerar en REST-API.

- Modell: TorchScript (`model_store/model.ts`)
- API: FastAPI
- Container: Docker
- Dependency management: uv

## Setup (lokalt)

### 1. Bygg Docker-imagen

```bash
docker build -t lab3-model-api .
```

### 2. Starta containern

```bash
docker run --rm -p 8000:8000 lab3-model-api
```

Applikationen kör nu på:

```text
http://localhost:8000
```

### 3. Testa API:t

Öppna Swagger UI i en webbläsare:

```text
http://localhost:8000/docs
```

#### Testa POST /predict

- Klicka på POST /predict
- Klicka på Try it out
- Ladda upp en bild (jpg/png)
- Klicka på Execute

Exempel på response:

```JSON
{
    "class_id": 5,
    "class_name": "dog",
    "confidence": 0.82
}
```

## Projektstruktur

```text
.
├── app/                # FastAPI-applikation
|   ├── __init__.py
|   ├── inference.py
|   ├── main.py
|   └── schemas.py
├── model_store/        # TorchScript-modell
|   └── model.ts
├── scripts/            # Test script
|   ├── test_predict.py
|   └── test_jpg
├── .dockerignore
├── .gitignore
├── .python-version
├── Dockerfile
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
```

## Uppfyller krav

- Modell exporterad till TorchScript
- POST /predict implementerad
- Dockerfile skapad
- Container går att bygga och starta
- API returnerar korrekt prediktion
- Utveckling skett via Feature Branches och Pull Requests

## Pull Requests

- PR 1 - FastAPI integration & Docker:
  https://github.com/BigLurch/lab3-model-api/pull/1

- PR 2 - Documentation update:
  https://github.com/BigLurch/lab3-model-api/pull/2
