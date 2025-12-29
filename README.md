# HazardSense-AI

## Helping Visually Impaired People Navigate Safely

While helping my visually impaired cousin, I realized most apps tell you “what” is around you, but not “what’s dangerous.” HazardSense-AI focuses on **hazard awareness first** — stairs, wet floors, vehicles, or other obstacles — and gives short, clear voice alerts.

### How It Works
1. A camera captures the environment (mocked for now).  
2. Detected objects are passed to our **hazard engine**.  
3. The engine prioritizes risks and generates short warnings.  
4. Voice alerts inform the user in real-time.

Example alerts:
- “Warning: stairs ahead!”  
- “Caution: slippery floor.”  
- “No immediate hazards detected.”

### Tech Stack
- Python  
- OpenCV (mocked image input)  
- PyTTSX3 for voice alerts  
- Rule-based hazard assessment  

### Folder Structure
HazardSense-AI/
├── src/
│ ├── vision.py
│ ├── hazard_engine.py
│ └── voice_alerts.py
├── assets/
│ └── demo_images/
├── docs/
├── README.md
└── requirements.txt

### Future Improvements
- Real-time video detection with Azure Computer Vision  
- Bluetooth or bone-conduction audio output  
- Distance estimation for hazards  
- Indoor navigation for smart buildings  

HazardSense-AI is simple, safe, and demonstrates a **practical application of AI for accessibility**.