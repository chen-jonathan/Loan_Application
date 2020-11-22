from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
clf_model = pickle.load(open('beta_model_3.pkl', 'rb'))


@app.route("/")
def home():
    a = [['0', '0', '0', '0', '0', '3000', '0', '66', '360', '0', '0']]
    pred = clf_model.predict(a)
    reasons = []
    if pred == 'N':
        reasons = getFactors(a)
    return render_template("index.html", approved=getApproved(pred), reasons=reasons, len=len(reasons))

if __name__ == "__main__":
    app.run()

@app.route('/submit', methods=['GET', 'POST'])
def run():
    a = []
    a.append(request.form['gender'])
    a.append(request.form['spouse'])
    a.append(request.form['dependent'])
    a.append(request.form['education'])
    a.append(request.form['employed'])
    for i in range(4):
        a.append(request.form["attribute" + str(i)])
    a.append(request.form['credit'])
    a.append(request.form['property'])
    reasons = []
    pred = clf_model.predict([a])
    if pred == 'N':
        reasons = getFactors([a])
    return render_template("index.html", approved=getApproved(pred), reasons=reasons, len=len(reasons))

def getApproved(pred):
    if (pred == 'Y'): return "Approved!"
    return "Not Approved."

def getFactors(a):
    a = a[0]
    print(a[10])
    factors = []
    if a[9] == '0': # Bad Credit History
        factors.append("Your Credit History is insufficient. Try getting more credit experience before applying again.")
    if a[10] == '0': # Rural Customer
        factors.append("Rural Customers have a more difficult time getting a loan based on property appreciation. Try improving other factors before applying again.")
    if int(a[7]) > 180: # High Loan
        factors.append("The borrowing amount you asked for is a little high. Please try a lower amount.")
    if a[3] == 1: # No Education
        factors.append("Your education status may impact your ability to get a loan. Lenders prefer those with a diploma or degree.")
    if int(a[5]) < 4200: # Low Income
        factors.append("The income you have provided may be too low for lenders.")
    return factors

