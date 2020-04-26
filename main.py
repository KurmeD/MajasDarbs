#import os #db
#from flask import Flask, render_template

#app = Flask(__name__)
from flask import Flask, render_template
#from flask_sqlalchemy import SQLALchemy #db


app = Flask('app')
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']#db
#db = SQLALchemy(app)#db

#class test(db.Model):
#  col =db.Column(db.String(255), primary_key=True)
#  col2 = db.Column(db.String(255), unique=True, nullable=False) 
#    def __repr__(self):
#      return '%r' % self.col

@app.route('/')
def root():
  return render_template('index.html')
#  return render_template('atminasspele.html')

@app.route('/atminasspele')
def spele():
  return render_template('atminasspele.html')

@app.route('/kalkulators')
def kalkulators():
  return render_template('kalkulators.html')
  
@app.route('/saites')
def saites():
  return render_template('saites.html')
@app.route('/veidotaji')
def veidotaji():
  return render_template('veidotaji.html')

@app.route('/rezultati')
def results():
  return render_template('rezultati.html')

@app.route('/postgresSQL')
def postgresSQL();
  result=test.query.all()
  return '%r' % result

#app.run(host='0.0.0.0', port=8020)
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)