import os
import shutil
import ntpath
from time import sleep

import progressbar

src_path = "/Users/maxmouse/Pictures/Photos Library.photoslibrary/originals"
dst_path = "/Volumes/MAXM1TFSSD/PhotoLibrary"
# nas_path = "/Volumes/NAS1/SHARED/PHOTOS/NATAN/ALL"


def find_files(path=src_path):
    print("files are:")
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))
    return files


def copy_files(src_files):
    with progressbar.ProgressBar(max_value=len(src_files)) as bar:
        copied = 0
        for orig_file in src_files:
            dst_file_path = dst_path + "/" + ntpath.basename(orig_file)
            try:
                shutil.copyfile(orig_file, dst_file_path)
            except:
                pass
            bar.update(copied + 1)
            copied += 1


def main():
    print("looking for files...")
    src_files = find_files()
    print("copying files to external drive...")
    copy_files(src_files)
    print("done")


if __name__ == "__main__":
    main()
