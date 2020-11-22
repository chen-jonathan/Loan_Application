from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
clf_model = pickle.load(open('beta_model_3.pkl', 'rb'))


@app.route("/")
def home():
    a = [[0, 0, 0, 0, 0, 3000, 0, 66, 360, 0, 1]]
    pred = clf_model.predict(a)
    print(pred)
    if pred == 'N':
        reasons = getFactors(a)
    return render_template("index.html", data=pred)


if __name__ == "__main__":
    app.run()

@app.route('/submit', methods=['GET', 'POST'])
def run():
    a = []
    for i in range(5):
        a.append(request.form["attribute" + str(i)])
        #if a[i] is None and i < 5:
        #    a[i] = 0
    print(a)
    pred = clf_model.predict([a])
    return render_template("index.html", data=pred)

def getFactors(a):
    a = a[0]
    factors = []
    if a[9] == 0: # Bad Credit History
        factors.append("Your Credit History is insufficient. Try getting more credit experience before applying again.")

