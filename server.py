from flask import Flask, request, jsonify
from emotion_detector import emotion_predictor

app = Flask(__name__)

@app.route('/emotion_detector', methods=['POST'])
def detect_emotion():
    try:
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({
                "code": 400,
                "error": "No text was provided"
            }), 400
            
        text = data['text']
        result = emotion_predictor(text)
        
        if result["code"] != 200:
            return jsonify(result), result["code"]
            
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({
            "code": 500,
            "error": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
