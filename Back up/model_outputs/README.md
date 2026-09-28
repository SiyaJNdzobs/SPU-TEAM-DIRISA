# Model Outputs, Results, and Interpretation Summary

### Problem Statement Alignment
This investigation addresses the critical question:
**"Which wards in KwaZulu-Natal are at greatest risk of catastrophic low voter turnout in the 2026 Local Government Elections, and how can resources be targeted to reverse civic disengagement?"**

In the 2021 Local Government Elections, KZN turnout collapsed from **61.4% (2016)** to **49.5% (2021)**, leaving millions of registered electors disengaged.

---

### Key Model Output Highlights (2026 Forecasts Across 921 Wards)
1. **Total Wards Forecasted:** 921 wards across all 44 municipalities in KwaZulu-Natal.
2. **Mean Projected Turnout (2026):** **60.90%** (an expected recovery of approximately 11.4 percentage points relative to the depressed 2021 baseline).
3. **Total Estimated Ballots to be Cast:** **3,636,162 votes** from an official registered roll of **6,030,969 voters**.
4. **Participation Risk Stratification:**
   - **Substantial Increase (>5pp):** 869 Wards (Communities with strong historical potential for re-engagement)
   - **Moderate Increase (1–5pp):** 48 Wards (Gradual stabilization)
   - **Stable (±1pp):** 2 Wards
   - **Moderate Decline (1–5pp):** 2 Wards (High-priority civic intervention targets)

---

### Output File Inventory
- **`kzn_ward_turnout_predictions_2026.csv`:** Full 921-ward prediction table with registered voters, predicted turnout %, expected vote volume, and risk category.
- **`model_evaluation_benchmark_scorecard.csv`:** Comparative evaluation of Baseline (MAE 11.14), Winning Model (MAE 10.14, +8.99% gain), and Rejected Model (MAE 11.48).
- **`feature_importance_ranking.csv`:** Feature weights proving past voting habit drives >70% of prediction accuracy.
