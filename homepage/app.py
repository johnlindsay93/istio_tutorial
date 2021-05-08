from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from forms import QueryServices
import requests

app = Flask(__name__)

app.secret_key = b'ksdfglbvlsdfbos'
csrf = CSRFProtect(app)
BASE = 'http://service:5001/'


@app.route("/", methods=['GET', 'POST'])
def home():
    form = QueryServices()
    if form.validate_on_submit():
        response = requests.get(BASE + f"services1")
        response = response.json()
        return render_template("home.html", form=form, value=response["data"])
    return render_template("home.html", form=form)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


