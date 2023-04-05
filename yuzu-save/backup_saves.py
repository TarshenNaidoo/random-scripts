import shutil
import os
import zipfile
import logging

# Set the path to the Yuzu saves directory
yuzu_saves_path = "C:\\Users\\Tarshen\\AppData\\Roaming\\yuzu\\nand"

# Set the path to the backup directory
backup_path = "G:\\My Drive\\"

def create_zip():
    try:
        # Create a zip file of the Yuzu saves directory
        with zipfile.ZipFile(backup_path + "yuzu_saves.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(yuzu_saves_path):
                for file in files:
                    zipf.write(os.path.join(root, file))
    except Exception as e:
        logging.exception("Error creating zip file")

def copy_zip():
    try:
        # Copy the zip file to the backup directory
        shutil.copyfile(backup_path + "yuzu_saves.zip", backup_path + "yuzu_saves_" + str(os.path.getctime(backup_path + "yuzu_saves.zip")) + ".zip")
    except Exception as e:
        logging.exception("Error copying zip file")

# Create a zip file and copy it to the backup directory
create_zip()
copy_zip()