from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
clf_model = pickle.load(open('beta_model_3.pkl', 'rb'))


@app.route("/")
def home():
    a = [[0, 0, 0, 0, 0, 3000, 0, 66, 360, 0, 0]]
    pred = clf_model.predict(a)
    print(pred)
    reasons = None
    if pred == 'N':
        reasons = getFactors(a)
    print(reasons)
    return render_template("index.html", data=pred, reasons=reasons, len=len(reasons))


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

def getFactors(a):
    a = a[0]
    factors = []
    if a[9] == 0: # Bad Credit History
        factors.append("Your Credit History is insufficient. Try getting more credit experience before applying again.")
    if a[10] == 0: # Rural Customer
        factors.append("Rural Customers have a more difficult time getting a loan based on property appreciation. Try improving other factors before applying again.")
    if a[7] > 180: # High Loan
        factors.append("The borrowing amount you asked for is a little high. Please try a lower amount.")
    return factors