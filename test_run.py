# test_run.py
from src.controller import run_demo

# Demo images
images = [
    "assets/demo_images/staircase.jpg",
    "assets/demo_images/wetfloor.jpg",
    "assets/demo_images/vehicle.jpg"
]

for img in images:
    print(f"\nRunning demo for: {img}")
    run_demo(img)
