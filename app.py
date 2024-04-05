from flask import Flask, render_template, request, jsonify
from utils import model_predict
import pickle

tokenizer = pickle.load(open("models/cv.pkl", "rb"))#rb -> read binary
model = pickle.load(open("models/clf.pkl", "rb"))#clf -> classifier(model)

app = Flask(__name__)

#creating route
@app.route("/" , methods=["GET","POST"])# the / route accepts both get & post
def home():
    '''
    text = ""
    if request.method == "POST":
        text = request.form.get('email-content') 
    '''
    #return render_template("index.html" ''', text=text''')
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    email = request.form.get('content')
    #tokenize the text
    token_email = tokenizer.transform([email])
    prediction = model_predict(email)
    return render_template("index.html", prediction=prediction, email=email)

# Create an API endpoint
@app.route('/api/predict', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)  # Get data posted as a json
    email = data['content']
    prediction = model_predict(email)
    return jsonify({'prediction': prediction, 'email': email})  # Return prediction

if __name__ == "__main__":
    app.run(debug=True)