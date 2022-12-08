import Flask
import render_template 

app = Flask(__name__)

def jobs():
    render_template('index.html')
    
route('/jobs')