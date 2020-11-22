from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
clf_model = pickle.load(open('beta_model_3.pkl', 'rb'))


@app.route("/")
def home():
    #a = [[9461, 10000, 637, 406597.5, 202500.0]]
    #pred = clf_model.predict(a)
    pred = []
    return render_template("index.html", data=pred)


if __name__ == "__main__":
    app.run()

@app.route('/submit', methods=['GET', 'POST'])
def run():
    a = []
    a.append(request.form(['gender']))
    a.append(request.form(['spouse']))
    a.append(request.form(['dependent']))
    a.append(request.form(['education']))
    a.append(request.form(['employed']))
    for i in range(5):
        a.append(request.form["attribute" + str(i)])

    a.append(request.form(['property']))
    print(a)
    pred = clf_model.predict(a)
    return render_template("index.html", data=pred)
