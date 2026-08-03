import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/cookie_cats.csv")


st.set_page_config(page_title="Cookie cats AB testing")

st.dataframe(df.head())

player = df["version"].value_counts()

col1, col2 = st.columns(2)
col1.metric("Gate 30 players", f"{player['gate_30']:,}")
col2.metric("Gate 40 players", f"{player['gate_40']:,}")

from statsmodels.stats.proportion import proportions_ztest

def avg(df, retention_col):

    average_retention = df.groupby("version")[retention_col].mean()


    return average_retention

stat1= avg(df,"retention_1")
stat7 = avg(df,"retention_7")
st.write("retention_1:",stat1)
st.write("retention_7:",stat7)

stat1_df = stat1.reset_index()
st.write(stat1_df)

fig1 = px.bar(stat1_df,x="version",y="retention_1")
st.plotly_chart(fig1)


stat7_df = stat7.reset_index()
fig2 = px.bar(stat7_df,x="version",y="retention_7")
st.plotly_chart(fig2)


def run_retention_test(df, retention_col):
    """
    Runs a two-proportion z-test comparing retention rates
    between gate_30 and gate_40 for the given retention column.
    """

    successes = df.groupby("version")[retention_col].sum()
    sample_size = df.groupby("version")[retention_col].count()
    stat,p_value = proportions_ztest(successes,sample_size)


    return stat, p_value


stat,p_value = run_retention_test(df,"retention_1")
st.write(f"retention_1 p_value {p_value:.4f}")
if p_value < 0.05:
    st.success("Statically significant difference")
else:
    st.info("Not statistically significant")


stat,p_value = run_retention_test(df,"retention_7")
st.write(f"retention_7 p_value {p_value:.4f}")
if p_value < 0.05:
    st.success("statisticallycally significant difference")
else:
    st.info("Not statistically significant")
