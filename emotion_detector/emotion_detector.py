from watson_nlp import EmotionPredictor

def emotion_predictor(text):
    try:
        if not text or text.strip() == "":
            return {
                "code": 400,
                "error": "No text was provided"
            }
            
        predictor = EmotionPredictor()
        result = predictor.predict(text)
        
        emotion_scores = {
            "anger": result["anger"],
            "disgust": result["disgust"],
            "fear": result["fear"],
            "joy": result["joy"],
            "sadness": result["sadness"]
        }
        
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        return {
            "code": 200,
            "data": {
                "emotion": dominant_emotion,
                "scores": emotion_scores
            }
        }
    except Exception as e:
        return {
            "code": 500,
            "error": str(e)
        }
