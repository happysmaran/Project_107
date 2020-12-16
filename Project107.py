import csv
import plotly.express as px
import pandas as pd

df=pd.read_csv("data.csv")

fig=px.scatter(
    df,
    x="student_id",
    y="level",
    color="student_id"
    )
fig.show();
