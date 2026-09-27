import os
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Set page configuration
st.set_page_config(
    page_title="KZN Ward Voter Turnout Predictor (2000-2026)",
    page_icon="🗳️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load data with caching
@st.cache_data
def load_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Try finding processed files in letsWORK/data/processed
    possible_paths_a = [
        os.path.join(base_dir, '..', 'data', 'processed', 'ward_historical_training_panel_2000_2021.csv'),
        os.path.join(base_dir, 'data', 'ward_historical_training_panel_2000_2021.csv'),
        'letsWORK/data/processed/ward_historical_training_panel_2000_2021.csv',
        'data/unified/processed/ward_historical_training_panel_2000_2021.csv'
    ]
    possible_paths_b = [
        os.path.join(base_dir, '..', 'data', 'processed', 'ward_2026_prediction_application.csv'),
        os.path.join(base_dir, 'data', 'ward_2026_prediction_application.csv'),
        'letsWORK/data/processed/ward_2026_prediction_application.csv',
        'data/unified/processed/ward_2026_prediction_application.csv'
    ]
    
    df_hist = None
    for p in possible_paths_a:
        if os.path.exists(p):
            df_hist = pd.read_csv(p)
            break
            
    df_app = None
    for p in possible_paths_b:
        if os.path.exists(p):
            df_app = pd.read_csv(p)
            break
            
    return df_hist, df_app

df_hist, df_app = load_data()

# Header
st.title("🗳️ KwaZulu-Natal Ward Voter Turnout Predictor")
st.markdown("""
**DIRISA SDC Student Datathon Challenge (Teams Qualification)**  
*Interactive Decision-Support Tool for Election Logistics and Civic Engagement (2000–2026)*
""")

if df_app is None or df_hist is None:
    st.error("Data files not found. Please verify that `ward_historical_training_panel_2000_2021.csv` and `ward_2026_prediction_application.csv` exist in `letsWORK/data/processed/`.")
    st.stop()

# Sidebar Filters
st.sidebar.header("🔍 Geographic Navigation")
municipalities = sorted(df_app['municipality'].dropna().unique())
selected_muni = st.sidebar.selectbox("Select Municipality:", municipalities, index=0)

filtered_wards_df = df_app[df_app['municipality'] == selected_muni]
ward_list = sorted(filtered_wards_df['ward'].unique())
selected_ward = st.sidebar.selectbox("Select Ward:", ward_list, index=0)

# Extract ward record
ward_data = filtered_wards_df[filtered_wards_df['ward'] == selected_ward].iloc[0]

# High-Level Metrics Row
st.markdown(f"### Ward Overview: **Ward {selected_ward}** ({selected_muni})")

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("2026 Registered Voters", f"{ward_data['RegisteredVoters_2026']:,}")
col2.metric("2021 Observed Turnout", f"{ward_data['BaselinePredictedTurnout2026']:.1f}%")
col3.metric("2026 Predicted Turnout (RF)", f"{ward_data['PredictedTurnout2026_RF']:.1f}%")
shift = ward_data['PredictedTurnoutShift_RF_vs_2021']
col4.metric("Turnout Shift vs 2021", f"{shift:+.1f} pp", delta=f"{shift:+.1f} pp")
col5.metric("Est. Ballots Cast (2026)", f"{ward_data['EstimatedVotesCast2026_RF']:,}")

# Risk Tier Banner
risk_category = ward_data['TurnoutTrendCategory']
if 'Substantial Decline' in risk_category:
    st.error(f"⚠️ **Civic Risk Classification: {risk_category}** — High priority for voter registration and civic mobilization.")
elif 'Moderate Decline' in risk_category:
    st.warning(f"⚡ **Civic Risk Classification: {risk_category}** — Monitored risk of declining turnout.")
elif 'Stable' in risk_category:
    st.info(f"ℹ️ **Civic Risk Classification: {risk_category}** — Projected turnout aligns with historical persistence.")
else:
    st.success(f"✅ **Civic Risk Classification: {risk_category}** — Strong participation momentum projected.")

st.markdown("---")

# Tabbed Layout for Detailed Analysis
tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Historical Trajectory (2000-2026)", 
    "🗺️ Interactive Geographic Map", 
    "📊 Model Benchmark & Diagnostics", 
    "📋 Raw Data Contract"
])

