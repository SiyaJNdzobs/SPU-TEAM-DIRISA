# SPU-DIRISA Team: KwaZulu-Natal Ward-Level Voter Turnout Predictor (2000–2026)

> **Project Navigation Note:**
> - **Final Production Pipeline:** All consolidated, end-to-end deliverables reside in [`letsWORK/`](letsWORK/) (`letsWORK/notebook/full_pipeline.ipynb` and `letsWORK/dashboard/app.py`).
> - **Exploratory Foundation:** The [`strategising/`](strategising/) folder preserves the original stage-by-stage work where team members explored raw data, tested hypotheses, and developed deep domain insights.
> - **Unified Solution:** All empirical findings and lessons learned from the `strategising/` phase directly informed and shaped the unified, presentation-grade pipeline in `letsWORK/`.

This project delivers an empirical, high-resolution machine learning forecasting system across all 921 wards in KwaZulu-Natal ahead of South Africa’s 2026 Local Government Elections. We harmonized 21 years of longitudinal IEC election records (2000–2021) with StatsSA Quarterly Labour Force Survey employment benchmarks and Census multidimensional poverty headcounts to diagnose the structural drivers of civic disengagement. By training an ensemble Random Forest predictive engine, our model forecasts ward-level turnout and quantifies the electoral impact of localized socioeconomic grievance to equip the IEC, municipal planners, and civil society with actionable operational intelligence before election day. See the live model dashboard: [SPU Election Turnout Predictor KZN](https://kzn-election-turnout-predictor-zjgdsdekfa7zfxqsdaotwa.streamlit.app/).

---

## Executive Summary & Core Platform Features

The **KZN Election Turnout Predictor** platform bridges advanced predictive modeling with practical public governance, translating complex demographic and electoral datasets into actionable intelligence:

1. **Democratic Participation & Population Coverage Indicator:**
   - Dedicated multi-metric indicator comparing **Overall Resident Population** (StatsSA Census baseline of $12.4\text{M}$ residents), **Registered Voters on Roll** ($6.03\text{M}$, $48.5\%$), **Active Ballots Cast** ($3.64\text{M}$, $29.3\%$ of population), and the **Non-Voting Population Gap** ($8.79\text{M}$, $70.7\%$).
   - Dynamically recalculates per filter across Statewide, District, Municipal, and Ward views.
   - Includes transparent data availability notes explaining official municipal census enumerations vs. ward demographic weighting.
2. **Analytical Justification: Answering "Who is Not Voting, and Where Are They Located?":**
   - **Who is Not Voting? (Demographic Profiling):** Diagnoses disaffected & unregistered youth aged 18–29 (>65% of non-voters, facing >40% youth unemployment), informal settlement residents protesting municipal service collapse, and deep rural subsistence households facing geographic isolation.
   - **Where Are They Located? (Geographic Hotspots):** Maps civic abstention clusters across the eThekwini peri-urban informal belt (Inanda, Ntuzuma, KwaMashu, Umlazi), the northern rural traditional authority corridor (Umkhanyakude, Zululand, King Cetshwayo), and post-industrial midland towns (Newcastle, Dannhauser, Endumeni).
   - Clarifies the critical distinction between the *Turnout Gap* (registered non-voters) and the *Voter Registration Gap* (unregistered eligible citizens).
3. **Interactive Year Period Range Filter (From – To):**
   - Enables users to specify any temporal window from **2000 to 2026** (e.g., `2011 to 2022`, `2016 to 2021`, or `2026 Projected`).
   - Automatically detects all historical Local Government Election cycles within the selected window (2000, 2006, 2011, 2016, 2021, 2026).
   - Computes dynamic **Mean Turnout** and **Cumulative Votes Cast** with cycle-average benchmarks across the chosen period.
4. **Dedicated "Number of Votes" Forecasting Feature:**
   - Translates abstract turnout percentages into raw ballot volume forecasts for every ward.
   - Highlights projected ballots cast in 2026 ($2.7\text{M}–3.6\text{M}$ votes across $5.4\text{M}–6.0\text{M}$ registered voters) on the 5th top KPI card, map hover tooltips, and data explorer tables.
   - Supports cumulative vote aggregations across historical periods (e.g., $8,581,014$ cumulative votes between 2011 and 2022).
5. **Authentic Ward-Level Socioeconomic & Service Delivery Linking:**
   - Overcomes historical municipal aggregate limitations by embedding continuous, ward-specific distributions benchmarked to Census and StatsSA data.
   - Dynamically recalculates Unemployment Rate, Poverty Index, and Service Delivery Rating (continuous 1-decimal scale, e.g. $4.8/10$ to $8.2/10$) across any combination of District, Municipality, Ward, and Party filters.
6. **Context-Aware Zero-Result Filter Fallback:**
   - When a user filters for a party that holds no wards in a specific municipality (e.g., searching for DA in Nkandla), the system transparently explains the local political reality (*"In Nkandla, no wards are held by DA. Electoral pluralities are held by: IFP (14 wards), ANC (2 wards)"*) while preserving the geographical view.
7. **Interactive Solid Party Color Cartography:**
   - Wards are geographically rendered within their municipal footprints using solid, official party colors: **ANC Green (`#007A3D`)**, **IFP Gold/Amber (`#D99B00`)**, **DA Blue (`#005BA6`)**, **MK Charcoal (`#222222`)**, and **EFF Crimson (`#C00000`)**.
   - Includes 6 indicator overlay modes (Party in Charge, Voter Turnout, Number of Votes, Unemployment Rate, Poverty Index, Service Delivery Rating).
8. **Strictly Runnable Pipeline Notebook (`.ipynb`):**
   - Consolidated master pipeline located at [`letsWORK/notebook/full_pipeline.ipynb`](letsWORK/notebook/full_pipeline.ipynb).
   - Built to standard Jupyter Notebook format with full Python 3 kernel metadata, robust path resolvers, and 23 pre-computed execution outputs for instant rendering on GitHub and all IDEs.

---

## Repository Architecture

```text
SPU-TEAM-DIRISA/
├── README.md                                  # Executive overview, live links, and team directory
├── requirements.txt                           # Cloud deployment dependencies contract
│
├── letsWORK/                                  # CONSOLIDATED PRODUCTION WORKSPACE
│   ├── dashboard/
│   │   ├── app.py                             # Live Streamlit decision-support application
│   │   ├── requirements.txt                   # Dashboard environment specification
│   │   └── README.md                          # Technical architecture & interface guide
│   ├── data/
│   │   ├── raw/                               # Harmonized raw inputs (IEC, StatsSA, Crosswalks)
│   │   ├── interim/                           # Standardized intermediate clean datasets
│   │   └── processed/
│   │       ├── ward_historical_training_panel_2000_2021.csv   # Dataset (a): 4,462 historical records
│   │       └── ward_2026_prediction_application.csv          # Dataset (b): 921 wards with 2026 forecasts
│   └── notebook/
│       └── full_pipeline.ipynb                # Executed 38-cell end-to-end master pipeline (.ipynb)
│
├── Problem and Solution Statements/           # STRATEGIC RESEARCH SPECIFICATION
│   └── README.md                              # KZN ground diagnostics, 4-para Problem & 4-para Solution
│
├── Technical Document Specification/          # RUBRIC-ALIGNED TECHNICAL SPECIFICATION
│   └── README.md                              # Model outputs, limitations, deployment, & code standards
│
└── strategising/                              # HISTORICAL EXPLORATION & RESEARCH STAGES
    ├── data/                                  # Staged modular datasets
    └── notebooks/                             # 15 staged modular exploration notebooks
```

---

## Team Members

| Full Name | GitHub Profile | Program |
|---|---|---|
| Lehlogonolo Mothibi | [LEHLOGONOLO09](https://github.com/LEHLOGONOLO09) | Computer Science |
| Mochene Des Rakobela | [Des-star-droid](https://github.com/Des-star-droid) | ICT |
| Seraphine Mutwambaka Bharula | [Starfire-star](https://github.com/Starfire-star) | Computer Science |
| Simamkele Jokose | [Princess24-maker](https://github.com/Princess24-maker) | ICT |
| Patsimo Roobajie | [Phatsimo883](https://github.com/Phatsimo883) | Data Science |
| Siyabonga Jose Ndzobondzobo | [SiyaJNdzobs](https://github.com/SiyaJNdzobs) | ICT |
