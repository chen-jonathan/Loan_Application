from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
clf_model = pickle.load(open('model.pkl', 'rb'))


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()


@app.route('/submit', methods=['POST'])
def run():
    a = []
    for i in range(6):
        a[i] = request.form["attribute" + str(i)]
        if a[i] is None and i < 5:
            a[i] = 0
    arr = np.array(a)
    pred = clf_model.predict(arr)
    return render_template("index.html", data=pred)
