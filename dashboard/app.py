import streamlit as st
import pandas as pd
import plotly.express as px
from statsmodels.stats.proportion import proportions_ztest

st.set_page_config(page_title="Cookie Cats A/B Test", layout="wide")

df = pd.read_csv("data/cookie_cats.csv")

st.title("Cookie Cats: Gate Placement A/B Test")
st.caption("Does moving the level gate from 30 to 40 affect player retention?")

with st.expander("Preview raw data"):
    st.dataframe(df.head())

# --- Group sizes ---
player_counts = df["version"].value_counts()
col1, col2 = st.columns(2)
col1.metric("Gate 30 players", f"{player_counts['gate_30']:,}")
col2.metric("Gate 40 players", f"{player_counts['gate_40']:,}")


def avg_retention(df, retention_col):
    return df.groupby("version")[retention_col].mean().reset_index()


def run_retention_test(df, retention_col):
    """Two-proportion z-test comparing gate_30 vs gate_40 retention."""
    successes = df.groupby("version")[retention_col].sum()
    sample_size = df.groupby("version")[retention_col].count()
    stat, p_value = proportions_ztest(successes, sample_size)
    return stat, p_value


COLOR_MAP = {"gate_30": "#2ecc71", "gate_40": "#e74c3c"}

# --- Retention 1 ---
st.subheader("Day-1 Retention")

col_chart, col_stats = st.columns([2, 1])

with col_chart:
    stat1_df = avg_retention(df, "retention_1")
    fig1 = px.bar(stat1_df, x="version", y="retention_1", color="version",
                  color_discrete_map=COLOR_MAP)
    st.plotly_chart(fig1, width='stretch')

with col_stats:
    stat, p_value = run_retention_test(df, "retention_1")
    st.metric("P-value", f"{p_value:.4f}")
    if p_value < 0.05:
        st.success("Statistically significant")
    else:
        st.info("Not statistically significant")

# --- Retention 7 ---
st.subheader("Day-7 Retention")

col_chart, col_stats = st.columns([2, 1])

with col_chart:
    stat7_df = avg_retention(df, "retention_7")
    fig2 = px.bar(stat7_df, x="version", y="retention_7", color="version",
                  color_discrete_map=COLOR_MAP)
    st.plotly_chart(fig2, width='stretch')

with col_stats:
    stat, p_value = run_retention_test(df, "retention_7")
    st.metric("P-value", f"{p_value:.4f}")
    if p_value < 0.05:
        st.success("Statistically significant")
    else:
        st.info("Not statistically significant")

st.divider()
st.markdown("""
**Takeaway:** Day-1 retention shows no statistically significant difference between groups.
Day-7 retention shows a statistically significant *drop* for gate_40 — suggesting the
later gate placement modestly hurts longer-term engagement. Recommendation: keep the gate at level 30.
""")
