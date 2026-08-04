# Cookie Cats A/B Test

Using the "Cookie Cats" mobile game dataset to run a real A/B test. It examines what happens when a player installs the game and is randomly assigned to either `gate_30` or `gate_40` — two versions of the game with a level-progression gate placed at different points.

The data covers 90,189 players who installed the game while the A/B test was running. Variables:

- **userid**: A unique identifier for each player.
- **version**: Whether the player was placed in the control group (`gate_30` — gate at level 30) or the treatment group (`gate_40` — gate moved to level 40).
- **sum_gamerounds**: Number of game rounds played during the first 14 days after install.
- **retention_1**: Did the player come back and play 1 day after installing?
- **retention_7**: Did the player come back and play 7 days after installing?

## Project Goal

Determine which gate placement leads to better player retention, so stakeholders have data-backed evidence for the decision rather than guesswork.

## Key Findings

A two-proportion z-test was run comparing `gate_30` vs `gate_40` at two time horizons:

| Metric | gate_30 | gate_40 | P-value | Significant? |
|---|---|---|---|---|
| Day-1 retention | 44.8% | 44.2% | 0.074 | No |
| Day-7 retention | 19.0% | 18.2% | 0.0016 | **Yes** |

**Day-1 retention** showed no statistically significant difference — the small gap is consistent with random noise.

**Day-7 retention** showed a statistically significant *drop* for `gate_40`. With ~90,000 players in the sample, a gap this size is very unlikely to be due to chance.

**Recommendation:** keep the gate at level 30. Day-7 retention is generally a stronger signal of real, lasting engagement than day-1, and the data shows `gate_40` modestly but reliably hurts it.

## Architecture



Kaggle CSVs (1 file1)
│
▼
Python / pandas (dashboard/app.py, notebooks/explore.py)
│
▼
statisical testing (statsmodel) + streamlit dashboard

## Tech Stack

- **Python** (pandas, streamlit, plotly.express) — extraction, visualization and transformation
- **Git** — version-controlled


## Interactive Dashboard

Built with Streamlit + Plotly to make the statisical comparison explorable.

![Dashboard overview: order metrics and review score comparison](data/dashboard.png)


Run it locally with:
```bash
streamlit run dashboard/app.py
```

## Setup & Reproduction

1. Download the [Cookie Cats dataset](https://www.kaggle.com/datasets/yufengsui/mobile-games-ab-testing) into `data/`
2. Install dependencies:
```bash
   pip install pandas statsmodels streamlit plotly --break-system-packages
```
3. Run the analysis or dashboard:
```bash
   python notebooks/explore.py
   streamlit run dashboard/app.py
```