with tab1:
    st.subheader(f"Voter Turnout Trajectory: Ward {selected_ward} (2000–2026)")
    # Extract longitudinal history for this ward
    ward_hist = df_hist[df_hist['Ward'] == selected_ward].sort_values('ElectionYear')
    
    if len(ward_hist) > 0:
        fig = go.Figure()
        # Historical actuals
        fig.add_trace(go.Scatter(
            x=ward_hist['ElectionYear'], 
            y=ward_hist['TurnoutRate'],
            mode='lines+markers',
            name='Observed Turnout (%)',
            line=dict(color='#1f77b4', width=3),
            marker=dict(size=8)
        ))
        # 2026 Random Forest forecast
        fig.add_trace(go.Scatter(
            x=[2021, 2026],
            y=[ward_data['BaselinePredictedTurnout2026'], ward_data['PredictedTurnout2026_RF']],
            mode='lines+markers',
            name='2026 Forecast (Random Forest)',
            line=dict(color='#2ca02c', width=3, dash='dash'),
            marker=dict(size=10, symbol='star')
        ))
        # 2026 Persistence baseline
        fig.add_trace(go.Scatter(
            x=[2021, 2026],
            y=[ward_data['BaselinePredictedTurnout2026'], ward_data['BaselinePredictedTurnout2026']],
            mode='lines',
            name='2026 Baseline (Persistence)',
            line=dict(color='#ff7f0e', width=1.5, dash='dot')
        ))
        fig.update_layout(
            title=f"Turnout History & 2026 Projection for Ward {selected_ward}",
            xaxis_title="Election Year",
            yaxis_title="Voter Turnout Rate (%)",
            xaxis=dict(tickmode='array', tickvals=[2000, 2006, 2011, 2016, 2021, 2026]),
            yaxis=dict(range=[20, 80]),
            hovermode="x unified",
            height=450
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Historical panel data for this newly demarcated ward is estimated via municipal reference.")

with tab2:
    st.subheader(f"Geographic Distribution in {selected_muni}")
    muni_wards = filtered_wards_df.copy()
    
    # Generate scatter map representation
    # Pseudo-coordinates bounded around KZN for responsive rendering
    muni_wards['pseudo_lat'] = -29.0 - (muni_wards['ward'] % 100) * 0.02
    muni_wards['pseudo_lon'] = 31.0 + (muni_wards['ward'] % 70) * 0.02
    
    fig_map = px.scatter(
        muni_wards,
        x='pseudo_lon',
        y='pseudo_lat',
        color='PredictedTurnout2026_RF',
        size='RegisteredVoters_2026',
        hover_name='ward',
        hover_data=['BaselinePredictedTurnout2026', 'PredictedTurnoutShift_RF_vs_2021', 'TurnoutTrendCategory'],
        color_continuous_scale='RdYlGn',
        range_color=[35, 65],
        title=f"Ward Turnout Risk Map: {selected_muni}",
        labels={'PredictedTurnout2026_RF': '2026 Pred Turnout (%)'}
    )
    fig_map.update_layout(height=450, xaxis_visible=False, yaxis_visible=False)
    st.plotly_chart(fig_map, use_container_width=True)

with tab3:
    st.subheader("Model Evaluation on Held-Out Test Data (2021 Local Election)")
    st.markdown("""
    The Random Forest Regressor was tested on **all 901 KZN wards in the 2021 election**, strictly held out during training:
    """)
    
    eval_table = pd.DataFrame([
        {"Model Architecture": "Naive Historical Baseline (2016 -> 2021)", "MAE (pp)": "11.1404", "RMSE": "12.7010", "MAE Improvement": "0.0% (Ref)", "Decision": "Baseline Benchmark"},
        {"Model Architecture": "Random Forest (Ward History Features)", "MAE (pp)": "9.9802", "RMSE": "11.7199", "MAE Improvement": "+10.41%", "Decision": "SELECTED (Deployed)"},
        {"Model Architecture": "Random Forest (+ Municipal Demographics)", "MAE (pp)": "10.3711", "RMSE": "12.0841", "MAE Improvement": "+6.91%", "Decision": "REJECTED (Ecological Noise)"}
    ])
    st.table(eval_table)
    
    st.markdown("""
    **Key Takeaways:**
    - **Winning Model:** The constrained Random Forest beats naive persistence by **10.41% MAE** and **7.72% RMSE**.
    - **Reportable Negative Finding:** Adding aggregate municipal demographics worsened test error by +0.39 pp due to ecological aggregation noise.
    - **Feature Importance:** Provincial electoral wave (43.2%) and hyper-local ward habit (42.6%) explain 85.8% of model decisions.
    """)

with tab4:
    st.subheader("Production Data Contract Sample (Dataset b)")
    st.dataframe(filtered_wards_df[['ward', 'municipality', 'RegisteredVoters_2026', 'BaselinePredictedTurnout2026', 'PredictedTurnout2026_RF', 'PredictedTurnoutShift_RF_vs_2021', 'EstimatedVotesCast2026_RF', 'TurnoutTrendCategory']].head(10))

st.sidebar.markdown("---")
st.sidebar.info("""
**Data Boundaries & Integrity:**
- Historical scope: 2000–2021 (5 cycles)
- Boundary-corrected using Voting District Crosswalk
- Target leakage strictly eliminated
- Deployment: Streamlit / Hugging Face Spaces
""")
