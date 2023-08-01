from flask import Flask, request, render_template
import requests
import os
# set your token and pi url
token = os.environ['token']
ph_url = os.environ['ph_url']

app = Flask(__name__)


'''@app.route("/", methods=['GET', 'POST'])
def hello_world():
    return "<p>Hello, World!</p>"
'''
def disable_pi(seconds):
    url = ph_url+'/admin/api.php?disable='+str(seconds)+'&auth='+token
    r = requests.get(url)
    print(r)
    
@app.route("/", methods=['GET', 'POST'])
def pi():
    if request.method == 'POST':
        seconds = request.form['seconds']
        disable_pi(seconds)
        return render_template("pi.html", seconds=seconds)
#### #### return template with how long pihole was paused for        
    return render_template("pi.html")

