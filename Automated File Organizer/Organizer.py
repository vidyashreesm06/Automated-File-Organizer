from pathlib import Path
import shutil

# Define the category folders and their file extensions
DIRECTORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".csv", ".pptx", ".md"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a", ".wma"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".flv", ".wmv", ".webm"],
    "Code": [".py", ".js", ".html", ".css", ".json"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
    "Setup": [".exe", ".dmg", ".pkg"],
}


def organize_folder(target_folder):
    path = Path(target_folder)

    if not path.exists():
        print(f"Error: The path '{target_folder}' does not exist.")
        return

    # Loop through all items in the folder
    for item in path.iterdir():
        # Only process files (skip folders)
        if item.is_file():
            # Skip the script itself and README if run inside the target folder
            if item.resolve() == Path(__file__).resolve() or item.name.lower() == "readme.md":
                continue

            file_extension = item.suffix.lower()
            moved = False

            # Check which category matches the extension
            for category, extensions in DIRECTORIES.items():
                if file_extension in extensions:
                    category_folder = path / category
                    category_folder.mkdir(exist_ok=True)  # Create folder if missing

                    # Move the file
                    dest_file = category_folder / item.name
                    shutil.move(str(item), str(dest_file))
                    print(f"Moved: {item.name} -> {category}/")
                    moved = True
                    break

            # If the extension doesn't match any category, put it in 'Others'
            if not moved:
                others_folder = path / "Others"
                others_folder.mkdir(exist_ok=True)
                dest_file = others_folder / item.name
                shutil.move(str(item), str(dest_file))
                print(f"Moved: {item.name} -> Others/")

    print("Organization complete!")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        target = sys.argv[1].strip().strip('"\'')
    else:
        target = input("Enter the path of the folder you want to organize (or press Enter for current folder): ").strip().strip('"\'')
        if not target:
            target = "."
    organize_folder(target)
