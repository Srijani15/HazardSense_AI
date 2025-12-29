from src.hazard_engine import assess_hazards

def detect_objects(image_path):
    """
    Simple mock detection based on filename keywords.
    Returns a list of detected hazards.
    """
    image_name = image_path.lower()

    detected = []

    if "stair" in image_name:
        detected.append("staircase")
    if "wet" in image_name or "floor" in image_name:
        detected.append("wet floor")
    if "vehicle" in image_name or "car" in image_name:
        detected.append("vehicle")
    if "pole" in image_name:
        detected.append("pole")
    if "drain" in image_name or "open" in image_name:
        detected.append("open drain")

    return detected


def get_hazard_alerts(image_path):
    """
    Returns sorted hazard alerts (message + score)
    """
    objects = detect_objects(image_path)
    hazards = assess_hazards(objects)
    return hazards
