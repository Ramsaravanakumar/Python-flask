# Emotion Detection Application

This application uses Watson NLP to detect emotions in text.

## Project Structure

```
Python-flask/
├── README.md              # Project documentation
├── emotion_detector.py    # Main emotion detection logic
├── requirements.txt       # Project dependencies
├── server.py             # Flask server implementation
└── tests/               # Test directory
    └── test_emotion_detector.py  # Unit tests
```

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python server.py
```

## API Endpoints

### POST /emotion_detector

Detects emotions in the provided text.

Request Body:
```json
{
    "text": "Your text here"
}
```

Response:
```json
{
    "code": 200,
    "data": {
        "emotion": "dominant_emotion",
        "scores": {
            "anger": 0.0,
            "disgust": 0.0,
            "fear": 0.0,
            "joy": 0.0,
            "sadness": 0.0
        }
    }
}
```

## Testing

Run tests using:
```bash
python -m pytest tests/
```
