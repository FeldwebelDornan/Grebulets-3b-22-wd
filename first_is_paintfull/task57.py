import os
def find_files(locDir, locExt):
    if not os.path.isdir(locDir):
        raise ValueError("Папки нет")

    files_and_dirs = os.listdir(locDir)

    for file_or_dir in files_and_dirs:
        full_path = os.path.join(locDir,file_or_dir)
        if os.path.isdir(full_path):
            find_files(full_path,locExt)
        else:
            if full_path.endswith(locExt):
                print(full_path)
find_files('.','.py')