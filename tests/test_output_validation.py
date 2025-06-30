import unittest
from emotion_detector.emotion_detector import emotion_predictor

class TestOutputValidation(unittest.TestCase):
    def test_success_output_format(self):
        """Test successful response format"""
        result = emotion_predictor("I am feeling happy today")
        
        # Validate overall structure
        self.assertIn("code", result)
        self.assertIn("data", result)
        self.assertEqual(result["code"], 200)
        
        # Validate data structure
        data = result["data"]
        self.assertIn("emotion", data)
        self.assertIn("scores", data)
        
        # Validate scores structure
        scores = data["scores"]
        expected_emotions = ["anger", "disgust", "fear", "joy", "sadness"]
        
        for emotion in expected_emotions:
            self.assertIn(emotion, scores)
            self.assertIsInstance(scores[emotion], (int, float))
            self.assertGreaterEqual(scores[emotion], 0.0)
            self.assertLessEqual(scores[emotion], 1.0)

    def test_error_output_format(self):
        """Test error response format"""
        result = emotion_predictor("")
        
        # Validate error structure
        self.assertIn("code", result)
        self.assertIn("error", result)
        self.assertEqual(result["code"], 400)
        self.assertIsInstance(result["error"], str)

    def test_internal_error_format(self):
        """Test internal error response format"""
        # This test assumes we have a way to trigger internal errors
        # In practice, you would mock the emotion predictor to raise an exception
        pass

if __name__ == '__main__':
    unittest.main()
