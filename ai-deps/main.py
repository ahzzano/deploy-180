from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
import numpy as np
import io
from PIL import Image
import pickle
from transformers import ViTImageProcessor, ViTForImageClassification
import torch

app = FastAPI()

vgg19 = tf.keras.models.load_model('vgg19_knn/vgg19_features.keras')
vgg19.load_weights('vgg19_knn/vgg19_features.weights.h5')

file = open('vgg19_knn/knn.pkl', 'rb')
knn = pickle.load(file)
file.close()

class_names = ['Cordana', 'Healthy', 'Pestalotiopsis', 'Sigatoka']
class_names_cosine = ['Cordona', 'Pestalotiopsis', 'Sigatoka', 'Healthy']

cosine = ViTForImageClassification.from_pretrained(
    'google/vit-base-patch16-224',
    num_labels=4,
    ignore_mismatched_sizes=True
)
cosine.load_state_dict(torch.load("warmup+cosine/warmup_cosine.pth", map_location=torch.device("cpu")))
cosine.eval()


@app.post('/vgg19knn')
async def vgg19knn_prediction(file: UploadFile = File(...)):
    img = Image.open(io.BytesIO(await file.read())).resize((224,224))
    arr = np.array(img).astype(np.float32) / 255

    image_np = np.expand_dims(arr, axis=0).astype(np.float32)
    features = vgg19.predict(image_np, verbose=0)
    prediction = knn.predict(features)
    knn_class = class_names[prediction[0]]
    return { "prediction": knn_class}

@app.post('/cosine')
async def warmupcosine_prediction(file: UploadFile = File(...)):
    img = Image.open(io.BytesIO(await file.read())).resize((224,224))
    arr = np.array(img).astype(np.float32) / 255
    image_np = np.expand_dims(arr, axis=0).astype(np.float32)
    image_np = np.transpose(image_np, (0, 3, 1, 2))
    print(image_np.shape)

    input_tensor = torch.from_numpy(image_np).float()
    prediction = cosine(input_tensor).logits
    pred_class = torch.argmax(prediction, dim=1)
    print(prediction)
    pred_int = int(pred_class.item()) 
    return { "prediction": class_names_cosine[pred_int]}