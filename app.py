"import joblib\n",     
"import numpy as np\n",     
"app = Flask(__name__)\n",     
"model = joblib.load('iris_model.pkl')\n",     
"model = joblib.load('Product_Ratings_Dataset.xls')\n",     
"@app.route('/')\n",     
"def home():\n",     
"return render_template('home.html')\n", 
