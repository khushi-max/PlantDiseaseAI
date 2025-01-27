#Import necessary libraries
from flask import Flask, render_template, request

import numpy as np
import os

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
#from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH ='model_inception.h5'

# Load your trained model
model = load_model(MODEL_PATH)




def pred_plant_dieas(plant_plant):
    
    
  test_image = load_img(plant_plant, target_size = (224, 224)) # load image 
  print("@@ Got Image for prediction")
  
  test_image = img_to_array(test_image)/255 # convert image to np array and normalize
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
  
  result = model.predict(test_image).round(3) # predict diseased palnt or not
  print('@@ Raw result = ', result)
  
  pred = np.argmax(result) # get the index of max value
  
  if pred==0:
        return "Diseased Apple leaf", 'applescab.html'
  elif pred==1:
        return "Diseased Apple leaf", 'Apple___Black_rot.html'
  elif pred==2:
        return "Diseased Apple leaf", 'Apple___Cedar_apple_rust.html'
  elif pred==3:
        return "Healthy Apple leaf", 'apple_healthy.html'
  elif pred==4:
        return "Healthy Blueberry leaf", 'blueberry_healthy.html'
  elif pred==5:
        return "Healthy Cherry_(including_sour) leaf", 'cherry_healthy.html'
  elif pred==6:
        return "Diseased Cherry_(including_sour) leaf", 'Cherry_(including_sour)___Powdery_mildew.html'
  elif pred==7:
        return "Diseased Corn_(maize) leaf", 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot.html'
  elif pred==8:
        return "Diseased Corn_(maize) leaf", 'Corn_(maize)___Common_rust_.html'
  elif pred==9:
        return "Healthy Corn_(maize) leaf", 'corn_healthy.html'
  elif pred==10:
       return "Diseased Corn_(maize) leaf", 'Corn_(maize)___Northern_Leaf_Blight.html'
  elif pred==11:
        return "Diseased Grape leaf", 'Grape___Black_rot.html'
  elif pred==12:
        return "Diseased Grape leaf", 'Grape___Esca_(Black_Measles).html'
  elif pred==13:
       return "Healthy Grape leaf", 'grape_healthy.html'
  elif pred==14:
        return "Diseased Grape leaf", 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot).html'
  elif pred==15:
        return "Diseased Orange leaf", 'Orange___Haunglongbing_(Citrus_greening).html'
  elif pred==16:
        return "Diseased Peach leaf", 'Peach___Bacterial_spot.html'
  elif pred==17:
        return "Healthy Peach leaf", 'peach_healthy.html'
  elif pred==18:
        return "Diseased Pepper,_bell leaf", 'Pepper,_bell___Bacterial_spot.html'
  elif pred==19:
        return "Healthy Pepper,_bell leaf", 'pepper,bell_healthy.html'
  elif pred==20:
       return "Diseased Potato leaf", 'Potato___Early_blight.html'
  elif pred==21:
        return "Healthy Potato leaf", 'potato_healthy.html'
  elif pred==22:
        return "Diseased Potato leaf", 'Potato___Late_blight.html'
  elif pred==23:
       return "Healthy Raspberry leaf", 'raspberry_healthy.html'
  elif pred==24:
        return "Healthy Soybean leaf", 'soybean_healthy.html'
  elif pred==25:
        return "Diseased Squash leaf", 'Squash___Powdery_mildew.html'
  elif pred==26:
        return "Healthy Strawberry leaf", 'strawberry_healthy.html'
  elif pred==27:
        return "Diseased Strawberry leaf", 'Strawberry___Leaf_scorch.html'
  elif pred==28:
       return "Diseased Tomato leaf", 'Tomato___Bacterial_spot.html'
  elif pred==29:
        return "Diseased Tomato leaf", 'Tomato___Early_blight.html'
  elif pred==30:
        return "Healthy Tomato leaf", 'tomato_healthy.html'
  elif pred==31:
        return "Diseased Tomato leaf. Name of disease: Late_blight", 'Tomato___Late_blight.html'
  elif pred==32:
        return "Diseased Tomato leaf", 'Tomato___Leaf_Mold.html'
  elif pred==33:
        return "Diseased Tomato leaf", 'Tomato___Septoria_leaf_spot.html'
  elif pred==34:
        return "Diseased Tomato leaf", 'Tomato___Spider_mites Two-spotted_spider_mite.html'
  elif pred==35:
        return "Diseased Tomato leaf", 'Tomato___Target_Spot.html'
  elif pred==36:
        return "Diseased Tomato leaf", 'Tomato___Tomato_mosaic_virus.html'
  else: 
       return "Diseased Tomato leaf", 'Tomato___Tomato_Yellow_Leaf_Curl_Virus.html'
    
    


@app.route("/", methods=['GET', 'POST'])
def home():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
   

    if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('static/useruploaded', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred, output_page = pred_plant_dieas(plant_plant=file_path)
              
        return render_template(output_page, pred_output = pred, user_image = file_path)
    

if __name__ == "__main__":
    app.run(threaded=False,) 
