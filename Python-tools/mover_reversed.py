import os

images = 600
destine = '../Moved'

for dir in os.listdir('.'):
    if dir[-3:] != '.py':

        print('Processing {}'.format(dir))

        if not os.path.isdir(os.path.join(destine, dir)):
            os.makedirs(os.path.join(destine, dir))

        for i, image in enumerate(os.listdir(dir)):
            os.system('mv {} {}'.format(os.path.join(dir, image), os.path.join(destine, dir)))

            if i + 1 == images:
                break
