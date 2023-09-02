import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("./app/data.csv")
data=df[df["Country/Territory"]=="Bolivia"].iloc[:,5:13]
plt.bar(data.columns,data.values[0]);
plt.rcParams["figure.figsize"] = (5,4)
plt.xticks(rotation=45);
