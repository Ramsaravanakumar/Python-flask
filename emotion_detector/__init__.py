"""
Emotion Detector Package
=======================

This package provides functionality for detecting emotions in text using Watson NLP.

Modules:
--------
- emotion_detector: Main emotion detection functionality
- server: Flask server implementation
- tests: Unit tests for the package

Usage:
------
```python
from emotion_detector import emotion_predictor

# Example usage
result = emotion_predictor("I am feeling happy today")
```
"""

from .emotion_detector import emotion_predictor
