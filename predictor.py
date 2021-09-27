import numpy as np
from keras.preprocessing import image
from tensorflow.keras.models import load_model
saved_model = load_model("model/brain.h5")
status = True



def check(input_img):
    print(" your image is : " + input_img)
    print(input_img)

    img = image.load_img("images/" + input_img)
    #img = np.asarray(img)
    print(img)

    #img = np.expand_dims(img, axis=0)

    #print(img)
    output = np.argmax(model.predict(img.reshape(1,70,70,3)))

    print(output)
    return output
