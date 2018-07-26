from flask import Flask, render_template, request, send_file, abort
from geopy.geocoders import Nominatim
import pandas
import datetime

import os
from werkzeug.utils import secure_filename

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    global filename
    if request.method=='POST':
        file=request.files["file"]
        try:
            df = pandas.read_csv(file)
            nom=Nominatim()
            # df["Address"] = df["Address"] + ", " + df["Locality"]
            df["Coordinates"]=df["Address"].apply(nom.geocode)
            df["Latitude"]=df["Coordinates"].apply(lambda x: x.latitude if x != None else None)
            df["Longitude"]=df["Coordinates"].apply(lambda x: x.longitude if x != None else None)
            df=df.drop("Coordinates", 1)
            filename = datetime.datetime.now().strftime("uploads/+%Y-%m-%d-%H-%M-%S-%f"+".csv")
            df.to_csv(filename, index=None)
            final_table = df.to_html(classes="table table-dark")
            return render_template("index.html", html=final_table, btn="download.html")
        except:
            return render_template("index.html", html='<div class="alert alert-warning" role="alert">Yout file do not contain Address column!</div>')
            

@app.route("/download")
def download():
    return send_file(filename, attachment_filename='yourfile.csv', as_attachment=True)


if __name__ == '__main__':
    app.debug=True
    app.run()
