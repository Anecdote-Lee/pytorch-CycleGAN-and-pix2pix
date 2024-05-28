import shutil
import os
from pathlib import Path
import argparse

def parse_cmdargs():
    parser = argparse.ArgumentParser(
        description = '이미지 파일들 정리하는 코드입니다'
    )
    parser.add_argument(
        '--root',
        help    = 'directory with images',
        dest = 'root',
        metavar = 'ROOT',
        type    = str,
    )

    return parser.parse_args()

def main():
    cmdargs = parse_cmdargs()
    folder_list = ['real_a', 'real_b', 'fake_a', 'fake_b']

    route = cmdargs.root

    for folder in folder_list:
        try:
            if not os.path.exists(route + "/ext_valid/" + folder):
                os.makedirs(route + "/ext_valid/" + folder)
        except OSError:
            print("Error: Failed to create the directory.")
        try:
            if not os.path.exists(route + "/int_valid/" + folder):
                os.makedirs(route + "/int_valid/" + folder)
        except OSError:
            print("Error: Failed to create the directory.")

    for each_file in os.listdir(route + "/images/"):
        checknmove(each_file, route)
        


def checknmove(file_name, route):
    if (file_name[:2] == 'HP') or (file_name[:2] == 'SS') or (file_name[:2] == 'AD'):
        move_route = route + "/ext_valid"
    else:
        move_route = route + "/int_valid"

    if 'fake_A' in file_name:
        shutil.copy(route+"/images/"+file_name, move_route + '/fake_a/' + file_name)
    elif 'fake_B' in file_name:
        shutil.copy(route+"/images/"+file_name, move_route + '/fake_b/' + file_name)        
    elif 'real_A' in file_name:
        shutil.copy(route+"/images/"+file_name, move_route + '/real_a/' + file_name)    
    elif 'real_B' in file_name:
        shutil.copy(route+"/images/"+file_name, move_route + '/real_b/' + file_name)       
    else:
        pass


if __name__ == '__main__':
    main()
