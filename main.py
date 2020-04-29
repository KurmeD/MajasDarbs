#from flask import Flask, render_template

#app = Flask(__name__)
import os
from flask import Flask, render_template, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy
app = Flask('app')

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

class test(db.Model):
    col = db.Column(db.String(255), primary_key=True)
    col2 = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self):
        return '%r' % self.col

@app.route('/')
def root():
  return render_template('index.html')
#  return render_template('atminasspele.html')

@app.route('/atminasspele')
def spele():
 return render_template('atminasspele.html')

@app.route('/rezultati')
def rezultati():
 return render_template('rezultati.html')

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

#@app.route('/atminasspele')
#def spele#_page():
#  return render_template('chats.html')

@app.route('/health')
def health_check():
  return "OK"

@app.route('/chats/lasi')
def ielasit_chatu():
  chata_rindas=[]
  with open("chats.txt", "r", encoding="UTF-8") as f:
    for rinda in f:
      chata_rindas.append(rinda)
      
  return jsonify({"chats": chata_rindas})


@app.route('/chats/suuti', methods= ['POST'])
def suuti_zinju():
  dati = request.json

  with open("chats.txt", "a", newline="", encoding="UTF-8") as f:
    f.write(dati["autors"]+": "+dati["chats"] + "\n")

  return ielasit_chatu()



@app.route('/postgreSQL')
def postgresSQL():
  result = test.query.all()
  return '%r' % result

#app.run(host='0.0.0.0', port=8020)
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support 5000
    app.run(threaded=True, port=5000, debug=True)