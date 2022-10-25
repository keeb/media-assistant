#!/usr/bin/env python

from genericpath import isdir, isfile
from lib.file import crawl_for_files, crawl_for_folders, check_folder, isphoto
import shutil
import os

root_folder = "/storage/01/pussy/collections/belle-delphine/"
photos_folder = os.path.join(root_folder, "photos")
video_folder = os.path.join(root_folder, "videos")


if not check_folder(root_folder): raise Exception("specified folder does not exist")

# loook through all photo directories and see if there is a video and if so
# propose a move from there to videos directory as a first pass

# also think about changing from, i.e, April 2022 to 04-2022

# need to normalize file extension caputaliza

months = ["", "January", "February", "March", "April", "May", "June", \
     "July", "August", "September", "October", "November", "December"]

for folder in crawl_for_folders(photos_folder):
    folder_name = folder.split(os.sep)[-1]
    print (folder_name)
    #print(folder_name)
    #shutil.copy(file, video_folder)