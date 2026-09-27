# KZN Election Turnout Predictor (2000–2026)

## 1. What the System Offers

The **KZN Election Turnout Predictor** is an interactive, executive-grade decision-support system designed to forecast ward-level voter participation for South Africa's 2026 Local Government Elections across all 921 wards in KwaZulu-Natal, with full longitudinal exploration spanning 2000 to 2026.

Live Cloud Application: [SPU Election Turnout Predictor KZN](https://kzn-election-turnout-predictor-zjgdsdekfa7zfxqsdaotwa.streamlit.app/)

### Key Capabilities:
- **Democratic Participation & Population Coverage Indicator:** A dedicated multi-metric banner comparing **Overall Resident Population** (StatsSA baseline), **Registered Voters on Roll**, **Active Ballots Cast (Votes)**, and the **Non-Voting Population Gap**. Dynamically recalculates across statewide ($12.4\text{M}$ pop), district, municipal, and ward filter levels, with transparent data governance disclosures.
- **Analytical Justification: "Who is Not Voting, and Where Are They Located?":** Integrated analytical briefing diagnosing non-voting cohorts (disaffected youth aged 18–29, informal settlement residents facing municipal service failure, and deep rural subsistence households) and mapping their geographic hotspots (eThekwini peri-urban belt, northern traditional rural corridor, and declining industrial midland towns).
- **Dual Temporal Selection Mode (Single Year & Year Range):** Choose between **Single Year** (instant evaluation of individual election cycles: 2026 Projected, 2021, 2016, 2011, 2006, 2000) or **Year Range** (custom temporal windows like `2011 to 2022` or `2000 to 2026` with automatic cycle detection and multi-cycle ballot accumulation).
- **Stakeholder Review & National Scaling Feedback System:** Built-in evaluation modal dialog allowing electoral practitioners—including **IEC officials, registered voters, journalists, academic researchers, and data scientists**—to rate model performance out of 5 stars, provide qualitative feedback, and automatically dispatch evaluations to `siyajndzobs@gmail.com`. This feedback directly drives our architectural roadmap for expanding the predictive platform to national South African coverage (4,468 wards across all 9 provinces).
- **Dedicated "Number of Votes" Forecasting Feature:** Converts turnout percentages into raw ballot volume forecasts ($2.7\text{M}–3.6\text{M}$ votes from $5.4\text{M}–6.0\text{M}$ registered voters in 2026), providing operational planners with exact ballot paper requirements.
- **Cascading Geographic Filtering:** Seamless drill-down across all 11 District Councils, 54 Local Municipalities, and 921 Wards.
- **Context-Aware Zero-Result Filter Fallback:** When a chosen party holds 0 wards in a selected municipality (e.g., DA in Nkandla), the system explains why by naming the actual plurality holders in that municipality (e.g., IFP and ANC) and preserves the geographical view.
- **Authentic Continuous Socioeconomic Indicators:** Dynamically calculates Unemployment Rate, Poverty Index, and Service Delivery Rating (continuous 1-decimal scale, e.g. 4.8 to 8.2 out of 10) across active filters.
- **Solid Party Color Cartography:** Interactive map displaying wards filled with official party colors (**ANC Green `#007A3D`**, **IFP Gold `#D99B00`**, **DA Blue `#005BA6`**, **MK Charcoal `#222222`**, **EFF Crimson `#C00000`**) with 6 indicator overlay modes.
- **Multi-Chart Analytical Engine:** Instant toggling between Turnout Trends (2000–2026), Municipal Turnout Rankings (Horizontal Bar), Distribution Histograms, Socioeconomic Driver Scatter Plots, and Turnout Shift Categories.
- **Dual Data Export Engine:** One-click CSV downloads of the filtered selection or the full statewide 921-ward 2026 master dataset.

---

## 2. Technical Methodology, Tools, and Justification

| Layer | Technology | Justification |
| :--- | :--- | :--- |
| **Predictive Modeling** | **Scikit-Learn (Random Forest Regressor)** | Selected for its proven ability to model non-linear relationships between socioeconomic distress and voter turnout without artificial linearity assumptions. Successfully reduced held-out test error by 10.4% MAE over naive baselines. |
| **Data Engine** | **Python, Pandas, NumPy** | Vectorized feature fusion, longitudinal panel harmonization (2000–2021), and sub-millisecond calculation of multi-cycle cascading filter aggregations. |
| **Geospatial & Visuals** | **Plotly Express & Graph Objects** | Interactive client-side map rendering, dynamic hover tooltips, and presentation-grade charts without requiring heavy GIS backends. |
| **User Interface** | **Streamlit** | Enterprise executive dashboard with responsive state management, clean corporate typography, and zero-clutter decision cards. |
| **Deployment Infrastructure** | **Streamlit Community Cloud** | Deployed on managed container infrastructure connected to Git for continuous integration, real-time availability, and encrypted HTTPS delivery. |

---

## 3. Data Sources and Governance

1. **Electoral Commission of South Africa (IEC)**:
   - Ward-level results across 5 municipal election cycles (2000, 2006, 2011, 2016, 2021).
   - Certified voter registration rolls and voting district counts.
2. **Statistics South Africa (StatsSA)**:
   - Census demographic resident populations (enumerated at municipal and district tiers).
   - Quarterly Labour Force Survey (QLFS Q1 2024) employment and youth absorption metrics.
   - Sub-place settlement classifications (urban, traditional, farm).
3. **Poverty & Infrastructure Metrics**:
   - Lower-Bound Poverty Line (LBPL) headcount and poverty gap assessments.
   - Municipal Infrastructure Access and continuous Service Delivery satisfaction ratings.

---

## 4. Operational Value for Stakeholders

- **Electoral Administrators (IEC)**: Translates turnout forecasts into exact ballot requirements per ward to prevent ballot shortages and queue bottlenecks.
- **Municipal Planners**: Identifies wards where chronic service delivery failure correlates directly with democratic withdrawal.
- **Civic Organizations**: Guides targeted youth voter registration drives and civic education campaigns to the wards at greatest risk of voter apathy.
