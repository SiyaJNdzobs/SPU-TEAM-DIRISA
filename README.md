# SPU-DIRISA Team: KwaZulu-Natal Ward-Level Voter Turnout Predictor (2000–2026)

> [!IMPORTANT]
> ### 🧭 Project Navigation & Pipeline Evolution Roadmap
> 
> * **Phase 1 — Exploratory Groundwork ([`strategising/`](https://github.com/SiyaJNdzobs/SPU-TEAM-DIRISA/tree/main/strategising)):** Preserves initial stage-by-stage exploration across separated notebooks (Data Collection, Cleaning, Merging, EDA, and Modeling). Initial data collection and training yielded poor predictive performance, halting early iterations and prompting a comprehensive pipeline redesign.
> * **Phase 2 — Unified Pipeline & Historical Rectification ([`notebooks/Unified Notebook/01_End_to_End_Unified_Pipeline.ipynb`](https://github.com/SiyaJNdzobs/SPU-TEAM-DIRISA/blob/main/notebooks/Unified%20Notebook/01_End_to_End_Unified_Pipeline.ipynb)):** Consolidates exploratory steps into a cohesive pipeline, rigorously audits cleaning accuracy, and resolves the initial poor model performance by acquiring and incorporating omitted **2000 and 2006** LGE turnout cycles before retraining end-to-end.
> * **Phase 3 — Final Production Pipeline & Deployed App ([`letsWORK/`](https://github.com/SiyaJNdzobs/SPU-TEAM-DIRISA/tree/main/letsWORK)):** Final architectural refinement and retraining producing the flagship model in [`letsWORK/notebook/full_pipeline.ipynb`](https://github.com/SiyaJNdzobs/SPU-TEAM-DIRISA/blob/main/letsWORK/notebook/full_pipeline.ipynb) and driving the live cloud decision-support dashboard in [`letsWORK/dashboard/app.py`](https://github.com/SiyaJNdzobs/SPU-TEAM-DIRISA/blob/main/letsWORK/dashboard/app.py). Enhanced with **Dual Temporal Selection** (Single Year vs. Year Range) and a **Stakeholder Review & National Scaling Feedback System**.
> * **Phase 4 — Official Qualifier Submission Deliverables ([`SPU-TEAM-DIRISA-Team-Qualifier/`](https://github.com/SiyaJNdzobs/SPU-TEAM-DIRISA/tree/main/SPU-TEAM-DIRISA-Team-Qualifier)):** Complete competition submission package uploaded as an unblocked fallback after university email security stripped `.py` files. Houses the complete suite across 5 curated chapters: 1. Defined Problem Statement, 2. Working Notebook & Codebase, 3. Trained Model & Outputs, 4. [Clickable Video Submission](https://youtu.be/pvsST8agdB0), and 5. Presentation Slides, mirrored in the [`Back up/`](https://github.com/SiyaJNdzobs/SPU-TEAM-DIRISA/tree/main/Back%20up) archive.

This project delivers an empirical, high-resolution machine learning forecasting system across all 921 wards in KwaZulu-Natal ahead of South Africa’s 2026 Local Government Elections. We harmonized 21 years of longitudinal IEC election records (2000–2021) with StatsSA Quarterly Labour Force Survey employment benchmarks and Census multidimensional poverty headcounts to diagnose the structural drivers of civic disengagement. We could have done until 2024 but the LGE turnout data for the year 2024 is not yet available on the IEC page as our reliable source for this kind of data. By training an ensemble Random Forest predictive engine, our model forecasts ward-level turnout and quantifies the electoral impact of localized socioeconomic grievance to equip the IEC, municipal planners, and civil society with actionable operational intelligence before election day. See the live model dashboard: [SPU Election Turnout Predictor KZN](https://kzn-election-turnout-predictor-zjgdsdekfa7zfxqsdaotwa.streamlit.app/).

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
3. **Dual Temporal Selection Mode (Single Year & Year Range):**
   - Enables users to toggle between evaluating individual election cycles (e.g. `2026 Projected`, `2021 Observed`, `2016`, `2011`, `2006`, `2000`) or specifying custom period windows from **2000 to 2026** (e.g., `2011 to 2022`).
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
9. **Stakeholder Evaluation & National Scaling Feedback System:**
   - Features a built-in review dialog allowing **IEC officials, registered voters, journalists, academic researchers, and data scientists** to rate model reliability out of 5 stars and submit qualitative feedback.
   - Automatically transmits evaluations to us by sending them to us by email and records them to `stakeholder_reviews.csv` to directly guide our future development roadmap for scaling this predictive system from KwaZulu-Natal (921 wards) to **4,468 wards across all 9 South African provinces**.

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
| Siyabonga José Ndzobondzobo | [SiyaJNdzobs](https://github.com/SiyaJNdzobs) | ICT |
| Lehlogonolo Mothibi | [LEHLOGONOLO09](https://github.com/LEHLOGONOLO09) | Computer Science |
| Machuene Des Rakobela | [Des-star-droid](https://github.com/Des-star-droid) | ICT |
| Seraphine Mutwambaka Bharula | [Starfire-star](https://github.com/Starfire-star) | Computer Science |
| Simamkele Jokose | [Princess24-maker](https://github.com/Princess24-maker) | ICT |

