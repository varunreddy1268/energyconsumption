# Importing essential libraries and modules

from flask import Flask, render_template, request, Markup
import numpy as np
import pandas as pd

import requests
import config
import pickle
import io
import torch
from torchvision import transforms
from PIL import Image
import pre_processing as pre_process
import model_building as build

# ==============================================================================================
# ===============================================================================================
# ------------------------------------ FLASK APP -------------------------------------------------


app = Flask(__name__)

# render home page


@ app.route('/')
def home():
    title = 'Household Electric Power Consumption'
    return render_template('index.html', title=title)
import pandas as pd

@app.route('/do-predict', methods=['GET', 'POST'])
def disease_prediction():
    title = 'Household Electric Power Consumption'

    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files.get('file')
        if not file:
            return render_template('disease.html', title=title)
        #try:
        df = pd.read_csv(file)
        x=pre_process.preprocessing(df,"active_energy",100,2,2)
        train,target1,test,target=x.supreme_method()

        x1=build.model_building((120,1),2)
        final_model=x1.create_model()
        final_model.compile(optimizer="adam",loss="mean_squared_error")
        #print(type(final_model))
        final_model.fit(train,target1,epochs=5)
            #"""
            #prediction = predict_image(img)

            #prediction = Markup(str(disease_dic[prediction]))
            #"""
        prediction=final_model.predict(train)
          #  return render_template('disease-result.html', prediction=prediction, title=title)

        #except:
         #   pass
    return render_template('disease.html', title=title)


# ===============================================================================================
if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=3001)
