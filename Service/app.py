from flask import Flask, jsonify
from flask_wtf.csrf import CSRFProtect

import requests

app = Flask(__name__)

app.secret_key = b'ksdfglbvlsdfbos'
csrf = CSRFProtect(app)
BASE = 'http://127.0.0.1:5001/'


# Post - /public data: {systolic, diastolic}
@app.route('/services1', methods=['GET', 'POST'])
def calculate_bp_public():
    data = "This is services1 - v5"
    return jsonify({'data': data})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5001')


