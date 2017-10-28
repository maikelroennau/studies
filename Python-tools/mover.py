import os
from tflearn.data_utils import shuffle


images = 400
destine = '../Moved'

for dir in os.listdir('.'):
    if dir[-3:] != '.py':

        print('Processing {}'.format(dir))

        if not os.path.isdir(os.path.join(destine, dir)):
            os.makedirs(os.path.join(destine, dir))

        if len(os.listdir(dir)) - images < 0:
            print 'Not enough images for this class'
        else:
            files = os.listdir(dir)
            shuffle(files)

            for i in range(len(files) - images):
                os.system('mv {} {}'.format(os.path.join(dir, files[i]), os.path.join(destine, dir)))
