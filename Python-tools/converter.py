import os

for directory in os.listdir('.'):
    if directory[-3:] != '.py':
        for image in os.listdir(directory):
            os.system('convert {} {}'.format(os.path.join(directory, image), os.path.join(directory, os.path.splitext(image)[0] + '.jpg')))
            os.system('rm {}'.format(os.path.join(directory, image)))