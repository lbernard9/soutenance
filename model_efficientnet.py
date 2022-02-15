from tensorflow.keras.layers import Dense, Dropout, Flatten, GlobalAveragePooling2D, Input
from tensorflow.keras.models import Model
from tensorflow.keras.applications.efficientnet import preprocess_input
from tensorflow.keras.applications import EfficientNetB1

import tensorflow as tf

MODEL_PATH = "./model/efficientnet_10_weights_augm"

class model_efficientnet:
    model = None
    def __init__(self):
        self.model = self.define_model()
        self.model.load_weights(MODEL_PATH)


    def define_model(self):
        base_model = EfficientNetB1(
            weights='imagenet',
            input_shape=(256, 256, 3),
            include_top=False)
        base_model.trainable = False
        x = GlobalAveragePooling2D()(base_model.output)
        x = Dense(units=1024, activation='relu')(x)
        x = Dropout(0.2)(x)
        x = Dense(units=512, activation='relu')(x)
        x = Dropout(0.2)(x)
        x = Dense(units=256, activation='relu')(x)
        x = Dropout(0.2)(x)
        # A Dense classifier
        outputs = Dense(units=10, activation='softmax')(x)
        model = Model(base_model.input, outputs)
        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        return model


    def load_and_preprocess(self, img_filepath):
        img = tf.io.read_file(img_filepath)
        img = tf.io.decode_jpeg(img, channels=3)
        img = tf.image.resize_with_crop_or_pad(img, 256, 256)
        img = tf.cast(img, tf.float32)
        img = preprocess_input(img)
        return img

    def format_dataset(self, data: tuple):
        dataset_eval = tf.data.Dataset.from_tensor_slices(data)
        dataset_eval = (dataset_eval.map(lambda x, y: [self.load_and_preprocess(x), y],
                                         num_parallel_calls=tf.data.experimental.AUTOTUNE).prefetch(tf.data.experimental.AUTOTUNE).batch(32))
        return dataset_eval

    def evaluate(self, dataset_eval):
        return self.model.evaluate(dataset_eval)

    def predict(self, dataset_eval):
        return self.model.predict(dataset_eval)