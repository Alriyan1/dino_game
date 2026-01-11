# control_dino 🦖

**control_dino** is a simple screen-capture-based controller for the Chrome offline Dinosaur game (T-Rex). It watches a region of your screen for obstacles and automatically presses Space to make the dinosaur jump.

---

## 🔧 Features

- Real-time screen capture using `mss` and `pyautogui`.
- Simple image preprocessing and contour detection with `OpenCV` and `cvzone`.
- Auto jump when an obstacle is detected within a configurable distance.
- Lightweight and easy to tweak for different screen sizes and game positions.

---

## 🧩 Requirements

- Python 3.8+ (tested on Windows)
- Libraries:
  - `opencv-python`
  - `mss`
  - `numpy`
  - `pyautogui`
  - `cvzone`

Install the dependencies with pip:

```bash
pip install opencv-python mss numpy pyautogui cvzone
```

> Tip: Use a virtual environment (venv/conda) to keep requirements isolated.

---

## 🚀 Usage

1. Open the Chrome T-Rex dinosaur game (chrome://dino) or the offline game in a browser and position the game window on your screen.
2. Adjust the capture region in `main.py` if needed (see **Configuration** below).
3. Run the script:

```bash
python main.py
```

4. A window titled `Game` will appear showing the captured region with annotated contours. Press `Esc` to quit.

---

## ⚙️ Configuration & Tuning

Key values are in `main.py`:

- Screen capture region (mss):
  - `capture_screen_region_opencv_mss(x, y, width, height)` — tune `x`, `y`, `width`, `height` to match your game window.
- Crop area inside the captured frame:
  - `cp = (start_row, end_row, start_col)` — controls the image area processed for obstacles.
- Jump threshold:
  - `game_logic(..., jump_distance=90)` — lower makes the dino jump later, raise to jump earlier.

If the script misses obstacles or jumps too early, try:
- Increasing `jump_distance` to detect obstacles sooner.
- Adjusting `cp` and the capture coordinates to ensure the obstacle region is fully inside the processed area.

---

## 🐞 Troubleshooting

- If nothing happens when you run the script:
  - Verify dependencies are installed.
  - Confirm the game window is visible and the capture region covers the game area.
  - Run with prints/logging or temporarily show intermediate windows (`imgCrop`, `imgContour`) by uncommenting lines in `main.py`.

- If the script spams jumps:
  - Increase `minArea` in `find_contours` (currently `minArea=100`) or tune morphological steps in `preprocess()`.

---

## ⚖️ Credits

- Built with `OpenCV`, `mss`, `pyautogui`, and `cvzone`.

---

If you'd like, I can add a `requirements.txt`, a configuration file to store the capture coordinates, or small CLI flags to make tuning easier—tell me which you'd prefer! ✅
