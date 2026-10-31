# QR Code Generator

A small Python project that turns a list of URLs (such as YouTube links) into QR code images and saves each one as a PNG file.

## Features

- Generates a QR code for every URL in a list
- Saves each code as its own `.png` file (`qr_1.png`, `qr_2.png`, ...)
- Removes the `?si=...` tracking tag from links before encoding, giving simpler, easier-to-scan codes
- Keeps going if one entry fails, and prints which one

## Project Structure

```
.
├── generator.py   # Entry point: loops through the data and creates the codes
├── main_qr.py     # Contains generate_qr_code(url, file_path)
├── url.py         # List of URLs
├── file_path.py   # List of folders to save into
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

1. Open `url.py` and list your links:

```python
url = [{"url": "https://youtu.be/example1"},
       {"url": "https://youtu.be/example2"}]
```

2. Open `file_path.py` and list the folders where the images should be saved. Use one folder per URL, in the same order:

```python
file_path = [{"file_path": "C:\\Users\\YourName\\Desktop"},
             {"file_path": "C:\\Users\\YourName\\Documents"}]
```

3. Run the generator:

```
python generator.py
```

4. Find `qr_1.png`, `qr_2.png`, and so on in the folders you listed.

## How It Works

`generator.py` pairs the first URL with the first folder, the second with the second, and so on. For each pair it:

1. Removes the `?si=...` tracking tag from the link
2. Builds a file name such as `qr_1.png` inside the folder
3. Calls `generate_qr_code(url, file_path)` from `main_qr.py`, which creates and saves the image
4. Prints an error and moves on to the next entry if saving fails

## Notes

- **Matching order:** The two lists are paired by position, so URL number 2 goes with folder number 2. If you add, remove, or reorder an entry in one file, do the same in the other.
- **Equal lengths:** If one list is longer than the other, the extra entries are skipped silently.
- **Folders must exist:** Each folder in `file_path.py` has to exist on your computer, or that entry will fail.
- **Windows paths:** Use double backslashes (`C:\\Users\\...`) or a raw string (`r"C:\Users\..."`). A single backslash can cause a syntax error.
- **File names:** Names come from the entry number, so running the script again overwrites the earlier images.
- **Portability:** Folders that belong to one person's user account will not work on other computers.

## Troubleshooting

| Problem | Likely cause |
|---|---|
| `ModuleNotFoundError: No module named 'qrcode'` | Run `pip install qrcode pillow` |
| `ModuleNotFoundError: No module named 'main_qr'` (or `url`, `file_path`) | The file name does not match the import |
| `SyntaxError: (unicode error)` | Single backslashes in a Windows path |
| `Entry N failed: ...` | That folder does not exist or cannot be written to |
| Fewer images than expected | The two lists have different lengths |

## Ideas for Future Improvements

- Combine the two data files into one list, so each URL stays attached to its folder
- Use one shared output folder instead of per-user paths
- Better checks for empty or invalid URLs
- Custom colors and a logo in the center
- Reading links from a CSV or text file
- Automated tests with `pytest`

## License

Free to use for personal and learning projects.
