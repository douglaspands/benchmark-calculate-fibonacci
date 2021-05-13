from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    @app.route("/fibonacci/v1/sequence/<int:number>")
    def fibonacci_sequence(number):
        f = [0, 1]
        for i in range(2, number + 1):
            f.append(f[i-1] + f[i-2])
        return jsonify(data={"value": f[number]})

    return app
