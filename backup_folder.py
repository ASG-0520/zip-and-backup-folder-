import os
import time

timestr = time.strftime("%H.%M_%d.%m.%Y")


def from_folder_to_zip():
    print('\n[*] You can change settings via backup_folder.py')
    # ------------------------------------------------------------------------------
    folder_will_zip = '/Users/aleksandrg./Desktop/a'    # this folder will be zipped
    path_to = '/Users/aleksandrg./Desktop/b'            # in this folder
    name_of_zip = f'{timestr}.zip'                      # with this name 
    # ------------------------------------------------------------------------------

    # {folder_will_zip} && cd ..
    work_path_split = os.path.split(folder_will_zip)[:-1]  # tuple
    work_path = "".join(work_path_split)  # str

    zip_dir = os.path.split(folder_will_zip)[-1:]
    os.chdir(work_path)  # cd "/work_path"
    os.system(f"zip -r -X {path_to}/{name_of_zip} {''.join(zip_dir)}")


def zip_in_manual():
    print()
    print('example from a to b:')
    print('cd /Users/aleksandrg./Desktop/a && cd .. && zip -r -X /Users/aleksandrg./Desktop/b/backup.zip a')
    print('-' * 60)
    print("cd {path to the folder that will be zipped} && cd .. && zip -r -X {path to new folder}/{file name.zip} "
          "{the folder you’re gonna zip} \n")


if __name__ == "__main__":
    from_folder_to_zip()
