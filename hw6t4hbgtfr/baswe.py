import psycopg2
import flask
from flask import request, jsonify, Flask


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/v1/tavolo/all",methods=['GET'])
def l_tavoli():
    agcom = "SELECT * FROM public.tavoli;"
    con = psycopg2.connect(database="postgres", user="postgres", password="gungadin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute(agcom)

    line = cur.fetchall()
    con.commit()
    con.close()
    dic = []
    for linea in line:
        dic.append(linea)
    return jsonify(dic)


@app.route("/v1/menu/all",methods=['GET'])
def l_menu():
    agcom = "SELECT * FROM public.menu;"
    con = psycopg2.connect(database="postgres", user="postgres", password="gungadin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute(agcom)

    line = cur.fetchall()
    con.commit()
    con.close()
    dic = []
    for linea in line:
        dic.append(linea)
    return jsonify(dic)


@app.route("/v1/prenotazione/all",methods=['GET'])
def l_ordini():
    agcom = "SELECT * FROM public.prenotazioni;"
    con = psycopg2.connect(database="postgres", user="postgres", password="gungadin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute(agcom)

    line = cur.fetchall()
    con.commit()
    con.close()
    dic = []
    for linea in line:
        dic.append(linea)
    return jsonify(dic)

    
@app.route("/v1/prenotazione/rapporto",methods=['GET'])
def rap_pren():
    agcom = "select menu.nome, prenotazioni.data, tavoli.n_posti from public.menu, public.prenotazioni, public.tavoli where menu.idm = prenotazioni.idme and tavoli.idt = prenotazioni.idta;"
    con = psycopg2.connect(database="postgres", user="postgres", password="gungadin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute(agcom)

    line = cur.fetchall()
    con.commit()
    con.close()
    dic = []
    for linea in line:
        dic.append(linea)
    return jsonify(dic)

@app.route("/v1/prenotazione/indata",methods=['POST', 'GET'])
def rap_pren_data():
    agdata = request.args['data']
    agcom = "select menu.nome, prenotazioni.data, tavoli.n_posti from public.menu, public.prenotazioni, public.tavoli where prenotazioni.data >= '" + agdata +"' and menu.idm = prenotazioni.idme and tavoli.idt = prenotazioni.idta;"
    con = psycopg2.connect(database="postgres", user="postgres", password="gungadin", host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute(agcom)

    line = cur.fetchall()
    con.commit()
    con.close()
    dic = []
    for linea in line:
        dic.append(linea)
    return jsonify(dic)



app.run()
