"""US Dental Cost Index 2026 — state-vs-state comparison tool.

Data: Real Dental Costs Data & Research Team (CC BY 4.0).
DOI: 10.5281/zenodo.20531729 — methodology: https://realdentalcosts.com/methodology
"""
import pandas as pd
import streamlit as st

st.set_page_config(page_title="US Dental Cost Comparison 2026 — State vs State",
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
    "Compare average dental prices between any two U.S. states — single implant, "
    "porcelain veneer and braces — using the open **US Dental Cost Index** "
    "([DOI 10.5281/zenodo.20531729](https://doi.org/10.5281/zenodo.20531729)) compiled by the "
    "[Real Dental Costs Data & Research Team](https://realdentalcosts.com). "
    "Pricing/market research, **not** medical advice."
)

c1, c2 = st.columns(2)
with c1:
    s1 = st.selectbox("State A", df["state"], index=int(df.index[df["code"] == "AL"][0]))
with c2:
    s2 = st.selectbox("State B", df["state"], index=int(df.index[df["code"] == "CA"][0]))

a = df[df["state"] == s1].iloc[0]
b = df[df["state"] == s2].iloc[0]

m1, m2, m3 = st.columns(3)
m1.metric(f"Implant — {s1}", f"${a.implant_avg_usd:,}",
          f"{a.implant_avg_usd - national_implant:+,} vs U.S. avg", delta_color="inverse")
m2.metric(f"Implant — {s2}", f"${b.implant_avg_usd:,}",
          f"{b.implant_avg_usd - national_implant:+,} vs U.S. avg", delta_color="inverse")
diff = abs(int(a.implant_avg_usd) - int(b.implant_avg_usd))
cheaper = s1 if a.implant_avg_usd < b.implant_avg_usd else s2
m3.metric("Same implant, price gap", f"${diff:,}", f"cheaper in {cheaper}")

st.subheader("Side-by-side: average price by procedure")
comp = pd.DataFrame({
    "Procedure": ["Single implant", "Porcelain veneer", "Braces (traditional)"],
    s1: [a.implant_avg_usd, a.veneer_avg_usd, a.braces_avg_usd],
    s2: [b.implant_avg_usd, b.veneer_avg_usd, b.braces_avg_usd],
}).set_index("Procedure")
st.bar_chart(comp)

st.subheader("Full ranking — all 50 states + DC")
proc = st.radio("Rank by", ["implant_avg_usd", "veneer_avg_usd", "braces_avg_usd", "cost_index"],
                format_func=lambda x: {"implant_avg_usd": "Implant avg $",
                                       "veneer_avg_usd": "Veneer avg $",
                                       "braces_avg_usd": "Braces avg $",
                                       "cost_index": "Composite Cost Index"}[x],
                horizontal=True)
table = df[["state", "code", "implant_avg_usd", "implant_low_usd", "implant_high_usd",
            "veneer_avg_usd", "braces_avg_usd", "cost_index", "cost_of_living_index"]] \
    .sort_values(proc).reset_index(drop=True)
table.index += 1
st.dataframe(table, use_container_width=True, height=420)

st.markdown(
    "---\n"
    "**Source & methodology:** [realdentalcosts.com/methodology](https://realdentalcosts.com/methodology) · "
    "Dataset CC BY 4.0 · State-by-state guides and cost calculators: "
    "[realdentalcosts.com](https://realdentalcosts.com)"
)
