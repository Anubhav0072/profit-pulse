from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# SIP Calculator
@app.route("/sip", methods=["GET", "POST"])
def sip():
    result = None
    if request.method == "POST":
        try:
            m = float(request.form["monthly"])
            r = float(request.form["rate"]) / 100 / 12
            n = int(request.form["years"]) * 12

            result = round(m * (((1+r)**n - 1)/r) * (1+r), 2)
        except:
            result = "Invalid Input"

    return render_template("sip.html", result=result)


# FD Calculator
@app.route("/fd", methods=["GET", "POST"])
def fd():
    result = None
    if request.method == "POST":
        try:
            p = float(request.form["principal"])
            r = float(request.form["rate"]) / 100
            t = int(request.form["time"])

            result = round(p * (1+r)**t, 2)
        except:
            result = "Invalid Input"

    return render_template("fd.html", result=result)


# SSY Calculator
@app.route("/ssy", methods=["GET", "POST"])
def ssy():
    result = None
    if request.method == "POST":
        try:
            yearly = float(request.form["yearly"])
            rate = 7.6 / 100

            total = 0
            for i in range(15):
                total += yearly * ((1 + rate) ** (21 - i))

            result = round(total, 2)
        except:
            result = "Invalid Input"

    return render_template("ssy.html", result=result)


# EMI Calculator
@app.route("/emi", methods=["GET", "POST"])
def emi():
    result = None
    if request.method == "POST":
        try:
            p = float(request.form["loan"])
            r = float(request.form["rate"]) / 100 / 12
            n = int(request.form["months"])

            emi = (p * r * (1+r)**n) / ((1+r)**n - 1)
            result = round(emi, 2)
        except:
            result = "Invalid Input"

    return render_template("emi.html", result=result)


# Run App
if __name__ == "__main__":
    app.run(debug=True)