from tensorflow.keras.layers import Dense, Dropout, Flatten, GlobalAveragePooling2D, Input
from tensorflow.keras.models import Model
from tensorflow.keras.applications.efficientnet import preprocess_input
from tensorflow.keras.applications import EfficientNetB1

import tensorflow as tf
import os

CATEGORIES = ['basophil', 'blast', 'eosinophil', 'erythroblast', 'ig', 'lymphocyte', 'monocyte', 'neutrophil',
               'platelet', 'smudge']
MODEL_PATH = "./model/efficientnet_10_weights_augm"

def model_efficientNet():
    base_model = EfficientNetB1(
        weights='imagenet',
        input_shape=(256, 256, 3),
        include_top=False)
    base_model.trainable = False
    x = GlobalAveragePooling2D()(base_model.output)
    x = Dense(units=1024,activation='relu')(x)
    x = Dropout(0.2)(x)
    x = Dense(units=512,activation='relu')(x)
    x = Dropout(0.2)(x)
    x = Dense(units=256,activation='relu')(x)
    x = Dropout(0.2)(x)
    # A Dense classifier
    outputs = Dense(units=10,activation='softmax')(x)
    model = Model(base_model.input, outputs)
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

def load_and_preprocess(img_filepath):
    img = tf.io.read_file(img_filepath)
    img = tf.io.decode_jpeg(img, channels=3)
    img = tf.image.resize_with_crop_or_pad(img, 256, 256)
    img = tf.cast(img, tf.float32)
    img = preprocess_input(img)
    return img

def getData(path_directory):
    files =[]
    filecategories=[]
    for index, category in enumerate(CATEGORIES):
        directory = path_directory+'/'+category
        for filename in os.listdir(directory):
            path = directory +"/" + filename
            if os.path.isfile(path):
                    files.append(path)
                    filecategories.append(index)
    return files, filecategories

def predict_img(path_directory):
    model = model_efficientNet()
    model.load_weights(MODEL_PATH)
    files, files_categories = getData(path_directory)
    dataset_eval = tf.data.Dataset.from_tensor_slices((files, files_categories))
    dataset_eval = (dataset_eval.map(lambda x, y: [load_and_preprocess(x), y], num_parallel_calls=tf.data.experimental.AUTOTUNE).prefetch(tf.data.experimental.AUTOTUNE).batch(32))
    accuracy = model.evaluate(dataset_eval)[1] * 100
    predict = model.predict(dataset_eval)
    eval_predict_class = predict.argmax(axis=1)
    eval_predict_class_name = [CATEGORIES[i] for i in eval_predict_class]
    return accuracy, files, eval_predict_class_name

# print(predict_img("./files_demo"))  #Pour test