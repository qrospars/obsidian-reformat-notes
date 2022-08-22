# DOn't forget to make a backup of your notes before running any reformatting

from operator import contains
from shutil import move
import os
import re


def move_tags_out_of_metadata(folder_absolute_path, filename):
    """Move the tags out of the metadata since the links are not supported in metadata

    Args:
        folder_absolute_path (string): absolute path to the note folder
        filename (string): note file name
    """
    # Check if the notes has the tags in the metadata
    try:
        with open(os.path.join(folder_absolute_path, filename), 'r+') as f:
            file = f.read()
            file = re.sub(r"(Tags:.+)\n---", r"---\n\1", file)
            # Setting the position to the top
            # of the page to insert data
            f.seek(0)
            # # Writing replaced data in the file
            f.write(file)
            # # Truncating the file size
            f.truncate()
    except:
        return


notes_absolute_path = r"C:\Users\quentin.rospars\Documents\Sync\Notes"
for filename in os.listdir(notes_absolute_path):
    move_tags_out_of_metadata(notes_absolute_path, filename)
