"""
removes useless files in subdir
"""

from lib.file import crawl_for_files, ismedia
import os

root_folder = "/storage/02/"

files = crawl_for_files(root_folder)

for file in files:
    if not ismedia(file):
        print("found a shitty file, %s" % file)
        #os.remove(file)