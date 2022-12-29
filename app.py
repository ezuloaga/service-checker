from flask import Flask, render_template, url_for
import datetime as dt
import requests

app = Flask(__name__)

# Define the services
services_to_monitor =	{
  "service_name": ["enviro", "wleds", "unraid","pfsense"],
  "service_address": ["http://192.168.1.68:8000/metrics", "http://192.168.1.79/", "http://192.168.1.12:9100/metrics",'http://192.168.1.1:9100/metrics']
}

# Home Page
@app.route('/')
def home():
    return render_template("home.html", title='The Home Page')





# Check status of service
def service_current_status(dest):
    try:
        r = requests.get(dest, timeout=10)
        if r.status_code:
            status=True
            message='Success!'
        else:
            status=False
            message='Down!'
    except Exception as e:
        status=False
        message = e
        # print(e)
    return message

# Summary Page
@app.route('/summary')
def summary():
    # Status Summary
    list_of_dicts = [
                    {'name':'wleds','endpoint':'http://192.168.1.79/'},
                    {'name':'enviro','endpoint':'http://192.168.1.68:8000/metrics'},
                    {'name':'unraid','endpoint':'http://192.168.1.12:9100/metrics'},
                    {'name':'pfsense','endpoint':'http://192.168.1.1:9100/metrics'},
                    {'name':'home assistant','endpoint':'http://192.168.1.57:8123'}
                    ]
    # service1 = {'name':'wleds','endpoint':'http://192.168.1.79/'}
    # service2 = {'name':'enviro','endpoint':'http://192.168.1.68:8000/metrics'}
    # # List of dictionaries (dont delete)

    # result = [service_name,endpoint]
    # for endpoint in list_of_dicts:
    #     result = requests.get(dest, timeout=10)
    #     print(result.status_code)
    # service_name = list_of_dicts['name']
    # endpoint = list_of_dicts['endpoint']
    service_dict = {'name':'wleds','endpoint':'http://192.168.1.79/'}, {'name':'enviro','endpoint':'http://192.168.1.68:8000/metrics'}
    for i in service_dict:
        service = service_dict[0]
        # endpoint = service_dict.endpoint[:]
    return render_template("summary.html", service=service,  title='Service Status')


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
    return render_template("enviro.html", status=status, timestamp=timestamp, title='enviro')


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
    return render_template("wled.html", status=status, timestamp=timestamp, title='wled')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

