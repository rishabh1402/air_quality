import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def graph(city):
    dp = pd.read_csv('D:/Hackathons/Delta/Air/Air_quality.csv',encoding= 'unicode_escape')
    dp2 = dp[dp['city']==city].reset_index()
    sns.countplot(dp2['pollutant_id'])
    plt.title('Air Quality Index', size=20)
    plt.savefig("./static/output.jpg")

c="Agra"
graph(c)


