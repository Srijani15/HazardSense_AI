from src.vision import get_hazard_alerts
from src.voice_alerts import speak_warnings

def run_demo(image_path):
    """
    Run demo: print and speak hazards
    """
    hazards = get_hazard_alerts(image_path)
    print("Detected hazards (sorted by risk):")
    for msg, score in hazards:
        print(f"{msg} (score {score})")
    speak_warnings(hazards)
