import pandas as pd

df = pd.read_csv("data/cookie_cats.csv")

print(df.head())

print(df["version"].value_counts())


retention_1 = df.groupby("version")["retention_1"].mean()
print(retention_1)

gate_30_success = df[df["version"] == "gate_30"].value_counts()
print(gate_30_success)


gate_40_success = df[df["version"] == "gate_40"].value_counts()
print(gate_40_success)

