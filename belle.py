#!/usr/bin/env python

from genericpath import isdir, isfile
import shutil
import os

root_folder = "/storage/01/pussy/collections/random/belle-delphine/"
photos_folder = os.path.join(root_folder, "photos")
video_folder = os.path.join(root_folder, "videos")


def check_folder(folder):
    try:
        os.listdir(folder)
        return True
    except:
        return False

def crawl_for_files(folder):
    data = []
    if not check_folder(folder): return None
    for file in os.listdir(folder):
        combined = os.path.join(folder, file)
        if os.path.isdir(combined):
            for subitem in crawl_for_files(combined):
                data.append(subitem)
        elif os.path.isfile(combined):
            data.append(combined)
    return data

def get_extension(file):
    filename, extension = os.path.splitext(file)
    return extension

def isphoto(file):
    photo_extensions = [".jpg", ".JPG", ".png", ".jpeg", ".PNG"]
    if get_extension(file) in photo_extensions:
        return True
    return False

def normalize(file):
    pass



if not check_folder(root_folder): raise Exception("specified folder does not exist")



# loook through all photo directories and see if there is a video and if so
# propose a move from there to videos directory as a first pass

# also think about changing from, i.e, April 2022 to 04-2022

# need to normalize file extension caputaliza

for file in crawl_for_files(photos_folder):
    if not isphoto(file):
        print(file)
        shutil.copy(file, video_folder)