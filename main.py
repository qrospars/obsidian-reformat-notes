# DOn't forget to make a backup of your notes before running any reformatting

from operator import contains
from shutil import move
import os
import re


def moveTagsOutOfMetadata(folderAbsolutePath, filename):
    # Check if the notes has the tags in the metadata
    try:
        with open(os.path.join(folderAbsolutePath, filename), 'r+') as f:
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


for filename in os.listdir(r"C:\Users\quentin.rospars\Documents\Sync\Notes"):
    moveTagsOutOfMetadata(
        r"C:\Users\quentin.rospars\Documents\Sync\Notes", filename)
