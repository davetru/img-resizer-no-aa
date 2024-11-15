# Batch Image Resizer with Pixelated Scaling

This Python program batch-resizes images within a directory tree while preserving their pixelated appearance by avoiding anti-aliasing. It uses the [Pillow (PIL)](https://pillow.readthedocs.io/) library to upscale `.png` and `.jpg` images by a user-defined multiplier. The resized images are saved in a corresponding directory structure under a specified output directory.

## Features

- Recursively processes all subdirectories within the input directory.
- Resizes images using the nearest-neighbor interpolation method (`Image.NEAREST`) to maintain pixelation.
- Outputs resized images into a new directory while preserving the input directory's structure.

## Requirements

- Python 3.6 or higher
- Pillow library

To install Pillow, run:

```bash
pip install Pillow
```

## Usage

1. Place your images into a `sprites` directory (or modify the script to use a different directory).
2. Adjust the `new_size_multiplier` variable in the script to set the resizing factor. For example: `new_size_multiplier = 10` will enlarge the images by 10 times their original dimensions.
3. Run the script: `python resizer.py`
4. The resized images will be saved in the `resized_sprites` directory (or whichever output directory you define).

## Directory Structure

Before running the script:
```
project/
│
├── sprites/
│   ├── image1.png
│   ├── image2.jpg
│   ├── subdir/
│       ├── image3.png
│
└── resizer.py
```

After running the script:
```
project/
│
├── sprites/
│   ├── image1.png
│   ├── image2.jpg
│   ├── subdir/
│       ├── image3.png
│
├── resized_sprites/
│   ├── image1.png
│   ├── image2.jpg
│   ├── subdir/
│       ├── image3.png
│
└── resizer.py
```

# Configuration

## Input Directory
Set the `input_dir` variable to the directory path containing your images. By default, it is:
`input_dir = "sprites"`

## Output Directory
Set the `output_dir` variable to the desired path for saving resized images. By default, it is:
`output_dir = "resized_sprites"`

## Resizing Multiplier
Set the `new_size_multiplier` variable to the desired scale factor. For example:
`new_size_multiplier = 10`

# How It Works

1. The script traverses the input directory tree using `os.walk()`.
2. For each image file (`.png` or `.jpg`), it opens the image using Pillow's `Image.open()`.
3. The script resizes the image using the nearest-neighbor interpolation method to preserve pixelation.
4. The resized image is saved to the corresponding subdirectory in the output directory.

## Error Handling

If any error occurs during image processing, the script will display the filename and the error message in the terminal.

## Example Output

When processing `image1.png` (100x100) with `new_size_multiplier = 10`, the output will be:
- Original dimensions: 100x100
- Resized dimensions: 1000x1000
- Resized image: Saved in `resized_sprites/image1.png`

## License

This project is open-source and available under the MIT License.

## Author

Created by David Tru Tran.

#  Acknowledgments

Thanks to the Pillow library for making image processing simple and efficient!
