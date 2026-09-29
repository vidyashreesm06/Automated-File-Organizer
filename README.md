# Automated File Organizer 📂

A simple yet powerful Python script designed to automatically sort and organize files in a target directory into neatly categorized folders based on their file extensions.

## ✨ Features

* **Automatic Categorization**: Sorts files into dedicated folders such as:
  * **Images** (`.jpg`, `.jpeg`, `.png`, `.gif`, etc.)
  * **Documents** (`.pdf`, `.docx`, `.txt`, `.pptx`, etc.)
  * **Videos & Audio** (`.mp4`, `.mkv`, `.mp3`, `.wav`, etc.)
  * **Archives & Others** (`.zip`, `.rar`, etc.)
* **Flexible Execution**: Run it on any specific folder path via command-line arguments, or let it prompt you interactively for the path.
* **Safe Handling**: Automatically creates destination folders if they do not already exist, preventing missing-directory errors.

---

## 🛠️ Tech Stack

* **Language**: Python 3
* **Libraries**: Built-in modules (`os`, `shutil`, `pathlib`, `sys`)

---

## 🚀 How to Use

1. Clone or download this repository.
2. Open your terminal and run the script:
   ```bash
   python organizer.py
