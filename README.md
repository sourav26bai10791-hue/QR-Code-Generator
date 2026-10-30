# QR Code Generator

A small Python project that turns URLs (such as YouTube links) into QR code images and saves them as PNG files.

## Features

- Generates a QR code from any URL
- Saves each code as a `.png` image
- Stores a list of links and save locations in one place (`inputs.py`)

## Project Structure

```
.
├── main_qr.py    # Contains generate_qr_code(url, file_path)
├── inputs.py     # Dictionary of URLs and where to save each QR code
└── README.md
```

## Requirements

- Python 3.8 or newer
- The `qrcode` library
- The `Pillow` library (needed to save images)

## Installation

1. Download or clone this project.
2. Install the dependencies:

```
pip install qrcode pillow
```

## Usage

1. Open `inputs.py` and add or edit your entries. Each entry has a name, a URL, and a save location:

```python
inputs = {
    "input1": {
        "url": "https://youtu.be/example",
        "file_path": "C:\\Users\\YourName\\Documents\\qr_input1.png"
    },
}
```

2. Run the script:

```
python main_qr.py
```

3. Find your QR code images in the folders you set in `file_path`.

## Notes

- **Windows paths:** Use double backslashes (`C:\\Users\\...`) or a raw string (`r"C:\Users\..."`). A single backslash can cause a syntax error.
- **File names:** `file_path` must be a full file name ending in `.png`, not just a folder.
- **File name match:** The import in `main_qr.py` must match the file name. If the file is called `inputs.py`, use `from inputs import inputs`.
- **Tracking tags:** The `?si=...` part of a YouTube link is only a tracking tag. You can remove it to get a simpler, easier-to-scan QR code.
- **Portability:** Paths that point to one person's user folder will not work on other computers. Use a shared output folder if you plan to share the project.

## Troubleshooting

| Problem | Likely cause |
|---|---|
| `ModuleNotFoundError: No module named 'qrcode'` | Run `pip install qrcode pillow` |
| `ModuleNotFoundError: No module named 'inputs'` | The file name and the import do not match |
| `SyntaxError: (unicode error)` | Single backslashes in a Windows path |
| Nothing happens when running | The script defines the function but never calls it |
| Error when saving | `file_path` is a folder, or the folder does not exist |

## Ideas for Future Improvements

- Error handling for bad URLs and missing folders
- Custom colors and a logo in the center
- Reading links from a CSV or text file
- Command-line options for URL and output folder
- Automated tests with `pytest`

## License

Free to use for personal and learning projects.
