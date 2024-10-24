import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath) as archive:
        archive.extractall(dest_dir)



if __name__ == '__main__':
    extract_archive('compressed.zip',
                    r'F:\Tutorial\programming\pythonUdemy\tod_app\files')
    print('this is working')