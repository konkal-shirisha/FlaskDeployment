from flask import Flask, render_template, request
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
app = Flask(__name__)
model = joblib.load('Product_Ratings_Dataset.xls')
model = joblib.load('Product_Recommendation_Dataset.xls.pkl')
@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form[f'feature{i}']) for i in range(1,5)]
    except ValueError:
        return render_template('result.html',prediction="Invalid input. Please enter numeric values.")
    prediction = model.predict([features])[0]
    class_name = ['Setosa','Versicolor','Virginica']
    result = class_name[prediction]
    return render_template('result.html', prediction = result)
if __name__=='__main__':
    app.run(debug=True)
