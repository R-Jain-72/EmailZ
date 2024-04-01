from flask import Flask

#create instance of flask
app = Flask(__name__)#__name__ refers to the current module

#creating route
@app.route("/")
def home():
    return "Hello Duniya"

if __name__ == "__main__":
    app.run(debug=True)