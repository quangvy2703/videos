from flask import Flask, render_template


app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
        return render_template('index.html')

app.run(host="10.142.0.13", port=5000)
