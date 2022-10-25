import os

def get_folder_contents(path): 
    return os.listdir(path)

def crawl_for_files(folder):
    data = []
    if not check_folder(folder): return None
    for file in os.listdir(folder):
        combined = os.path.join(folder, file)
        if os.path.isdir(combined):
            try:
                for subitem in crawl_for_files(combined):
                    data.append(subitem)
            except:
                print("think we found a dead end.. %s" % combined)
        elif os.path.isfile(combined):
            data.append(combined)
    return data

def crawl_for_folders(folder):
    data = []
    for file in os.listdir(folder):
        combined = os.path.join(folder, file)
        if os.path.isdir(combined):
            data.append(combined)
            for subitem in crawl_for_folders(combined):
                data.append(subitem)
    return data

def get_extension(file):
    filename, extension = os.path.splitext(file)
    return extension

def isphoto(file):
    photo_extensions = [".jpg", ".png", ".jpeg", ".gif"]
    if get_extension(file.lower()) in photo_extensions:
        return True
    return False

def ismovie(file):
    movie_extensions = [".mp4", ".mkv", ".mpg", ".mpeg", ".avi", ".flv", ".wmv", \
        ".webm", ".m4v", ".ts"]
    if get_extension(file.lower()) in movie_extensions:
        return True
    return False

def isaudio(file):
    audio_extensions = [".mp3", ".flac", ".ogg"]
    if get_extension(file.lower()) in audio_extensions:
        return True
    return False

def issubtitle(file):
    sub_extensions = [".srt", ".sub", ".smi"]
    if get_extension(file.lower()) in sub_extensions:
        return True
    return False  

def isiso(file):
    iso_extensions = [".iso", ".avhdx", ".vhdx", ".img", ".rar"]
    if get_extension(file.lower()) in iso_extensions:
        return True
    return False      

def ismedia(file):
    if ismovie(file): return True
    if issubtitle(file): return True
    if isphoto(file): return True
    if isaudio(file): return True
    if isiso(file): return True
    return False

def check_folder(folder):
    try:
        os.listdir(folder)
        return True
    except:
        return False