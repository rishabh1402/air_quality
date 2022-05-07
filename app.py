from flask import Flask, render_template, redirect, url_for, Response, request, session
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd


app = Flask(__name__,template_folder='templates')

def graph(city):
    dp = pd.read_csv('./Air_quality.csv',encoding= 'unicode_escape')
    dp['state'] = dp['state'].str.upper()
    dp['city'] = dp['city'].str.upper()
    dp2 = dp[dp['city']==city].reset_index()
    sns.countplot(dp2['pollutant_id'])
    plt.title('Air Quality Index', size=20)
    plt.savefig("static/output.jpg")


# ROUTES
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/check", methods=["GET", "POST"])
def check():
    state = request.form['state']
    state = state.upper()
    city = request.form['city']
    city = city.upper()
    graph(city)
    return render_template("success.html")    


@app.route("/about")
def about():
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True)
