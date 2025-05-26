# 🖼️ Batch Image Resizer with Pixelated Scaling

A Python utility to batch-resize images while preserving their pixelated charm. This tool recursively scans an input folder, resizes `.png` and `.jpg` images using nearest-neighbor scaling, and saves the output with the same folder structure elsewhere.

Perfect for resizing retro sprites, pixel art, or any images where sharp pixel edges matter.

---

## ✨ Features

* 🔁 Recursively processes all subfolders
* 🧱 Uses `Image.NEAREST` (no anti-aliasing) to preserve pixelated appearance
* 🗃️ Outputs to a parallel directory structure
* 🖼️ Supports `.png` and `.jpg` formats

---

## 📦 Requirements

* Python 3.6+
* Pillow (Python Imaging Library)

Install it with:

```bash
pip install pillow
```

---

## 🚀 How to Use

1. Place your original images inside a folder, e.g. `sprites/`
2. Open `resizer.py` and adjust these variables:

```python
input_dir = "sprites"             # Folder containing images
output_dir = "resized_sprites"    # Folder to save resized images
new_size_multiplier = 10          # Resize scale (e.g. 10x larger)
```

3. Run the script:

```bash
python resizer.py
```

---

## 🧩 Example Directory Structure

**Before:**

```
project/
├── sprites/
│   ├── hero.png
│   └── icons/
│       └── coin.jpg
└── resizer.py
```

**After:**

```
project/
├── sprites/           # original images remain untouched
├── resized_sprites/   # resized versions (same structure)
│   ├── hero.png
│   └── icons/
│       └── coin.jpg
└── resizer.py
```

---

## 🛠 Configuration

| Variable              | Description                                        |
| --------------------- | -------------------------------------------------- |
| `input_dir`           | Folder with original images                        |
| `output_dir`          | Folder to save resized copies                      |
| `new_size_multiplier` | Factor to scale up each image (e.g. 10 = 10x size) |

---

## ⚙️ How It Works

1. Traverses all folders using `os.walk()`
2. Filters image files by `.png` and `.jpg`
3. Opens them with Pillow’s `Image.open()`
4. Resizes with nearest-neighbor scaling to maintain pixel sharpness
5. Saves output in mirrored subdirectories

---

## ❗ Error Handling

If any image fails to process, the script prints the filename and error so you can debug without halting the batch.

---

## 📏 Example Output

With `new_size_multiplier = 10`, a 100×100 image becomes 1000×1000:

```
Original: hero.png (100x100)
Resized:  hero.png (1000x1000)
Saved to: resized_sprites/hero.png
```

---

## 📌 License

MIT License — free to use, modify, and distribute.

---

## 🧑‍💻 Author

Created by Dave Tran. Optimized for simplicity and sprite-perfect scaling.

---

## 🧠 Acknowledgments

Thanks to the Pillow library for making image processing fun and flexible!
