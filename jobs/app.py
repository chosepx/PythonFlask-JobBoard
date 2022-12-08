from Flask import Flask, render_template

app = Flask(__name__)

@app.route('/jobs')
def jobs():
    render_template('index.html')
    
