from flask import Flask, request

app = Flask(__name__)

flag = dict()


@app.route("/user", methods=["POST"])
def user():
    global flag
    if request.method == "POST":
        data = request.json
        flag["123"] = data["password"]
        return "123"


@app.route("/user/<route>")
def get_user(route):
    if request.method == "GET":
        return flag[route]


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
