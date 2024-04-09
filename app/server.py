from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return "<h1 style=color:blue>Hello</h1>"

@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)