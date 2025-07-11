# ⚽ Football Player Re-Identification Analysis

An end-to-end football video analysis system that uses **YOLOv8** object detection and **OpenCV** tracking to identify and analyze player movement from broadcast footage.
---

Final Output Image:


<img width="1812" height="835" alt="image" src="https://github.com/user-attachments/assets/b868c2f8-9bf9-4c45-9047-a9ba14d12a97" />

---

## 🔍 Overview

This project implements a real-time football player tracking pipeline:
- Detects players using **YOLOv8**.
- Assigns unique IDs and tracks their movements using **Deep SORT**.
- Calculates player statistics such as **distance covered**, **speed**, and **heatmaps**.
- Supports **multi-camera footage** and **custom video input**.

---

## 🧠 Tech Stack

| Technology | Role |
|------------|------|
| [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) | Object Detection |
| OpenCV | Image Processing & Video Handling |
| NumPy | Coordinate Calculations |
| Matplotlib | Data Visualization |
| Python | Backend Logic |

---

## 🚀 Features

✅ Detects and tracks players in real-time  
✅ Annotates players with ID and bounding boxes  
✅ Visualizes movement and distance covered  
✅ Multi-angle camera support  
✅ Easily customizable for your own videos

---

## 📂 Project Structure

football-analysis-yolo/
│
├── input_videos/ # Input match footage
├── output_videos/ # Results with annotations
├── utils/ # Utility scripts
│ ├── tracker.py # Object tracker logic
│ └── distance_calc.py # Player movement logic
│
├── main.py # Main execution script
├── requirements.txt # Python dependencies
└── README.md


---

## 📸 Sample Output

![Sample Output](https://github.com/YOUR_USERNAME/football-analysis-yolo/assets/sample_output.gif)

---

## ⚙️ Installation

Download YOLOv11 best model weights

python
Copy
Edit
from ultralytics import YOLO
model = YOLO('best.pt')  # or yolov11s.pt for more accuracy

📊 Future Work
Integrate possession tracking

Add player heatmaps

Live stream support

Generate post-match PDF reports

🙌 Credits
Inspired by rohithr2511/Re-Identification-Football-Analysis
Built using Ultralytics YOLOv11

🧠 License
MIT License - free to use and modify for educational & non-commercial purposes.

⭐ Show Your Support
If you found this project useful, please consider giving it a ⭐ on GitHub!


Let me know if you want a version with:
- Better visuals (GIFs or screenshots)
- A different color/markdown style (e.g. dark mode preview, shields.io badges, etc.)

