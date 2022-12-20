from flask import Flask, render_template
import datetime as dt
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

# check on prometheus service
@app.route('/enviro')
def enviro():
    try:
        timestamp = dt.datetime.now()
        r = requests.get("http://192.168.1.68:8000/metrics", timeout=10)  # Rasberry pi 3 wireless
        if r.status_code:
            status = "UP"
        else:
            status = r.status_code
    except Exception as e:
        status = e
    return f'Enviro+ prometheus service is <b>{status}</b> at {timestamp}. Remember to flush'


# Check wled url
@app.route('/wled')
def wled():
    try:
        timestamp = dt.datetime.now()
        r = requests.get("http://192.168.1.79/", timeout=10)  # Diguno (wled) Wireless
        if r.status_code:
            status = "UP"
        else:
            status = r.status_code
    except Exception as e:
        status = e
    return f'Diguno (wled) Wireless is <b>{status}</b> at {timestamp}.'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

