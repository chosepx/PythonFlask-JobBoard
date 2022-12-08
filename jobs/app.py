from flask import Flask, render_template,g
import sqlite3
app = Flask(__name__)

def open_connection():
    connection = getattr('_connection') 
    if (connection == None):
        connection = sqlite3.connect(PATH)
        g._connection = sqlite3.connect(PATH)
        
    return connection

def execute_sql(sql,values = (),commit = False,single = False):
    connection = open_connection()
   
    if (commit == True):
        results = connection.commit()
    else:
        results = cursor.fetchone() if single else cursor.fetchall()
    return results

@app.teardown_appcontext
def close_connection(exception):
    connection =getattr(g,'_connection',None) 
    if(connection is not None):
        connection.close()
        
        
@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
    
PATH = 'db/jobs.sqlite'