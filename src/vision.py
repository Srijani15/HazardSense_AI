# vision.py

from hazard_engine import assess_hazards

def mock_detect_objects():
    # Simulated detections (replace with Azure Vision later)
    return ["staircase", "wet floor"]

if __name__ == "__main__":
    objects = mock_detect_objects()
    warnings = assess_hazards(objects)

    for w in warnings:
        print(w)
