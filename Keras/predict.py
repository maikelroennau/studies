from keras.models import load_model
from keras.utils import np_utils

import dataset_loader


img_width, img_height = 48, 48

train_data_dir = 'Jaffe'

model = load_model('first_try.h5')

images, labels = dataset_loader.load_dataset_images(train_data_dir, img_width, img_height, load_backup=False, export_dataset=False)
labels = np_utils.to_categorical(labels, 7)

print model.predict_classes(images)
