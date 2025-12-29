# HazardSense_AI 

A simple AI tool to help visually impaired people navigate safely. It detects hazards like stairs, wet floors, and vehicles, and gives voice alerts in real-time.


## What We Did

- Built a Python program to detect hazards from images.  
- Added risk scoring (stairs = high risk, wet floor = medium, etc.).  
- Voice alerts with `pyttsx3` to warn the user.  
- Prepared demo images for instant testing.  
- Everything is modular, so we can add more hazards or real AI later.


## How to Try It

1. Activate your virtual environment:

venv\Scripts\activate   # Windows
# or
source venv/bin/activate  # Mac/Linux

2. Run the demo:

python test_run.py

- Console prints detected hazards with scores.

- Voice alerts announce hazards automatically.

## Next Steps / Future Plans
Real-time camera detection.

Replace mock detection with real AI (YOLO / Azure).

Wearable or mobile app integration.

Multi-language voice alerts.

Cloud dashboard to monitor public hazards.