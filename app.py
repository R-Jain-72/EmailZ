from flask import Flask, render_template, request

app = Flask(__name__)

#creating route
@app.route("/" , methods=["GET","POST"])# the / route accepts both get & post
def home():
    text = ""
    if request.method == "POST":
        text = request.form.get('email-content')
    return render_template("index.html", text=text)

if __name__ == "__main__":
    app.run(debug=True)