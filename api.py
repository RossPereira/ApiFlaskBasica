import os
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=['GET'])
@cross_origin()
def index():
    return "<h1>Hello World</h1>"


@app.route("/somar/<int:n1>/<int:n2>", methods=['GET'])
@cross_origin()
def somar(n1, n2):
    resultado = n1 + n2
    resultado = str(resultado)
    return resultado

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()