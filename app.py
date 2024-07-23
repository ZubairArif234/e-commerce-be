from flask import Flask
from controllers.arithmetic import arithmetic
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(arithmetic ,url_prefix='/arithmetic')



if __name__ == "__main__":
    app.run(debug=True)