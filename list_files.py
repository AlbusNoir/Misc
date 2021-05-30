'''
Useful for listing the files in a folder
'''
import os

def main():
    path = input('Enter folder path: ')

    files = os.listdir(path)

    output_file = 'folder_contents.txt'

    os.chdir(path)

    with open(output_file, 'w') as f:
        f.write(f'Contents of {path}:\n')

        for file in files:
            ext_stripped = os.path.splitext(file)[0] + ''
            f.write(ext_stripped + '\n')



if __name__ == '__main__':
    main()
