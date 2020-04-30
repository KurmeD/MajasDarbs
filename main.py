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

@app.route('/rezultati/lasi')
def ielasit_rezultatus():
  rezultatu6_rindas=[]
  rezultatu5_rindas=[]
  rezultatu4_rindas=[]
  with open("pari6.txt", "r", encoding="UTF-8") as f1:
    for rinda in f1:
      rezultatu6_rindas.append(rinda)

  with open("pari5.txt", "r", encoding="UTF-8") as f2:
    for rinda in f2:
      rezultatu5_rindas.append(rinda)

  with open("pari4.txt", "r", encoding="UTF-8") as f3:
    for rinda in f3:
      rezultatu4_rindas.append(rinda)

  return jsonify({"rezultati6": rezultatu6_rindas, "rezultati5": rezultatu5_rindas, "rezultati4": rezultatu4_rindas})


@app.route('/chats/suuti', methods= ['POST'])
def suuti_zinju():
  dati = request.json

  with open("chats.txt", "a", newline="", encoding="UTF-8") as f:
    f.write(dati["autors"]+": "+dati["chats"] + "\n")

  return ielasit_chatu()

@app.route('/rezultati/suuti', methods= ['POST'])
def suuti_rezultatu():
  dati = request.json
  jauna_rinda=str(dati["rezultats"])+" "+dati["autors"]
  rezultatu_rindas=[]
  fails=""
  if dati["limenis"]==6:
    fails="pari6.txt"
  elif dati["limenis"]==5:
    fails="pari5.txt"
  else:
    fails="pari4.txt"

  with open(fails, "r", encoding="UTF-8") as f:
    for rinda in f:
      rezultatu_rindas.append(rinda)

  f.close()
  for rinda in rezultatu_rindas:
    if dati["rezultats"] < int(rinda.split()[0]):
      rezultatu_rindas.insert(rezultatu_rindas.index(rinda),jauna_rinda)
    else:
      rezultatu_rindas.append(jauna_rinda)

  with open(fails, "w", newline="", encoding="UTF-8") as f:
    for rinda in rezultatu_rindas:
      f.write(rinda+"\n")

  return ielasit_rezultatus()



@app.route('/postgreSQL')
def postgresSQL():
  result = test.query.all()
  return '%r' % result

#app.run(host='0.0.0.0', port=8020)
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support 5000
    app.run(threaded=True, port=5000, debug=True)