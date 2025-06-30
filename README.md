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
├── setup.py              # Package setup
├── requirements.txt      # Project dependencies
├── emotion_detector/     # Package directory
│   ├── __init__.py      # Package initialization
│   ├── emotion_detector.py  # Main emotion detection logic
│   └── server.py        # Flask server implementation
└── tests/               # Test directory
    └── test_emotion_detector.py  # Unit tests
```

## Package Installation

The application can be installed as a Python package:

1. Install in development mode:
```bash
pip install -e .
```

2. Or install as a package:
```bash
pip install .
```

3. Run the application using the installed package:
```bash
emotion-detector
```

## Emotion Detection Code

Here's the implementation of the emotion detection functionality:

![Emotion Detection Code](2a_emotion_detection.png)

## Setup

### Prerequisites

Before using the application, ensure you have Python 3.8 or higher installed on your system.

### Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

The application requires the following libraries:
- Flask: For the web server
- Watson NLP: For emotion detection
- pytest: For running tests
- flake8: For code analysis

### Importing the Application

The application can be imported in two ways:

1. As a standalone module:
```python
from emotion_detector import emotion_predictor

# Example usage
result = emotion_predictor("I am feeling happy today")
```

2. Through the Flask server (recommended):
```bash
python server.py
```

The server will start on http://localhost:5000 by default.

## API Endpoints

### POST /emotion_detector

Detects emotions in the provided text.

#### Request Body
```json
{
    "text": "Your text here"
}
```

#### Success Response (200)
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

#### Error Response (400)
```json
{
    "code": 400,
    "error": "No text was provided"
}
```

#### Error Response (500)
```json
{
    "code": 500,
    "error": "Internal server error"
}
```

### Output Format Validation

The output format is strictly validated to ensure:
1. Consistent response structure
2. Proper error handling
3. Accurate emotion scoring
4. Correct dominant emotion identification

#### Validation Rules

1. Success Response (200):
   - Must contain `code` and `data` keys
   - `code` must be 200
   - `data` must contain:
     - `emotion`: string value of dominant emotion
     - `scores`: dictionary containing all 5 emotions with float values between 0.0 and 1.0

2. Error Response (400):
   - Must contain `code` and `error` keys
   - `code` must be 400
   - `error` must be a string describing the error

3. Internal Error Response (500):
   - Must contain `code` and `error` keys
   - `code` must be 500
   - `error` must be a string describing the internal error

#### Example Validation Code
```python
import emotion_detector

# Example text
result = emotion_detector.emotion_predictor("I am feeling happy today")

# Validate success response
assert result["code"] == 200
assert "data" in result
assert "emotion" in result["data"]
assert "scores" in result["data"]

# Validate scores
scores = result["data"]["scores"]
for emotion in ["anger", "disgust", "fear", "joy", "sadness"]:
    assert emotion in scores
    assert 0.0 <= scores[emotion] <= 1.0

# Validate error response
result = emotion_detector.emotion_predictor("")
assert result["code"] == 400
assert "error" in result
assert isinstance(result["error"], str)
```

#### Running Output Validation Tests

You can run the output validation tests using:
```bash
python -m pytest tests/test_output_validation.py -v
```

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
