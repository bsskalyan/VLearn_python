import os
import sys
import shutil
from datetime import datetime


def backup_files(src_dir: str, dst_dir: str):
    # Validate source directory
    if not os.path.isdir(src_dir):
        print(f"❌ Source directory does not exist: {src_dir}")
        return

    # Validate destination directory
    if not os.path.isdir(dst_dir):
        print(f"❌ Destination directory does not exist: {dst_dir}")
        return

    for filename in os.listdir(src_dir):
        src_path = os.path.join(src_dir, filename)

        # Only handle files (skip subdirectories)
        if not os.path.isfile(src_path):
            continue

        dest_path = os.path.join(dst_dir, filename)

        # If file already exists in destination, append timestamp
        if os.path.exists(dest_path):
            name, ext = os.path.splitext(filename)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            new_filename = f"{name}_{timestamp}{ext}"
            dest_path = os.path.join(dst_dir, new_filename)

        try:
            shutil.copy2(src_path, dest_path)
            print(f"✅ Backed up: {src_path} -> {dest_path}")
        except OSError as e:
            print(f"❌ Error copying {src_path} to {dest_path}: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
        sys.exit(1)

    source = sys.argv[1]
    destination = sys.argv[2]

    backup_files(source, destination)
