from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['post'])
def my_form_post():
    text = request.form['text']
    angka = len(text)
    processed_text = text.lower()
    processed_number = int(angka)

    import pandas as pd

    #Load Data Kata
    df = pd.read_csv('data_kata_new.csv')
    #df = df.drop(labels="kelas", axis=1)
    #df = df.drop(labels="nilai", axis=1)
    #df = df.drop(labels="type", axis=1)
    df = df.astype(str)

    list_kata_df = df['lema'].tolist()
    list_kata = [o.lower() for o in list_kata_df]

    #Program
    import itertools
    from itertools import permutations, chain

    inp_kata = processed_text
    lst = []
    kata = [x.lower() for x in inp_kata]

    inp_jumlah_huruf = processed_number

    for y in list(chain.from_iterable(permutations(kata,i) for i in range (2,processed_number+1))):
        z=("".join(y))
        if len(z)>2:
            lst.append(z)

    list_hasil = [t for t in list_kata if t in lst]

    tiga_kata=[a for a in list_hasil if len(a)==3]
    empat_kata=[b for b in list_hasil if len(b)==4]
    lima_kata=[c for c in list_hasil if len(c)==5]
    enam_kata=[d for d in list_hasil if len(d)==6]
    tujuh_kata=[e for e in list_hasil if len(e)==7]

    #print([t for t in listkata if t in lst])
    string_hasil = " ".join(str(u) for u in list_hasil)

    return render_template('index_hasil.html', list_hasil=list_hasil, 
        tiga_kata=tiga_kata, empat_kata=empat_kata, lima_kata=lima_kata, 
        enam_kata=enam_kata, tujuh_kata=tujuh_kata)

@app.route('/about')
def about():
    return render_template('about_me.html')

if __name__ == "__main__":
    app.run(debug=True)

#Powershell flask
#env\Scripts\activate.ps1
#$env:FLASK_APP = ".\app.py"
#$env:FLASK_ENV = "development"

#Git Heroku
#source env/Scripts/activate
#git init
#git add .
#git commit -am 'initial'
#heroku login
#heroku git:remote -a generatortebakkata
#git push heroku master