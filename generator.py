import os
from url import url
from file_path import file_path
from main_qr import generate_qr_code

for number, (u, f) in enumerate(zip(url, file_path), start=1):
    link = u["url"].split("?")[0]          # drop the ?si=... tracking tag
    folder = f["file_path"]
    save_to = os.path.join(folder, f"qr_{number}.png")

    try:
        generate_qr_code(link, save_to)
    except OSError as error:
        print(f"Entry {number} failed: {error}")