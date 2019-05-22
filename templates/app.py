from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route("/")
def usuario():
    db_session = db.getSession(engine)
    usuario = db_session.query(entities.Usuario)
    data = usuario[:]
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')

if __name__ == "__main__":
    app.run()
