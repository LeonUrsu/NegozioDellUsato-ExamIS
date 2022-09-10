import os
import pathlib
import shutil





def main():
    mainPath = pathlib.Path().resolve()
    from_path = os.path.join(mainPath, "BackupFiles")
    to_path = os.path.join(mainPath, "Database")
    try:
        shutil.rmtree(to_path)
    except:
        pass
    shutil.copytree(from_path, to_path)
    print("FATTO_A_A_A_A_AA_A__A_A_A_A_A_A__A_A")

if __name__ == "__main__":
    main()

