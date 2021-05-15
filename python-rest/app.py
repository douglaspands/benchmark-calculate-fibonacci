from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    @app.route("/fibonacci/v1/sequence/<int:order>")
    def fibonacci_sequence(order):
        f = [0, 1]
        for i in range(2, order + 1):
            f.append(f[i-1] + f[i-2])
        return jsonify(data={"value": f[order]})

    return app
