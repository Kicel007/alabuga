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
from sklearn.model_selection import train_test_split

model = Sequential()

model.add(Conv2D(16, kernel_size=(3, 3), activation="relu", padding='same'))
model.add(BatchNormalization())

model.add(Conv2D(32, kernel_size=(3, 3),  activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Dropout(0.2))
model.add(Conv2D(64, kernel_size=(3, 3), activation="relu"))

model.add(Flatten())
model.add(Dropout(0.4))
model.add(Dense(100, activation='relu'))
model.add(Dense(6, activation="sigmoid"))

X_train = os.listdir(r'C:\Games\CV\cv\train\images/')
X_train = list(filter(lambda x: x.endswith(".jpg"), X_train))
X_train.sort()
X_train = np.array(list(map(lambda x: np.array(Image.open(r'C:\Games\CV\cv\train\images/' + x).convert('L')).astype('float16') / 255, X_train)))

X_train = tf.image.resize(X_train[..., np.newaxis], (300, 300))
X_train = np.array(X_train)

y_train = os.listdir(r'C:\Games\CV\cv\train\labels/')
y_train = list(filter(lambda x: x.endswith('.txt'), y_train))
y_train.sort()

y_train = list(map(lambda x : list(map(lambda y : int(y[0]), open(r'C:\Games\CV\cv\train\labels/' + x).readlines())), y_train))

for i in range(len(y_train)):
    y_train[i] = np.argmax(np.bincount(np.array(y_train[i])))

y_train = np.array(y_train)
y = to_categorical(y_train)

X = X_train.reshape(1109, 300, 300, 1)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.07, random_state=0)

model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, verbose=1, batch_size=40, validation_split=0.2)

model.save('SvarkaBot999.keras')