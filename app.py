from flask import Flask
from views.api import api
from flask_cors import CORS
import config

app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(api, url_prefix="/api")
CORS(app)


@app.route("/")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.debug = app.config["DEBUG"]
    app.run(host="0.0.0.0", port=app.config["PORT"])
    # app.run(host="0.0.0.0", port=5000, ssl_context="adhoc")
    # app.run(host="0.0.0.0", port=5000, ssl_context=("cert.pem", "priv_key.pem"))
