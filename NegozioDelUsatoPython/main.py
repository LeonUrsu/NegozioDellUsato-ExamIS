import os
import pathlib
import shutil

from Database.PathDatabase import PathDatabase




def main():
    mainPath = pathlib.Path().resolve()
    from_path = os.path.join(mainPath, "BackupFiles")
    to_path = os.path.join(mainPath, "Database")
    try:
        shutil.rmtree(to_path)
    except:
        pass
    shutil.copytree(from_path, to_path)


if __name__ == "__main__":
    main()

