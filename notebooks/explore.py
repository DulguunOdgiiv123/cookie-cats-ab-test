import pandas as pd

df = pd.read_csv("data/cookie_cats.csv")


from statsmodels.stats.proportion import proportions_ztest

def run_retention_test(df, retention_col):
    """
    Runs a two-proportion z-test comparing retention rates
    between gate_30 and gate_40 for the given retention column.
    """

    successes = df.groupby("version")[retention_col].sum()
    sample_size = df.groupby("version")[retention_col].count()
    stat,p_value = proportions_ztest(successes,sample_size)


    return stat, p_value

stat1,p1 = run_retention_test(df,"retention_1")
stat7,p7 = run_retention_test(df,"retention_7")

print("retention_1:",stat1,p1)
print("retention_7:",stat7,p7)

