import zipfile
import pathlib

def make_archive(for_compress,dest_dir):
    dest_dir = pathlib.Path(dest_dir,'compressed.zip')
    with zipfile.ZipFile(dest_dir,'w') as archive:
        for filepath in for_compress:
            filepath = pathlib.Path(filepath)
            archive.write(for_compress, arcname = filepath.name)



if __name__ == '__main__':
    make_archive(for_compress=['bonus.py','bonus11'],dest_dir='dest')