import numpy as np
import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from sklearn.preprocessing import MinMaxScaler
from keras.layers import Dense
from keras.layers import Flatten
from keras.models import Sequential
from keras.models import load_model
from PIL import Image, ImageDraw
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization, Conv1D, Flatten, MaxPooling1D, Embedding, Conv2D, MaxPooling2D
import tensorflow as tf



model = load_model(r'SvarkaBot999.keras')


answers = ['Bad Welding',
               'Crack',
               'Excess Reinforcement',
               'Good Welding',
               'Porosity',
               'Spatters']
def get_defect(image):
    image = tf.image.resize((np.array(Image.open(image).convert('L')).astype('float16') / 255)[..., np.newaxis], (300, 300))
    image = np.array(image)

    indx = model.predict(np.array([image])).argmax(axis=1)[0]

    return answers[indx]

