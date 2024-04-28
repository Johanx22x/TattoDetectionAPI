from flask import Flask, request, jsonify
from yolo_tattoo import perform_object_detection

app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect_objects():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'})
    
    image_file = request.files['image']
    
    # Perform object detection
    detections = perform_object_detection(image_file)

    print(detections)

    # Create a list to store the results
    # with over 70% confidence
    results = []
    for detection in detections:
        if detection['score'] > 0.7:
            results.append(detection)

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
