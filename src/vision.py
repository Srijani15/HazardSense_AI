import cv2
from src.hazard_engine import assess_hazards

def detect_objects(image_path):
    """
    Load an image and return detected objects (mocked for now)
    """
    img = cv2.imread(image_path)
    if img is None:
        return []

    return ["staircase", "vehicle", "wet floor"]

def get_hazard_alerts(image_path):
    """
    Return hazard alerts (message + score) for a given image
    """
    objects = detect_objects(image_path)
    hazards = assess_hazards(objects)
    return hazards
