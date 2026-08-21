"""US Dental Cost Index 2026 - state-vs-state comparison tool.

Data: Real Dental Costs Data & Research Team (CC BY 4.0).
Concept DOI: 10.5281/zenodo.20531728 - methodology: https://realdentalcosts.com/en/methodology/
Correction notice (July 2026): per-state veneer and braces series were derived, not observed, and were
retracted; this app shows the observed implant series and the Restorative Cost Index only.
See https://realdentalcosts.com/en/data-corrections/
"""
import pandas as pd
import streamlit as st

st.set_page_config(page_title="US Dental Cost Comparison 2026 - State vs State",
                   page_icon="🦷", layout="wide")

CSV = "us-dental-cost-index-2026.csv"

@st.cache_data
def load():
    df = pd.read_csv(CSV)
    return df.sort_values("state").reset_index(drop=True)

df = load()
national_implant = int(df["implant_avg_usd"].mean())

st.title("🦷 US Dental Cost Comparison 2026")
st.markdown(
    "Compare the average single-implant price and the Restorative Cost Index between any two U.S. states, "
    "using the open **US Dental Cost Index** "
    "([concept DOI 10.5281/zenodo.20531728](https://doi.org/10.5281/zenodo.20531728)) compiled by the "
    "[Real Dental Costs Data & Research Team](https://realdentalcosts.com). "
    "Pricing/market research, **not** medical advice. "
    "Correction notice: earlier versions showed veneer and braces series that were derived, not observed; "
    "they were retracted in July 2026 ([details](https://realdentalcosts.com/en/data-corrections/))."
)

c1, c2 = st.columns(2)
with c1:
    s1 = st.selectbox("State A", df["state"], index=int(df.index[df["code"] == "AL"][0]))
with c2:
    s2 = st.selectbox("State B", df["state"], index=int(df.index[df["code"] == "CA"][0]))

a = df[df["state"] == s1].iloc[0]
b = df[df["state"] == s2].iloc[0]

m1, m2, m3 = st.columns(3)
m1.metric(f"Implant - {s1}", f"${a.implant_avg_usd:,}",
          f"{a.implant_avg_usd - national_implant:+,} vs U.S. avg", delta_color="inverse")
m2.metric(f"Implant - {s2}", f"${b.implant_avg_usd:,}",
          f"{b.implant_avg_usd - national_implant:+,} vs U.S. avg", delta_color="inverse")
diff = abs(int(a.implant_avg_usd) - int(b.implant_avg_usd))
cheaper = s1 if a.implant_avg_usd < b.implant_avg_usd else s2
m3.metric("Same implant, price gap", f"${diff:,}", f"cheaper in {cheaper}")

st.subheader("Side-by-side")
comp = pd.DataFrame({
    "Metric": ["Single implant (USD)", "Restorative Cost Index (100 = US avg)"],
    s1: [a.implant_avg_usd, a.restorative_index],
    s2: [b.implant_avg_usd, b.restorative_index],
}).set_index("Metric")
st.dataframe(comp, use_container_width=True)

st.subheader("Full ranking - all 50 states + DC")
proc = st.radio("Rank by", ["implant_avg_usd", "restorative_index", "affordability_score"],
                format_func=lambda x: {"implant_avg_usd": "Implant avg $",
                                       "restorative_index": "Restorative Cost Index",
                                       "affordability_score": "Affordability score"}[x],
                horizontal=True)
table = df[["state", "code", "implant_avg_usd", "restorative_index", "cost_of_living_index",
            "affordability_score"]].sort_values(proc).reset_index(drop=True)
table.index += 1
st.dataframe(table, use_container_width=True, height=420)

st.markdown(
    "---\n"
    "**Source & methodology:** [realdentalcosts.com/en/methodology](https://realdentalcosts.com/en/methodology/) · "
    "Dataset CC BY 4.0 · State-by-state guides and cost calculators: "
    "[realdentalcosts.com](https://realdentalcosts.com)"
)
