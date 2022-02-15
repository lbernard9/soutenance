
import os

from model_efficientnet import model_efficientnet

CATEGORIES = ['basophil', 'blast', 'eosinophil', 'erythroblast', 'ig', 'lymphocyte', 'monocyte', 'neutrophil',
               'platelet', 'smudge']

model = model_efficientnet()


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
    files, files_categories = getData(path_directory)
    dataset_eval = model.format_dataset((files, files_categories))
    accuracy = model.evaluate(dataset_eval)[1] * 100
    predict = model.predict(dataset_eval)
    eval_predict_class = predict.argmax(axis=1)
    eval_predict_class_name = [CATEGORIES[i] for i in eval_predict_class]
    return accuracy, files, eval_predict_class_name

# print(predict_img("./files_demo"))  #Pour test