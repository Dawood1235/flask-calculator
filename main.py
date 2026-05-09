from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def result():
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")
    operation = request.args.get("operation")

    if not num1 or not num2 or not operation:
        return render_template("index.html")

    num1 = float(num1)
    num2 = float(num2)

    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        return None
