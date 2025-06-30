# Emotion Detection Application

This application uses IBM Watson NLP library to detect emotions in text. The application can identify five primary emotions:
- Anger
- Disgust
- Fear
- Joy
- Sadness

## Watson NLP Integration

The application leverages Watson NLP's advanced natural language processing capabilities to analyze text and determine emotional content. The emotion detection is performed using a pre-trained model that can accurately classify text into different emotional categories.

The implementation follows these key steps:
1. Text input validation
2. Emotion prediction using Watson NLP
3. Score normalization
4. Dominant emotion identification
5. Response formatting

## Emotion Detection Code

Here's the implementation of the emotion detection functionality:

![Emotion Detection Code](2a_emotion_detection.png)

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

## Emotion Detection Code

Here's the implementation of the emotion detection functionality:

![Emotion Detection Code](2a_emotion_detection.png)

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
