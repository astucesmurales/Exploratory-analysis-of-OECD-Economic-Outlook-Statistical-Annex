# Inflation, Wages, and Labour Markets

An exploratory data analysis of inflation dynamics and labour market indicators
across OECD countries, with a focus on wage growth, unit labour costs, and
cross-country heterogeneity.

## Motivation

Recent inflation spikes in the early 2020s raised questions about the role of
labour market dynamics, particularly wage growth and unit labour costs.
This project explores whether inflation outcomes are more closely associated
with cost-based labour pressures or with traditional quantity-based indicators
such as unemployment and employment growth.

## Data

The data come from the OECD dataset *Inflation, Wages, Costs and Labour Market*,
downloaded as an Excel workbook and cleaned using custom Python scripts.
**
A link to access the data can also be sourced in *references.bib*.

- Frequency: Annual
- Coverage: OECD and selected partner economies
- Units: Annual percentage changes

## Methodology

- Data reshaped from wide to long format for cross-country analysis (including correlation plots, regression)
- Cross-sectional means, medians, and dispersion measures computed by year
- Median values preferred during high-dispersion periods
- Exploratory correlations, scatter plots, and descriptive regressions used
  to examine joint patterns between inflation and labour market variables

## Key Findings

- Inflation, wage growth, and unit labour costs all exhibit elevated dispersion
  during the early 2020s
- Median inflation provides a more representative global benchmark than the mean
  during high-inflation periods
- Wage growth and unit labour costs display strong co-movement across countries
- Unit labour costs show a stronger association with inflation than unemployment
  or employment growth

## How to Run

1. Clone the repository
2. Ensure Python 3.9+ is installed
3. Install required packages: pandas, numpy, matplotlib, seaborn, statsmodels
4. Install and render Quarto

## Limitations

- Analysis is exploratory and descriptive; results do not imply causality
- Sample size is limited by annual frequency and country coverage
- Aggregation to global medians may mask country-specific dynamics
