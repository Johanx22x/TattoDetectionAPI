import yolov5
from PIL import Image
from io import BytesIO
from time import sleep
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

# Function to perform object detection using YOLOv5
def perform_object_detection(image_file):
    # Load your trained YOLOv5 model
    model_weights = "./weights.pt"
    # You should have your model weights saved after training
    model = yolov5.load(model_weights)

        # set model parameters
    model.conf = 0.25  # NMS confidence threshold
    model.iou = 0.45  # NMS IoU threshold
    model.agnostic = False  # NMS class-agnostic
    model.multi_label = False  # NMS multiple labels per box
    model.max_det = 1000  # maximum number of detections per image

    # Read the image data from the file stream
    image = Image.open(BytesIO(image_file.read())).convert('RGB')
    
    # Perform object detection
    results = model(image)  # Modify this function call to match your YOLOv5 inference function

    # parse results
    predictions = results.pred[0]
    boxes = predictions[:, :4] # x1, y1, x2, y2
    scores = predictions[:, 4]

    # Serialize boxes and scores
    detections = []
    for box, score in zip(boxes.tolist(), scores.tolist()):
        detection = {
            'box': box,
            'score': score
        }
        detections.append(detection)
    
    return detections