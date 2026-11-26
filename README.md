# Object Detection and Tracking Using YOLO

## About the Project
This project is an AI-based Object Detection and Tracking system developed using Python, OpenCV, and YOLO11.

It uses a pretrained YOLO11n model to detect objects in real time through a webcam and track detected objects across video frames.

## Features
- Real-time object detection using a webcam.
- Object tracking using ByteTrack.
- Bounding boxes around detected objects.
- Object labels and tracking IDs.
- Live video display.
- Press `q` to stop the application.

## Technologies Used
- Python
- YOLO11 (Ultralytics)
- OpenCV
- ByteTrack

## Project Structure

```text
Object_Detection_Tracking/
│
├── main.py
└── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ANITHA-R-1710/Object_Detection.git
```

### 2. Navigate to the Project Folder

```bash
cd Object_Detection
```

### 3. Install Required Libraries

```bash
pip install ultralytics opencv-python
```

## How to Run

Run the following command:

```bash
python main.py
```

The webcam will open, and the system will start detecting and tracking objects automatically.

Press **q** to stop the application.

## How It Works

1. The system accesses the webcam using OpenCV.
2. YOLO11 detects objects in each video frame.
3. ByteTrack tracks detected objects across frames.
4. Bounding boxes and object labels are displayed on the screen.
5. Tracking IDs help distinguish individual tracked objects.

## Applications
- Smart surveillance systems
- Traffic monitoring
- Real-time object tracking
- Security applications
- Automated monitoring systems

## Author
**Anitha R**

B.Tech – Artificial Intelligence and Data Science

GitHub: https://github.com/ANITHA-R-1710

---

*Developed as part of the CodeAlpha AI Internship.*
