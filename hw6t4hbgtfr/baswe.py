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

app.run()
