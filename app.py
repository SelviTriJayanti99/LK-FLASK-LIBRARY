from flask import Flask, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route("/")
def index():
    # Membaca file CSV
    df = pd.read_csv("kpop_data.csv")

    # Menghitung statistik
    average_debut = round(df['Tahun Debut'].mean(), 1)
    median_debut = df['Tahun Debut'].median()
    std_debut = round(df['Tahun Debut'].std(), 2)
    cumulative_sum = df['Tahun Debut'].cumsum().to_list()

    # Mengonversi DataFrame ke list of dicts
    kpop_groups = df.to_dict(orient='records')

    return render_template("index.html",
                           kpop_groups=kpop_groups,
                           average_debut=average_debut,
                           median_debut=median_debut,
                           std_debut=std_debut,
                           cumulative_sum=cumulative_sum)

if __name__ == "__main__":
    app.run(debug=True) 
    