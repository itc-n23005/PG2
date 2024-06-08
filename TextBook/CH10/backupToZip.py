import zipfile, os

def backup_to_zip(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '-' + str(number) + '.zip'
        print("zip = " + zip_filename)
        if not os.path.exists(zip_filename):
            break
        number = number + 1

        print(f'Creating {zip_filename}')
        backup_zip = zipfile.ZipFile(zip_filename, 'w')

        for foldername, subfolders, filename in os.walk(folder):
            print(f'Adding file in {foldername}...')
            backup_zip.write(foldername)
            for filename in filenames:
                new_base = os.path.basename(folder) + '-'
                if filename.starwith(new_base) and filename.endswith('.zip'):
                    backup_zip.write(os.path.joi(foldername, filename))
                    backup_zip.close()
                    print('Done.')

backup_to_zip(r'/vagrant/PG2/TextBook/')
