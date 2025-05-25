from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
import numpy as np
import io
from PIL import Image
import pickle

app = FastAPI()

squeezenet_model = tf.keras.models.load_model('squeezenet/squeezenet.keras')
squeezenet_model.load_weights('squeezenet/squeezenet.weights.h5')

vgg19 = tf.keras.models.load_model('vgg19_knn/vgg19_features.keras')
vgg19.load_weights('vgg19_knn/vgg19_features.weights.h5')

file = open('vgg19_knn/knn.pkl', 'rb')
knn = pickle.load(file)
file.close()

class_names = ['Cordana', 'Healthy', 'Pestalotiopsis', 'Sigatoka']


@app.post("/squeezenet")
async def squeezenet_prediction(file: UploadFile = File(...)):
    img = Image.open(io.BytesIO(await file.read())).resize((224,224))
    arr = np.array(img).astype(np.float32) / 255

    image_np = np.transpose(arr, (2, 0, 1))
    image_np = np.expand_dims(image_np, axis=0).astype(np.float32)
    pred = np.argmax(squeezenet_model.predict(image_np)) 
    valid = int(pred)

    return {"message": "i love you", "prediction": valid}


@app.post('/vgg19knn')
async def vgg19knn_prediction(file: UploadFile = File(...)):
    img = Image.open(io.BytesIO(await file.read())).resize((224,224))
    arr = np.array(img).astype(np.float32) / 255

    image_np = np.expand_dims(arr, axis=0).astype(np.float32)
    features = vgg19.predict(image_np, verbose=0)
    prediction = knn.predict(features)
    knn_class = class_names[prediction[0]]
    return { "prediction": knn_class}