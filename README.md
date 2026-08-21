# US Dental Cost Index by State (2026)

An independent 2026 dataset of the average single dental implant price across **all 50 U.S. states + the District of Columbia**, with a **Restorative Cost Index** (100 = national average), the state cost-of-living index and an affordability score. Compiled by the Real Dental Costs Data & Research Team.

> **Correction notice (July 2026).** Earlier releases of this dataset carried per-state `veneer_avg_usd` and `braces_avg_usd` columns and a composite `cost_index` that depended on them. Those series were derived from the implant series by fixed multipliers, not observed, and were retracted in July 2026 - see https://realdentalcosts.com/en/data-corrections/ . The current file contains the observed implant series and the **Restorative Cost Index** only. Always cite the concept DOI https://doi.org/10.5281/zenodo.20531728 (it resolves to the current version).

**Key finding:** a state's Restorative Cost Index tracks its cost of living at **Pearson r = 0.835**. Cheapest: Alabama (implant $3,759). Most expensive: California (implant $5,733).

> This is market and pricing research, **not** clinical or treatment advice.

## Columns
| Column | Type | Unit | Description |
|---|---|---|---|
| `rank` | int | - | Rank ascending by `restorative_index` (1 = cheapest) |
| `state` | string | - | State or jurisdiction name |
| `code` | string | - | USPS state code |
| `implant_avg_usd` | int | USD | Average single dental implant price (observed) |
| `restorative_index` | int | index | Implant price / national average x 100 (100 = U.S. average) |
| `cost_of_living_index` | float | index | State cost-of-living index |
| `affordability_score` | int | 0-100 | Independent access-and-value score |

## Source & citation
- Full methodology & ranking: https://realdentalcosts.com/en/us-dental-cost-index/
- Methodology: https://realdentalcosts.com/en/methodology/
- Concept DOI (Zenodo): https://doi.org/10.5281/zenodo.20531728
- License: **CC BY 4.0** - attribute to [Real Dental Costs](https://realdentalcosts.com/).
