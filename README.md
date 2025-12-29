# HazardSense_AI – AI Assistant for the Visually Impaired

**Detect Hazards & Provide Real-Time Voice Alerts**

---

## Project Overview

HazardSense_AI is an AI-powered system designed to assist visually impaired individuals by detecting potential hazards in their environment and providing real-time voice alerts. The system identifies hazards such as:

- Stairs
- Wet floors
- Vehicles
- Open drains
- Poles

The system is lightweight, modular, and demo-ready for hackathons, with the ability to scale to real AI detection models like YOLO or Azure Computer Vision.

---

## Features

- Real-time hazard detection from images.
- Risk scoring for prioritizing hazards.
- Voice alerts using `pyttsx3`.
- Lightweight and easy to deploy.
- Hackathon-ready mock detection for fast demos.
- Modular code structure for easy future enhancements.

---

## Folder Structure

HazardSense_AI/
├── src/ # Source code
│ ├── init.py
│ ├── controller.py # Main logic to run hazard detection and voice alerts
│ ├── vision.py # Handles object detection
│ ├── hazard_engine.py # Assigns risk scores to detected hazards
│ ├── voice_alerts.py # Handles text-to-speech warnings
│ └── azure_vision_stub.py # Placeholder for future Azure integration
├── assets/ # Demo assets
│ └── demo_images/ # Sample images for demonstration
├── docs/ # Documentation (optional)
├── test_run.py # Script to run demo images
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .gitignore # Git ignore file

yaml
Copy code

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Srijani15/HazardSense_AI.git
cd HazardSense_AI
Create a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

Windows:

powershell
Copy code
venv\Scripts\activate
Mac/Linux:

bash
Copy code
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Place your demo images in assets/demo_images/

Run the demo script:

bash
Copy code
python test_run.py
Expected console output:

yaml
Copy code
Running demo for: assets/demo_images/staircase.jpg
Detected hazards (sorted by risk):
Warning: stairs ahead! (score 10)

Running demo for: assets/demo_images/wetfloor.jpg
Detected hazards (sorted by risk):
Alert: slippery surface! (score 7)

Running demo for: assets/demo_images/vehicle.jpg
Detected hazards (sorted by risk):
Caution: vehicle nearby! (score 9)
Voice alerts will also be played using pyttsx3.

Future Improvements
Real-time hazard detection from camera feed.

Replace mock detection with YOLO or Azure Computer Vision for real AI.

Mobile or wearable device integration.

Multi-language voice alerts.

Cloud dashboard for hazard monitoring.

Hackathon Demo
Three distinct demo images: staircase.jpg, wetfloor.jpg, vehicle.jpg

Distinct outputs and voice alerts for each hazard.

Easy to extend to additional hazards and real-time detection.

Technology Stack
Language: Python 3.11

Libraries: OpenCV, pyttsx3, Pillow

Optional Cloud Integration: Azure Computer Vision

Version Control: Git + GitHub

Environment: Virtualenv