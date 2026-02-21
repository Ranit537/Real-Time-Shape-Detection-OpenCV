# 🎯 Real-Time Shape Detection (OpenCV)

Real-time shape detection system using **Python** and **OpenCV** that identifies geometric shapes such as **circles, triangles, rectangles, and polygons** using contour detection and image processing.

---

## 🚀 Features

* Live webcam detection
* Detects geometric shapes
* Adjustable edge detection thresholds
* Area filtering slider
* Bounding boxes + point count display
* Multi-window visualization panel
* Lightweight and fast processing

---

## 🖥️ Demo Preview

img_1.png

```
![Demo](demo.gif)
```

---

## 📦 Requirements

Install dependencies before running:

```
pip install opencv-python numpy
```

Or using requirements file:

```
pip install -r requirements.txt
```

---

## ▶️ How to Run

Clone repository:

```
git clone https://github.com/Ranit537/Real-Time-Shape-Detection-OpenCV.git
cd Real-Time-Shape-Detection-OpenCV
```

Run program:

```
python Obj_det.py
```

Press **Q** to exit webcam window.

---

## 🎛 Controls (Trackbars)

| Control    | Function                    |
| ---------- | --------------------------- |
| Threshold1 | Lower Canny edge threshold  |
| Threshold2 | Upper Canny edge threshold  |
| Area       | Minimum contour area filter |

Adjust these in the **Parameters window** while program runs.

---

## 🧠 How It Works

1. Capture webcam frame
2. Apply Gaussian blur
3. Convert to grayscale
4. Detect edges using Canny
5. Dilate edges
6. Find contours
7. Filter contours by area
8. Detect shape using polygon approximation
9. Draw bounding box and info text

---

## 🛠 Troubleshooting

**Camera not detected**

```
Change cv2.VideoCapture(0) → 1 or 2
```

**Black screen**

* Allow camera permissions
* Close other apps using camera

**Module not found**

```
pip install opencv-python numpy
```

---

## 📜 License

This project is licensed under the **MIT License** — feel free to use and modify.

---

## 👨‍💻 Author

**Ranit537**
GitHub: https://github.com/Ranit537

---

⭐ If you like this project, consider starring the repository!
