
from PIL import Image, ImageOps
import numpy as np

from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.imagenet_utils import decode_predictions

import cv2


resnet = ResNet50(weights = 'imagenet')



def classification(img):
    # Load the model
    # img: PIL Image object
    
    image = np.array(img)

    image = cv2.resize(image, (224, 224))
    
    image = np.array([image])
    
    # Normalize the image
    #norm_image = (image.astype(np.float32) / 127.0) - 1

    
    output = resnet.predict(image)
    pred_class = decode_predictions(output, top = 1)[0][0][1]
    
    return pred_class # return position of the highest probability