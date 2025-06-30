# 🧊 RGB-Thermal Image Overlay

This project overlays visible RGB imagery with aligned thermal imagery to create fused visualizations for inspection and analysis. It automates the processing of multiple image pairs using OpenCV.

🎯 Goal: Accurately align and overlay RGB and thermal image pairs into composite images.

---

## 📁 Folder Structure


<pre>
task1-rgb-thermal-overlay/
├── task_1_code.py           # Main Python script
├── input-images/            # Contains input RGB and thermal image pairs
├── task_1_output/           # Script output: overlaid images
├── screenshots/             # Screenshot samples of overlay
└── README.md                # This file
</pre>

---

## 📸 Sample Overlay

Below is an example overlay result from the script:

![Overlay Example](task_1_output/DJI_20250530121540_0001_AT.JPG)

---

## 🛠 Requirements

Install the following libraries:

pip install opencv-python numpy
Python version: 3.7+

▶️ How to Run
Place input files in the input-images/ folder:

RGB image: ends with _Z.JPG

Thermal image: ends with _AT.JPG

Run the script:
python task_1_code.py
Output will be saved to the   task_1_output.

📦 Input Naming Convention
The script automatically matches RGB and thermal image pairs using the common filename prefix:

File Type	Example Filename
RGB	DJI_20250530123037_0003_Z.JPG
Thermal	DJI_20250530123037_0003_AT.JPG
Output	DJI_20250530123037_0003_overlay.jpg

🧠 How It Works
Images are resized to match dimensions

RGB image is converted to grayscale and color-mapped

A weighted average of the RGB and thermal image is computed

Composite output is saved with overlay suffix

✅ Example Result
RGB (_Z)	Thermal (_AT)	→ Overlay
input RGB	input thermal	output overlay

📂 Sample Input & Output
input-images/DJI_..._Z.JPG

input-images/DJI_..._AT.JPG

output-images/DJI_..._overlay.jpg

🧪 Notes
Make sure both RGB and thermal images are perfectly aligned

The script uses simple averaging overlay (can be extended with alpha blending or color map tuning)

💡 Credits
Created as part of an AI Engineering assignment to demonstrate image fusion for field inspection workflows.

📬 Contact
GitHub: github.com/basi1l
