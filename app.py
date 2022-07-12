from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)

@app.route("/home")
def home():
        return render_template("index.html")

@app.route("/projects")
def projects():
        return render_template("projects.html")

@app.route("/tutorials")
def tutorials():
        return render_template("tutorials.html")

if __name__ == "__main__":
    app.run(debug=True)
