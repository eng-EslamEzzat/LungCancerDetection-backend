import cv2
from keras.models import load_model
import numpy as np

my_model = load_model('my_model.h5')
def get_classification(path):
    img_test = cv2.imread(path, 0)
    img_test = cv2.resize(img_test, (256, 256))
    X_test = np.array(img_test).reshape(-1, 256, 256, 1)
    X_test = X_test / 255.0
    y_test = my_model.predict(X_test)
    y_test_bool = np.argmax(y_test, axis=1)

    if y_test_bool[0] == 0:
        return "Benign Case"
    elif y_test_bool[0] == 1:
        return "Malignant Case"
    elif y_test_bool[0] == 2:
        return "Normal Case"
    return "Unknown Case"