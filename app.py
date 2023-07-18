from flask import Flask,request,render_template 
from utils import hpp


app = Flask(__name__)


@app.route('/')      				# get method fuction
def index():
    return render_template('index.html')


@app.route('/predict',methods = ['POST'])   # post method function
def predict():
    data = request.form
    hpp_obj = hpp(data)
    result = hpp_obj.predict()
   
    return render_template('index.html',pred = result)


if __name__ == "__main__":
    app.run(debug = True) 