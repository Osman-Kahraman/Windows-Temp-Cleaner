import os, shutil
folder = "insert your path name of temp file"

for i in os.listdir(folder):
    file_path = os.path.join(folder, i)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except PermissionError:
        pass
