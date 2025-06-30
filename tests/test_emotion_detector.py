import unittest
from emotion_detector import emotion_predictor

class TestEmotionDetector(unittest.TestCase):
    def test_valid_input(self):
        result = emotion_predictor("I am so happy today!")
        self.assertEqual(result["code"], 200)
        self.assertIn("joy", result["data"]["scores"])
        
    def test_empty_input(self):
        result = emotion_predictor("")
        self.assertEqual(result["code"], 400)
        self.assertIn("error", result)
        
    def test_none_input(self):
        result = emotion_predictor(None)
        self.assertEqual(result["code"], 400)
        self.assertIn("error", result)
        
    def test_invalid_input(self):
        result = emotion_predictor(123)
        self.assertEqual(result["code"], 400)
        self.assertIn("error", result)

if __name__ == '__main__':
    unittest.main()
