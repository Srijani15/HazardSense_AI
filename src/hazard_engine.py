# hazard_engine.py

def assess_hazards(detected_objects):
    """
    detected_objects: list of strings
    returns: list of hazard warnings
    """

    hazards = []

    if "staircase" in detected_objects:
        hazards.append("Warning. Stairs ahead. Please proceed carefully.")

    if "vehicle" in detected_objects:
        hazards.append("Caution. Vehicle detected nearby.")

    if "wet floor" in detected_objects:
        hazards.append("Alert. Slippery surface detected.")

    if not hazards:
        hazards.append("No immediate hazards detected.")

    return hazards
