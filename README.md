# US Dental Cost Index by State (2026)

An independent 2026 dataset of average dental prices across **all 50 U.S. states + the District of Columbia**, compiled by the Real Dental Costs Data & Research Team.

**▶ Live interactive explorer:** https://tresor4k.github.io/us-dental-cost-index/

For each jurisdiction it reports the average single dental implant price (low/avg/high), the average per-tooth veneer price, the average full-course braces price, a composite **Cost Index** (each procedure ÷ its national average × 100, so 100 = the U.S. average), the state **cost-of-living index**, and an **affordability** score (0–100).

**Key finding:** a state's dental Cost Index tracks its cost of living at **Pearson r = 0.835**. Cheapest: Alabama (Cost Index 76, implant $3,759). Most expensive: California (Cost Index 116, implant $5,733).

> This is market and pricing research, **not** clinical or treatment advice.

## Columns
| Column | Type | Unit | Description |
|---|---|---|---|
| `rank` | int | — | Rank ascending by `cost_index` (1 = cheapest) |
| `state` | string | — | State or jurisdiction name |
| `code` | string | — | USPS state code |
| `implant_avg_usd` | int | USD | Average single dental implant price |
| `implant_low_usd` | int | USD | Low end of single-implant range |
| `implant_high_usd` | int | USD | High end of single-implant range |
| `veneer_avg_usd` | int | USD | Average per-tooth veneer price |
| `braces_avg_usd` | int | USD | Average full-course braces price |
| `cost_index` | int | index | Composite index (100 = U.S. national average) |
| `cost_of_living_index` | float | index | State cost-of-living index |
| `affordability_score` | int | 0–100 | Independent access-and-value score |

## Source & citation
- Full methodology & ranking: https://realdentalcosts.com/en/us-dental-cost-index/
- Citable DOI (Zenodo): https://doi.org/10.5281/zenodo.20531729
- License: **CC BY 4.0** — attribute to [Real Dental Costs](https://realdentalcosts.com/).
