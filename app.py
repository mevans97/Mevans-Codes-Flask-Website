from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)

@app.route("/")
def home():
        return render_template("index.html")

@app.route("/blog")
def blog():
        return render_template("blog.html")

@app.route("/tutorials")
def tutorials():
        return render_template("tutorials.html")

if __name__ == "__main__":
    app.run(debug=True)
