"""House price prediction service"""
<<<<<<< HEAD
import os
from dotenv import dotenv_values
from flask import Flask, request, url_for
from flask_cors import CORS
from joblib import load
from flask_httpauth import HTTPTokenAuth
from flask import send_from_directory
from utils import predict_io_bounded, predict_cpu_bounded, predict_cpu_multithread

MODEL_SAVE_PATH = 'models/linear_regression_v01.joblib'
=======

from flask import Flask, request
from flask_cors import CORS
>>>>>>> 194c62d94fc5690fff1a5395b67bd68f18a20f98

app = Flask(__name__)
CORS(app)

<<<<<<< HEAD
config = dotenv_values(".env")
auth = HTTPTokenAuth(scheme='Bearer')

tokens = {
    config['APP_TOKEN']: "user1",
}

model = load(MODEL_SAVE_PATH)


@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]

=======
>>>>>>> 194c62d94fc5690fff1a5395b67bd68f18a20f98

def predict(in_data: dict) -> int:
    """ Predict house price from input data parameters.
    :param in_data: house parameters.
    :raise Error: If something goes wrong.
    :return: House price, RUB.
    :rtype: int
    """
    area = float(in_data['area'])
<<<<<<< HEAD
    price = model.predict([[area]])
    return int(price)



@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
=======
    AVG_PRICE = 200_000                 # RUB / m2
    return int(area * AVG_PRICE)
>>>>>>> 194c62d94fc5690fff1a5395b67bd68f18a20f98


@app.route("/")
def home():
<<<<<<< HEAD
    return """
    <html>
    <head>
    <link rel="shortcut icon" href="/favicon.ico">
    </head>
    <body>
    <h1>Housing price service.</h1> Use /predict endpoint
    </body>
    </html>
    """


@app.route("/predict", methods=['POST'])
@auth.login_required
=======
    return '<h1>Housing price service.</h1> Use /predict endpoint'


@app.route("/predict", methods=['POST'])
>>>>>>> 194c62d94fc5690fff1a5395b67bd68f18a20f98
def predict_web_serve():
    """Dummy service"""
    in_data = request.get_json()
    price = predict(in_data)
    return {'price': price}


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
