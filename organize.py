import os
import extensions
from pathlib import Path


def Organize(path):
    try:
    
        target_dir = path

        all_files = os.listdir(target_dir)
        all_fext = []

        # split all file extensions from the dir
        for f in all_files:
            _, fext = os.path.splitext(f)
            if fext not in all_fext and fext != "":
                all_fext.append(fext)

        # create all dirs to organise files
        for ext in all_fext:
            try:
                ex = extensions.extension_paths[ext]
            except:
                ex = "other\\uncategorized"
            f_path = os.path.join(target_dir, ex)
            if os.path.isdir(f_path) == False:
                if ext:
                    Path(f_path).mkdir(parents=True, exist_ok=True)

        # move all files to their respective dirs
        for f in all_files:
            if os.path.isdir(os.path.join(target_dir, f)) == False:
                _, ext = os.path.splitext(f)
                try:
                    ex = extensions.extension_paths[ext]
                except:
                    ex = "other\\uncategorized"
                old_path = os.path.join(target_dir, f)
                new_path = os.path.join(target_dir, ex, f)
                os.rename(old_path, new_path)
    except:
        pass    