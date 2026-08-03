import pandas as pd

df = pd.read_csv("data/cookie_cats.csv")

#print(df.head())


print(df.groupby("version")["retention_1"].sum())


from statsmodels.stats.proportion import proportions_ztest
successes = [20034, 20119]
sample_sizes = [44700, 45489]
stat,p_value = proportions_ztest(successes,sample_sizes)

print(successes)
print(sample_sizes)
