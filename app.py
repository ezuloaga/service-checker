from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import datetime as dt
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c040121b0ff333ddb8b3549340ee64b1'

# # Define the services
# services_to_monitor =	{
#   "service_name": ["enviro", "wleds", "unraid","pfsense"],
#   "service_address": ["http://192.168.1.68:8000/metrics", "http://192.168.1.79/", "http://192.168.1.12:9100/metrics",'http://192.168.1.1:9100/metrics']
# }

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
    monitored_services = [
                    {
                    'name':"WLED",
                    'endpoint':"http://192.168.1.79/"
                    },

                    {
                        'name':"Enviro+",
                    'endpoint':"http://192.168.1.68:8000/metrics"
                    },

                    {
                        'name':"UNRAID",
                    'endpoint':"http://192.168.1.12:9100/metrics"
                    },

                    {
                        'name':"pfSense",
                    'endpoint':"http://192.168.1.1:9100/metrics"
                    },

                    {
                        'name':"Home Assistant",
                    'endpoint':"http://192.168.1.57:8123"
                    }
                    ]
    return render_template("summary.html", monitored_services=monitored_services, title='Services Summary')


# check on ENVIRO+
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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        # return redirect(url_for('home'))
        return redirect(url_for('summary'))
    return render_template("register.html", title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('summary'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

