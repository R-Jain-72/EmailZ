from flask import Flask, render_template, request
import pickle

tokenizer = pickle.load(open("cv.pkl", "rb"))#rb -> read binary
model = pickle.load(open("cfl.pkl", "rb"))#clf -> classifier(model)

app = Flask(__name__)

#creating route
@app.route("/" , methods=["GET","POST"])# the / route accepts both get & post
def home():
    '''
    text = ""
    if request.method == "POST":
        text = request.form.get('email-content') 
    '''
    return render_template("index.html" ''', text=text''')

@app.route("/predict", methods=["POST"])
def predict():
    email_text = request.form.get("email-content")
    #tokenize the text
    token_email = tokenizer.transform(email_text)
    prediction = model.predict(token_email)
    prediction = 1 if prediction == 1 else -1
    return render_template("index.html", prediction=prediction, text=email_text)

if __name__ == "__main__":
    app.run(debug=True)