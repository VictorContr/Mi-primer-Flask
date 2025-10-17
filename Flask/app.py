from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/carreras/')
def carreras():
    return render_template("carreras.html")

if __name__ == '__main__':
    app.run(debug= False)